# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time
import os
import urllib
import urllib3
import certifi

from knack.util import CLIError
from knack.log import get_logger

from azure.cli.core.azclierror import (RequiredArgumentMissingError, ValidationError)
from azure.cli.core.commands.parameters import get_subscription_locations
from azure.cli.core.util import should_disable_connection_verify

from ._client_factory import web_client_factory

logger = get_logger(__name__)

REQUESTS_CA_BUNDLE = "REQUESTS_CA_BUNDLE"


def str2bool(v):
    if v == 'true':
        retval = True
    elif v == 'false':
        retval = False
    else:
        retval = None
    return retval


def _normalize_sku(sku):
    sku = sku.upper()
    if sku == 'FREE':
        return 'F1'
    if sku == 'SHARED':
        return 'D1'
    return sku


# FYI these function/parameter names are misnomers -- this function really maps SKU name to SKU tier, not the reverse
def get_sku_name(tier):  # pylint: disable=too-many-return-statements
    tier = tier.upper()
    if tier in ['F1', 'FREE']:
        return 'FREE'
    if tier in ['D1', "SHARED"]:
        return 'SHARED'
    if tier in ['B1', 'B2', 'B3', 'BASIC']:
        return 'BASIC'
    if tier in ['S1', 'S2', 'S3']:
        return 'STANDARD'
    if tier in ['P1', 'P2', 'P3']:
        return 'PREMIUM'
    if tier in ['P1V2', 'P2V2', 'P3V2']:
        return 'PREMIUMV2'
    if tier in ['P1V3', 'P2V3', 'P3V3']:
        return 'PREMIUMV3'
    if tier in ['PC2', 'PC3', 'PC4']:
        return 'PremiumContainer'
    if tier in ['EP1', 'EP2', 'EP3']:
        return 'ElasticPremium'
    if tier in ['I1', 'I2', 'I3']:
        return 'Isolated'
    if tier in ['I1V2', 'I2V2', 'I3V2']:
        return 'IsolatedV2'
    if tier in ['WS1', 'WS2', 'WS3']:
        return 'WorkflowStandard'
    raise ValidationError("Invalid sku(pricing tier), please refer to command help for valid values")


# resource is client.web_apps for webapps, client.app_service_plans for ASPs, etc.
def get_resource_if_exists(resource, **kwargs):
    from azure.core.exceptions import ResourceNotFoundError
    try:
        return resource.get(**kwargs)
    except ResourceNotFoundError:
        return None


def normalize_sku_for_staticapp(sku):
    if sku.lower() == 'free':
        return 'Free'
    if sku.lower() == 'standard':
        return 'Standard'
    raise ValidationError("Invalid sku(pricing tier), please refer to command help for valid values")


def retryable_method(retries=3, interval_sec=5, excpt_type=Exception):
    def decorate(func):
        def call(*args, **kwargs):
            current_retry = retries
            while True:
                try:
                    return func(*args, **kwargs)
                except excpt_type as exception:  # pylint: disable=broad-except
                    current_retry -= 1
                    if current_retry <= 0:
                        raise exception
                time.sleep(interval_sec)
        return call
    return decorate


def raise_missing_token_suggestion():
    pat_documentation = "https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line"
    raise RequiredArgumentMissingError("GitHub access token is required to authenticate to your repositories. "
                                       "If you need to create a Github Personal Access Token, "
                                       "please run with the '--login-with-github' flag or follow "
                                       "the steps found at the following link:\n{0}".format(pat_documentation))


def _get_location_from_resource_group(cli_ctx, resource_group_name):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.cli.core.profiles import ResourceType
    client = get_mgmt_service_client(cli_ctx, ResourceType.MGMT_RESOURCE_RESOURCES)
    group = client.resource_groups.get(resource_group_name)
    return group.location


def _list_app(cli_ctx, resource_group_name=None):
    client = web_client_factory(cli_ctx)
    if resource_group_name:
        result = list(client.web_apps.list_by_resource_group(resource_group_name))
    else:
        result = list(client.web_apps.list())
    for webapp in result:
        _rename_server_farm_props(webapp)
    return result


def _rename_server_farm_props(webapp):
    # Should be renamed in SDK in a future release
    setattr(webapp, 'app_service_plan_id', webapp.server_farm_id)
    del webapp.server_farm_id
    return webapp


def _get_location_from_webapp(client, resource_group_name, webapp):
    webapp = client.web_apps.get(resource_group_name, webapp)
    if not webapp:
        raise CLIError("'{}' app doesn't exist".format(webapp))
    return webapp.location


def _normalize_location(cmd, location):
    location = location.lower()
    locations = get_subscription_locations(cmd.cli_ctx)
    for loc in locations:
        if loc.display_name.lower() == location or loc.name.lower() == location:
            return loc.name
    return location


def get_pool_manager(url):
    proxies = urllib.request.getproxies()
    bypass_proxy = urllib.request.proxy_bypass(urllib.parse.urlparse(url).hostname)

    if 'https' in proxies and not bypass_proxy:
        proxy = urllib.parse.urlparse(proxies['https'])

        if proxy.username and proxy.password:
            proxy_headers = urllib3.util.make_headers(proxy_basic_auth='{0}:{1}'.format(proxy.username, proxy.password))
            logger.debug('Setting proxy-authorization header for basic auth')
        else:
            proxy_headers = None

        logger.info('Using proxy for app service tunnel connection')
        http = urllib3.ProxyManager(proxy.geturl(), proxy_headers=proxy_headers)
    else:
        http = urllib3.PoolManager()

    if should_disable_connection_verify():
        http.connection_pool_kw['cert_reqs'] = 'CERT_NONE'
    else:
        http.connection_pool_kw['cert_reqs'] = 'CERT_REQUIRED'
        if REQUESTS_CA_BUNDLE in os.environ:
            ca_bundle_file = os.environ[REQUESTS_CA_BUNDLE]
            logger.debug("Using CA bundle file at '%s'.", ca_bundle_file)
            if not os.path.isfile(ca_bundle_file):
                raise CLIError('REQUESTS_CA_BUNDLE environment variable is specified with an invalid file path')
        else:
            ca_bundle_file = certifi.where()
        http.connection_pool_kw['ca_certs'] = ca_bundle_file
    return http
