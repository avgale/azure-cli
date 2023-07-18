# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Create(AAZCommand):
    """Create a DNS zone. Does not modify DNS records within the zone.
    """

    _aaz_info = {
        "version": "2018-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/dnszones/{}", "2018-05-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.if_match = AAZStrArg(
            options=["--if-match"],
            help="The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.",
        )
        _args_schema.if_none_match = AAZStrArg(
            options=["--if-none-match"],
            help="Set to '*' to allow a new DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored.",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.zone_name = AAZStrArg(
            options=["-n", "--name", "--zone-name"],
            help="The name of the DNS zone (without a terminating dot).",
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.etag = AAZStrArg(
            options=["--etag"],
            arg_group="Parameters",
            help="The etag of the zone.",
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Parameters",
            help="Resource location.",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.registration_vnets = AAZListArg(
            options=["--registration-vnets"],
            arg_group="Properties",
            help="A list of references to virtual networks that register hostnames in this DNS zone. This is a only when ZoneType is Private.",
        )
        _args_schema.resolution_vnets = AAZListArg(
            options=["--resolution-vnets"],
            arg_group="Properties",
            help="A list of references to virtual networks that resolve records in this DNS zone. This is a only when ZoneType is Private.",
        )
        _args_schema.zone_type = AAZStrArg(
            options=["--zone-type"],
            arg_group="Properties",
            help="The type of this DNS zone (Public or Private).",
            default="Public",
            enum={"Private": "Private", "Public": "Public"},
        )

        registration_vnets = cls._args_schema.registration_vnets
        registration_vnets.Element = AAZObjectArg()
        cls._build_args_sub_resource_create(registration_vnets.Element)

        resolution_vnets = cls._args_schema.resolution_vnets
        resolution_vnets.Element = AAZObjectArg()
        cls._build_args_sub_resource_create(resolution_vnets.Element)
        return cls._args_schema

    _args_sub_resource_create = None

    @classmethod
    def _build_args_sub_resource_create(cls, _schema):
        if cls._args_sub_resource_create is not None:
            _schema.id = cls._args_sub_resource_create.id
            return

        cls._args_sub_resource_create = AAZObjectArg()

        sub_resource_create = cls._args_sub_resource_create
        sub_resource_create.id = AAZStrArg(
            options=["id"],
            help="Resource Id.",
        )

        _schema.id = cls._args_sub_resource_create.id

    def _execute_operations(self):
        self.pre_operations()
        self.ZonesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ZonesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}",
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
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "zoneName", self.ctx.args.zone_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "If-Match", self.ctx.args.if_match,
                ),
                **self.serialize_header_param(
                    "If-None-Match", self.ctx.args.if_none_match,
                ),
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
            _builder.set_prop("etag", AAZStrType, ".etag")
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("registrationVirtualNetworks", AAZListType, ".registration_vnets")
                properties.set_prop("resolutionVirtualNetworks", AAZListType, ".resolution_vnets")
                properties.set_prop("zoneType", AAZStrType, ".zone_type")

            registration_virtual_networks = _builder.get(".properties.registrationVirtualNetworks")
            if registration_virtual_networks is not None:
                _CreateHelper._build_schema_sub_resource_create(registration_virtual_networks.set_elements(AAZObjectType, "."))

            resolution_virtual_networks = _builder.get(".properties.resolutionVirtualNetworks")
            if resolution_virtual_networks is not None:
                _CreateHelper._build_schema_sub_resource_create(resolution_virtual_networks.set_elements(AAZObjectType, "."))

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
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.max_number_of_record_sets = AAZIntType(
                serialized_name="maxNumberOfRecordSets",
                flags={"read_only": True},
            )
            properties.max_number_of_records_per_record_set = AAZIntType(
                serialized_name="maxNumberOfRecordsPerRecordSet",
                flags={"read_only": True},
            )
            properties.name_servers = AAZListType(
                serialized_name="nameServers",
                flags={"read_only": True},
            )
            properties.number_of_record_sets = AAZIntType(
                serialized_name="numberOfRecordSets",
                flags={"read_only": True},
            )
            properties.registration_virtual_networks = AAZListType(
                serialized_name="registrationVirtualNetworks",
            )
            properties.resolution_virtual_networks = AAZListType(
                serialized_name="resolutionVirtualNetworks",
            )
            properties.signing_keys = AAZListType(
                serialized_name="signingKeys",
                flags={"read_only": True},
            )
            properties.zone_type = AAZStrType(
                serialized_name="zoneType",
            )

            name_servers = cls._schema_on_200_201.properties.name_servers
            name_servers.Element = AAZStrType()

            registration_virtual_networks = cls._schema_on_200_201.properties.registration_virtual_networks
            registration_virtual_networks.Element = AAZObjectType()
            _CreateHelper._build_schema_sub_resource_read(registration_virtual_networks.Element)

            resolution_virtual_networks = cls._schema_on_200_201.properties.resolution_virtual_networks
            resolution_virtual_networks.Element = AAZObjectType()
            _CreateHelper._build_schema_sub_resource_read(resolution_virtual_networks.Element)

            signing_keys = cls._schema_on_200_201.properties.signing_keys
            signing_keys.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.signing_keys.Element
            _element.delegation_signer_info = AAZListType(
                serialized_name="delegationSignerInfo",
                flags={"read_only": True},
            )
            _element.flags = AAZIntType(
                flags={"read_only": True},
            )
            _element.key_tag = AAZIntType(
                serialized_name="keyTag",
                flags={"read_only": True},
            )
            _element.protocol = AAZIntType(
                flags={"read_only": True},
            )
            _element.public_key = AAZStrType(
                serialized_name="publicKey",
                flags={"read_only": True},
            )
            _element.security_algorithm_type = AAZIntType(
                serialized_name="securityAlgorithmType",
            )

            delegation_signer_info = cls._schema_on_200_201.properties.signing_keys.Element.delegation_signer_info
            delegation_signer_info.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.signing_keys.Element.delegation_signer_info.Element
            _element.digest_algorithm_type = AAZIntType(
                serialized_name="digestAlgorithmType",
            )
            _element.digest_value = AAZStrType(
                serialized_name="digestValue",
                flags={"read_only": True},
            )
            _element.record = AAZStrType(
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_sub_resource_create(cls, _builder):
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


__all__ = ["Create"]
