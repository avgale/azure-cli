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
    "network vnet-gateway update",
)
class Update(AAZCommand):
    """Update a virtual network gateway.

    :example: Change the SKU of a virtual network gateway.
        az network vnet-gateway update -g MyResourceGroup -n MyVnetGateway --sku VpnGw2
    """

    _aaz_info = {
        "version": "2015-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualnetworkgateways/{}", "2015-06-15"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the VNet gateway.",
            required=True,
            id_part="name",
        )
        _args_schema.gateway_default_site = AAZStrArg(
            options=["--gateway-default-site"],
            help="Name or ID of a local network gateway representing a local network site with default routes.",
            nullable=True,
        )
        _args_schema.gateway_type = AAZStrArg(
            options=["--gateway-type"],
            help="The gateway type.",
            nullable=True,
            enum={"ExpressRoute": "ExpressRoute", "Vpn": "Vpn"},
        )
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            help="VNet gateway SKU.",
            nullable=True,
            enum={"Basic": "Basic", "HighPerformance": "HighPerformance", "Standard": "Standard"},
        )
        _args_schema.vpn_type = AAZStrArg(
            options=["--vpn-type"],
            help="VPN routing type.",
            nullable=True,
            enum={"PolicyBased": "PolicyBased", "RouteBased": "RouteBased"},
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "BGP Peering"

        _args_schema = cls._args_schema
        _args_schema.asn = AAZIntArg(
            options=["--asn"],
            arg_group="BGP Peering",
            help="Autonomous System Number to use for the BGP settings.",
            nullable=True,
        )
        _args_schema.bgp_peering_address = AAZStrArg(
            options=["--bgp-peering-address"],
            arg_group="BGP Peering",
            help="IP address to use for BGP peering.",
            nullable=True,
        )
        _args_schema.peer_weight = AAZIntArg(
            options=["--peer-weight"],
            arg_group="BGP Peering",
            help="Weight (0-100) added to routes learned through BGP peering.",
            nullable=True,
        )
        _args_schema.enable_bgp = AAZBoolArg(
            options=["--enable-bgp"],
            arg_group="BGP Peering",
            help="Enable BGP (Border Gateway Protocol).",
            nullable=True,
        )

        # define Arg Group "Parameters"

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.ip_configurations = AAZListArg(
            options=["--ip-configurations"],
            arg_group="Properties",
            help="IP configurations for virtual network gateway.",
            nullable=True,
        )
        _args_schema.sku_tier = AAZStrArg(
            options=["--sku-tier"],
            arg_group="Properties",
            help="Gateway SKU tier.",
            nullable=True,
            enum={"Basic": "Basic", "HighPerformance": "HighPerformance", "Standard": "Standard"},
        )

        ip_configurations = cls._args_schema.ip_configurations
        ip_configurations.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.ip_configurations.Element
        _element.etag = AAZStrArg(
            options=["etag"],
            help="A unique read-only string that changes whenever the resource is updated.",
            nullable=True,
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the resource that is unique within a resource group. This name can be used to access the resource.",
            nullable=True,
        )
        _element.private_ip_address = AAZStrArg(
            options=["private-ip-address"],
            help="Gets or sets the privateIPAddress of the IP Configuration",
            nullable=True,
        )
        _element.private_ip_allocation_method = AAZStrArg(
            options=["private-ip-allocation-method"],
            help="The private IP address allocation method.",
            nullable=True,
            enum={"Dynamic": "Dynamic", "Static": "Static"},
        )
        _element.provisioning_state = AAZStrArg(
            options=["provisioning-state"],
            help="The provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.",
            nullable=True,
        )
        _element.public_ip_address = AAZObjectArg(
            options=["public-ip-address"],
            help="The reference to the public IP resource.",
            nullable=True,
        )
        cls._build_args_sub_resource_update(_element.public_ip_address)
        _element.subnet = AAZStrArg(
            options=["subnet"],
            help="test",
            nullable=True,
        )

        # define Arg Group "Root Cert Authentication"

        _args_schema = cls._args_schema
        _args_schema.vpn_client_root_certificates = AAZListArg(
            options=["--vpn-client-root-certificates"],
            arg_group="Root Cert Authentication",
            help="VpnClientRootCertificate for virtual network gateway.",
            nullable=True,
        )

        vpn_client_root_certificates = cls._args_schema.vpn_client_root_certificates
        vpn_client_root_certificates.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.vpn_client_root_certificates.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the resource that is unique within a resource group. This name can be used to access the resource.",
            nullable=True,
        )
        _element.public_cert_data = AAZStrArg(
            options=["public-cert-data"],
            help="The certificate public data.",
            nullable=True,
        )

        # define Arg Group "Sku"

        # define Arg Group "VPN Client"

        _args_schema = cls._args_schema
        _args_schema.address_prefixes = AAZListArg(
            options=["--address-prefixes"],
            singular_options=["--address-prefix"],
            arg_group="VPN Client",
            help="Space-separated list of CIDR prefixes representing the address space for the P2S Vpnclient.",
            nullable=True,
        )

        address_prefixes = cls._args_schema.address_prefixes
        address_prefixes.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "VpnClientConfiguration"
        return cls._args_schema

    _args_sub_resource_update = None

    @classmethod
    def _build_args_sub_resource_update(cls, _schema):
        if cls._args_sub_resource_update is not None:
            _schema.id = cls._args_sub_resource_update.id
            return

        cls._args_sub_resource_update = AAZObjectArg(
            nullable=True,
        )

        sub_resource_update = cls._args_sub_resource_update
        sub_resource_update.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
            nullable=True,
        )

        _schema.id = cls._args_sub_resource_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualNetworkGatewaysGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.VirtualNetworkGatewaysCreateOrUpdate(ctx=self.ctx)()
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
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class VirtualNetworkGatewaysGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualNetworkGatewayName", self.ctx.args.name,
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
            _UpdateHelper._build_schema_virtual_network_gateway_read(cls._schema_on_200)

            return cls._schema_on_200

    class VirtualNetworkGatewaysCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualNetworkGatewayName", self.ctx.args.name,
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
            _UpdateHelper._build_schema_virtual_network_gateway_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("bgpSettings", AAZObjectType)
                properties.set_prop("enableBgp", AAZBoolType, ".enable_bgp")
                properties.set_prop("gatewayDefaultSite", AAZObjectType)
                properties.set_prop("gatewayType", AAZStrType, ".gateway_type")
                properties.set_prop("ipConfigurations", AAZListType, ".ip_configurations")
                properties.set_prop("sku", AAZObjectType)
                properties.set_prop("vpnClientConfiguration", AAZObjectType)
                properties.set_prop("vpnType", AAZStrType, ".vpn_type")

            bgp_settings = _builder.get(".properties.bgpSettings")
            if bgp_settings is not None:
                bgp_settings.set_prop("asn", AAZIntType, ".asn")
                bgp_settings.set_prop("bgpPeeringAddress", AAZStrType, ".bgp_peering_address")
                bgp_settings.set_prop("peerWeight", AAZIntType, ".peer_weight")

            gateway_default_site = _builder.get(".properties.gatewayDefaultSite")
            if gateway_default_site is not None:
                gateway_default_site.set_prop("id", AAZStrType, ".gateway_default_site")

            ip_configurations = _builder.get(".properties.ipConfigurations")
            if ip_configurations is not None:
                ip_configurations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.ipConfigurations[]")
            if _elements is not None:
                _elements.set_prop("etag", AAZStrType, ".etag")
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties.ipConfigurations[].properties")
            if properties is not None:
                properties.set_prop("privateIPAddress", AAZStrType, ".private_ip_address")
                properties.set_prop("privateIPAllocationMethod", AAZStrType, ".private_ip_allocation_method")
                properties.set_prop("provisioningState", AAZStrType, ".provisioning_state")
                _UpdateHelper._build_schema_sub_resource_update(properties.set_prop("publicIPAddress", AAZObjectType, ".public_ip_address"))
                properties.set_prop("subnet", AAZObjectType)

            subnet = _builder.get(".properties.ipConfigurations[].properties.subnet")
            if subnet is not None:
                subnet.set_prop("id", AAZStrType, ".subnet")

            sku = _builder.get(".properties.sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".sku")
                sku.set_prop("tier", AAZStrType, ".sku_tier")

            vpn_client_configuration = _builder.get(".properties.vpnClientConfiguration")
            if vpn_client_configuration is not None:
                vpn_client_configuration.set_prop("vpnClientAddressPool", AAZObjectType)
                vpn_client_configuration.set_prop("vpnClientRootCertificates", AAZListType, ".vpn_client_root_certificates")

            vpn_client_address_pool = _builder.get(".properties.vpnClientConfiguration.vpnClientAddressPool")
            if vpn_client_address_pool is not None:
                vpn_client_address_pool.set_prop("addressPrefixes", AAZListType, ".address_prefixes")

            address_prefixes = _builder.get(".properties.vpnClientConfiguration.vpnClientAddressPool.addressPrefixes")
            if address_prefixes is not None:
                address_prefixes.set_elements(AAZStrType, ".")

            vpn_client_root_certificates = _builder.get(".properties.vpnClientConfiguration.vpnClientRootCertificates")
            if vpn_client_root_certificates is not None:
                vpn_client_root_certificates.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.vpnClientConfiguration.vpnClientRootCertificates[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties.vpnClientConfiguration.vpnClientRootCertificates[].properties")
            if properties is not None:
                properties.set_prop("publicCertData", AAZStrType, ".public_cert_data")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_sub_resource_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id

    _schema_virtual_network_gateway_read = None

    @classmethod
    def _build_schema_virtual_network_gateway_read(cls, _schema):
        if cls._schema_virtual_network_gateway_read is not None:
            _schema.etag = cls._schema_virtual_network_gateway_read.etag
            _schema.id = cls._schema_virtual_network_gateway_read.id
            _schema.location = cls._schema_virtual_network_gateway_read.location
            _schema.name = cls._schema_virtual_network_gateway_read.name
            _schema.properties = cls._schema_virtual_network_gateway_read.properties
            _schema.tags = cls._schema_virtual_network_gateway_read.tags
            _schema.type = cls._schema_virtual_network_gateway_read.type
            return

        cls._schema_virtual_network_gateway_read = _schema_virtual_network_gateway_read = AAZObjectType()

        virtual_network_gateway_read = _schema_virtual_network_gateway_read
        virtual_network_gateway_read.etag = AAZStrType()
        virtual_network_gateway_read.id = AAZStrType()
        virtual_network_gateway_read.location = AAZStrType()
        virtual_network_gateway_read.name = AAZStrType(
            flags={"read_only": True},
        )
        virtual_network_gateway_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        virtual_network_gateway_read.tags = AAZDictType()
        virtual_network_gateway_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_virtual_network_gateway_read.properties
        properties.bgp_settings = AAZObjectType(
            serialized_name="bgpSettings",
        )
        properties.enable_bgp = AAZBoolType(
            serialized_name="enableBgp",
        )
        properties.gateway_default_site = AAZObjectType(
            serialized_name="gatewayDefaultSite",
        )
        cls._build_schema_sub_resource_read(properties.gateway_default_site)
        properties.gateway_type = AAZStrType(
            serialized_name="gatewayType",
        )
        properties.ip_configurations = AAZListType(
            serialized_name="ipConfigurations",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.resource_guid = AAZStrType(
            serialized_name="resourceGuid",
        )
        properties.sku = AAZObjectType()
        properties.vpn_client_configuration = AAZObjectType(
            serialized_name="vpnClientConfiguration",
        )
        properties.vpn_type = AAZStrType(
            serialized_name="vpnType",
        )

        bgp_settings = _schema_virtual_network_gateway_read.properties.bgp_settings
        bgp_settings.asn = AAZIntType()
        bgp_settings.bgp_peering_address = AAZStrType(
            serialized_name="bgpPeeringAddress",
        )
        bgp_settings.peer_weight = AAZIntType(
            serialized_name="peerWeight",
        )

        ip_configurations = _schema_virtual_network_gateway_read.properties.ip_configurations
        ip_configurations.Element = AAZObjectType()

        _element = _schema_virtual_network_gateway_read.properties.ip_configurations.Element
        _element.etag = AAZStrType()
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_virtual_network_gateway_read.properties.ip_configurations.Element.properties
        properties.private_ip_address = AAZStrType(
            serialized_name="privateIPAddress",
        )
        properties.private_ip_allocation_method = AAZStrType(
            serialized_name="privateIPAllocationMethod",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.public_ip_address = AAZObjectType(
            serialized_name="publicIPAddress",
        )
        cls._build_schema_sub_resource_read(properties.public_ip_address)
        properties.subnet = AAZObjectType()
        cls._build_schema_sub_resource_read(properties.subnet)

        sku = _schema_virtual_network_gateway_read.properties.sku
        sku.capacity = AAZIntType()
        sku.name = AAZStrType()
        sku.tier = AAZStrType()

        vpn_client_configuration = _schema_virtual_network_gateway_read.properties.vpn_client_configuration
        vpn_client_configuration.vpn_client_address_pool = AAZObjectType(
            serialized_name="vpnClientAddressPool",
        )
        vpn_client_configuration.vpn_client_revoked_certificates = AAZListType(
            serialized_name="vpnClientRevokedCertificates",
        )
        vpn_client_configuration.vpn_client_root_certificates = AAZListType(
            serialized_name="vpnClientRootCertificates",
        )

        vpn_client_address_pool = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_address_pool
        vpn_client_address_pool.address_prefixes = AAZListType(
            serialized_name="addressPrefixes",
        )

        address_prefixes = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_address_pool.address_prefixes
        address_prefixes.Element = AAZStrType()

        vpn_client_revoked_certificates = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_revoked_certificates
        vpn_client_revoked_certificates.Element = AAZObjectType()

        _element = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element
        _element.etag = AAZStrType()
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_revoked_certificates.Element.properties
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.thumbprint = AAZStrType()

        vpn_client_root_certificates = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_root_certificates
        vpn_client_root_certificates.Element = AAZObjectType()

        _element = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_root_certificates.Element
        _element.etag = AAZStrType()
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_virtual_network_gateway_read.properties.vpn_client_configuration.vpn_client_root_certificates.Element.properties
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
        )
        properties.public_cert_data = AAZStrType(
            serialized_name="publicCertData",
        )

        tags = _schema_virtual_network_gateway_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_virtual_network_gateway_read.etag
        _schema.id = cls._schema_virtual_network_gateway_read.id
        _schema.location = cls._schema_virtual_network_gateway_read.location
        _schema.name = cls._schema_virtual_network_gateway_read.name
        _schema.properties = cls._schema_virtual_network_gateway_read.properties
        _schema.tags = cls._schema_virtual_network_gateway_read.tags
        _schema.type = cls._schema_virtual_network_gateway_read.type


__all__ = ["Update"]
