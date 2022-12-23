# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network express-route port link update",
)
class Update(AAZCommand):
    """Manage MACsec configuration of an ExpressRoute Link.

    :example: Enable MACsec on ExpressRoute Direct Ports once at a time.
        az network express-route port link update --resource-group MyResourceGroup --port-name MyExpressRoutePort --name link1 --macsec-ckn-secret-identifier MacSecCKNSecretID --macsec-cak-secret-identifier MacSecCAKSecretID --macsec-cipher GcmAes128

    :example: Enable administrative state of an ExpressRoute Link.
        az network express-route port link update --resource-group MyResourceGroup --port-name MyExpressRoutePort --name link2 --admin-state Enabled
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressrouteports/{}", "2022-01-01", "properties.links[]"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.port_name = AAZStrArg(
            options=["--port-name"],
            help="ExpressRoute port name.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.ids = AAZResourceIdArg(
            options=["--ids"],
            help="Resource ID.",
            nullable=True,
            fmt=AAZResourceIdArgFormat(
                template="/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/ExpressRoutePorts/{}/links/{}",
            ),
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The link name of the ExpressRoute Port.",
            required=True,
        )
        _args_schema.admin_state = AAZStrArg(
            options=["--admin-state"],
            help="Enable/Disable administrative state of an ExpressRoute Link.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )

        # define Arg Group "MACsec"

        _args_schema = cls._args_schema
        _args_schema.macsec_cak_secret_identifier = AAZStrArg(
            options=["--macsec-cak-secret-identifier"],
            arg_group="MACsec",
            help="The connectivity association key (CAK) ID that stored in the KeyVault.",
            nullable=True,
        )
        _args_schema.macsec_cipher = AAZStrArg(
            options=["--macsec-cipher"],
            arg_group="MACsec",
            help="Cipher Method.",
            nullable=True,
            enum={"GcmAes128": "GcmAes128", "GcmAes256": "GcmAes256", "GcmAesXpn128": "GcmAesXpn128", "GcmAesXpn256": "GcmAesXpn256"},
        )
        _args_schema.macsec_ckn_secret_identifier = AAZStrArg(
            options=["--macsec-ckn-secret-identifier"],
            arg_group="MACsec",
            help="The connectivity key name (CKN) that stored in the KeyVault.",
            nullable=True,
        )
        _args_schema.macsec_sci_state = AAZStrArg(
            options=["--macsec-sci-state"],
            arg_group="MACsec",
            help="Sci mode.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ExpressRoutePortsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.selectors.subresource.required())
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.selectors.subresource.required())
        yield self.ExpressRoutePortsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.selectors.subresource.required(), client_flatten=True)
        return result

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            result = result.properties.links
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].name == self.ctx.args.name,
                filters
            )
            idx = next(filters)[0]
            return result[idx]

        def _set(self, value):
            result = self.ctx.vars.instance
            result = result.properties.links
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].name == self.ctx.args.name,
                filters
            )
            idx = next(filters, [len(result)])[0]
            result[idx] = value
            return

    class ExpressRoutePortsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "expressRoutePortName", self.ctx.args.port_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_express_route_port_read(cls._schema_on_200)

            return cls._schema_on_200

    class ExpressRoutePortsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "expressRoutePortName", self.ctx.args.port_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_express_route_port_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.selectors.subresource.required())

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("id", AAZStrType, ".ids")
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("adminState", AAZStrType, ".admin_state")
                properties.set_prop("macSecConfig", AAZObjectType)

            mac_sec_config = _builder.get(".properties.macSecConfig")
            if mac_sec_config is not None:
                mac_sec_config.set_prop("cakSecretIdentifier", AAZStrType, ".macsec_cak_secret_identifier")
                mac_sec_config.set_prop("cipher", AAZStrType, ".macsec_cipher")
                mac_sec_config.set_prop("cknSecretIdentifier", AAZStrType, ".macsec_ckn_secret_identifier")
                mac_sec_config.set_prop("sciState", AAZStrType, ".macsec_sci_state")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.selectors.subresource,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_express_route_port_read = None

    @classmethod
    def _build_schema_express_route_port_read(cls, _schema):
        if cls._schema_express_route_port_read is not None:
            _schema.etag = cls._schema_express_route_port_read.etag
            _schema.id = cls._schema_express_route_port_read.id
            _schema.identity = cls._schema_express_route_port_read.identity
            _schema.location = cls._schema_express_route_port_read.location
            _schema.name = cls._schema_express_route_port_read.name
            _schema.properties = cls._schema_express_route_port_read.properties
            _schema.tags = cls._schema_express_route_port_read.tags
            _schema.type = cls._schema_express_route_port_read.type
            return

        cls._schema_express_route_port_read = _schema_express_route_port_read = AAZObjectType()

        express_route_port_read = _schema_express_route_port_read
        express_route_port_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        express_route_port_read.id = AAZStrType()
        express_route_port_read.identity = AAZObjectType()
        express_route_port_read.location = AAZStrType()
        express_route_port_read.name = AAZStrType(
            flags={"read_only": True},
        )
        express_route_port_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        express_route_port_read.tags = AAZDictType()
        express_route_port_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_express_route_port_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType()
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_express_route_port_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType()

        _element = _schema_express_route_port_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_express_route_port_read.properties
        properties.allocation_date = AAZStrType(
            serialized_name="allocationDate",
            flags={"read_only": True},
        )
        properties.bandwidth_in_gbps = AAZIntType(
            serialized_name="bandwidthInGbps",
        )
        properties.circuits = AAZListType(
            flags={"read_only": True},
        )
        properties.encapsulation = AAZStrType()
        properties.ether_type = AAZStrType(
            serialized_name="etherType",
            flags={"read_only": True},
        )
        properties.links = AAZListType()
        properties.mtu = AAZStrType(
            flags={"read_only": True},
        )
        properties.peering_location = AAZStrType(
            serialized_name="peeringLocation",
        )
        properties.provisioned_bandwidth_in_gbps = AAZFloatType(
            serialized_name="provisionedBandwidthInGbps",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
            flags={"read_only": True},
        )

        circuits = _schema_express_route_port_read.properties.circuits
        circuits.Element = AAZObjectType()

        _element = _schema_express_route_port_read.properties.circuits.Element
        _element.id = AAZStrType()

        links = _schema_express_route_port_read.properties.links
        links.Element = AAZObjectType()

        _element = _schema_express_route_port_read.properties.links.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_express_route_port_read.properties.links.Element.properties
        properties.admin_state = AAZStrType(
            serialized_name="adminState",
        )
        properties.connector_type = AAZStrType(
            serialized_name="connectorType",
            flags={"read_only": True},
        )
        properties.interface_name = AAZStrType(
            serialized_name="interfaceName",
            flags={"read_only": True},
        )
        properties.mac_sec_config = AAZObjectType(
            serialized_name="macSecConfig",
        )
        properties.patch_panel_id = AAZStrType(
            serialized_name="patchPanelId",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.rack_id = AAZStrType(
            serialized_name="rackId",
            flags={"read_only": True},
        )
        properties.router_name = AAZStrType(
            serialized_name="routerName",
            flags={"read_only": True},
        )

        mac_sec_config = _schema_express_route_port_read.properties.links.Element.properties.mac_sec_config
        mac_sec_config.cak_secret_identifier = AAZStrType(
            serialized_name="cakSecretIdentifier",
        )
        mac_sec_config.cipher = AAZStrType()
        mac_sec_config.ckn_secret_identifier = AAZStrType(
            serialized_name="cknSecretIdentifier",
        )
        mac_sec_config.sci_state = AAZStrType(
            serialized_name="sciState",
        )

        tags = _schema_express_route_port_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_express_route_port_read.etag
        _schema.id = cls._schema_express_route_port_read.id
        _schema.identity = cls._schema_express_route_port_read.identity
        _schema.location = cls._schema_express_route_port_read.location
        _schema.name = cls._schema_express_route_port_read.name
        _schema.properties = cls._schema_express_route_port_read.properties
        _schema.tags = cls._schema_express_route_port_read.tags
        _schema.type = cls._schema_express_route_port_read.type


__all__ = ["Update"]
