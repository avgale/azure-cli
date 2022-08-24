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
    "network local-gateway create",
)
class Create(AAZCommand):
    """Create a local VPN gateway.

    :example: Create a Local Network Gateway to represent your on-premises site.
        az network local-gateway create -g MyResourceGroup -n MyLocalGateway --gateway-ip-address 23.99.221.164 --local-address-prefixes 10.0.0.0/24 20.0.0.0/24
    """

    _aaz_info = {
        "version": "2015-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/localnetworkgateways/{}", "2015-06-15"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the local network gateway.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.location = AAZResourceLocationArg(
            help="Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.gateway_ip_address = AAZStrArg(
            options=["--gateway-ip-address"],
            help="Gateway's public IP address. (e.g. 10.1.1.1).",
        )
        _args_schema.local_address_prefixes = AAZListArg(
            options=["--address-prefixes", "--local-address-prefixes"],
            help="List of CIDR block prefixes representing the address space of the OnPremise VPN's subnet.",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...].",
        )

        local_address_prefixes = cls._args_schema.local_address_prefixes
        local_address_prefixes.Element = AAZStrArg()

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "BGP Peering"

        _args_schema = cls._args_schema
        _args_schema.asn = AAZIntArg(
            options=["--asn"],
            arg_group="BGP Peering",
            help="Autonomous System Number to use for the BGP settings.",
        )
        _args_schema.bgp_peering_address = AAZStrArg(
            options=["--bgp-peering-address"],
            arg_group="BGP Peering",
            help="IP address from the OnPremise VPN's subnet to use for BGP peering.",
        )
        _args_schema.peer_weight = AAZIntArg(
            options=["--peer-weight"],
            arg_group="BGP Peering",
            help="Weight (0-100) added to routes learned through BGP peering.",
        )

        # define Arg Group "Parameters"

        # define Arg Group "Properties"
        return cls._args_schema

    def _execute_operations(self):
        yield self.LocalNetworkGatewaysCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class LocalNetworkGatewaysCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName}",
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
                    "localNetworkGatewayName", self.ctx.args.name,
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
                    "api-version", "2015-06-15",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("bgpSettings", AAZObjectType)
                properties.set_prop("gatewayIpAddress", AAZStrType, ".gateway_ip_address")
                properties.set_prop("localNetworkAddressSpace", AAZObjectType)

            bgp_settings = _builder.get(".properties.bgpSettings")
            if bgp_settings is not None:
                bgp_settings.set_prop("asn", AAZIntType, ".asn")
                bgp_settings.set_prop("bgpPeeringAddress", AAZStrType, ".bgp_peering_address")
                bgp_settings.set_prop("peerWeight", AAZIntType, ".peer_weight")

            local_network_address_space = _builder.get(".properties.localNetworkAddressSpace")
            if local_network_address_space is not None:
                local_network_address_space.set_prop("addressPrefixes", AAZListType, ".local_address_prefixes")

            address_prefixes = _builder.get(".properties.localNetworkAddressSpace.addressPrefixes")
            if address_prefixes is not None:
                address_prefixes.set_elements(AAZStrType, ".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

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

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType()
            _schema_on_200_201.id = AAZStrType()
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.bgp_settings = AAZObjectType(
                serialized_name="bgpSettings",
            )
            properties.gateway_ip_address = AAZStrType(
                serialized_name="gatewayIpAddress",
            )
            properties.local_network_address_space = AAZObjectType(
                serialized_name="localNetworkAddressSpace",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
            )

            bgp_settings = cls._schema_on_200_201.properties.bgp_settings
            bgp_settings.asn = AAZIntType()
            bgp_settings.bgp_peering_address = AAZStrType(
                serialized_name="bgpPeeringAddress",
            )
            bgp_settings.peer_weight = AAZIntType(
                serialized_name="peerWeight",
            )

            local_network_address_space = cls._schema_on_200_201.properties.local_network_address_space
            local_network_address_space.address_prefixes = AAZListType(
                serialized_name="addressPrefixes",
            )

            address_prefixes = cls._schema_on_200_201.properties.local_network_address_space.address_prefixes
            address_prefixes.Element = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


__all__ = ["Create"]
