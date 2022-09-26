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
    "monitor log-analytics workspace data-export create",
)
class Create(AAZCommand):
    """Create a data export rule for a given workspace.

    For more information, see
    https://docs.microsoft.com/azure/azure-monitor/platform/logs-data-export

    :example: Create a data export rule for a given workspace.
        az monitor log-analytics workspace data-export create -g MyRG --workspace-name MyWS -n MyDataExport --destination <storage account id> --enable -t <table name>
    """

    _aaz_info = {
        "version": "2020-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/workspaces/{}/dataexports/{}", "2020-08-01"],
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
        _args_schema.data_export_name = AAZStrArg(
            options=["-n", "--name", "--data-export-name"],
            help="The data export rule name.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z][A-Za-z0-9-]+[A-Za-z0-9]$",
                max_length=63,
                min_length=4,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["--workspace-name"],
            help="The name of the workspace.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$",
                max_length=63,
                min_length=4,
            ),
        )

        # define Arg Group "Destination"

        _args_schema = cls._args_schema
        _args_schema.event_hub_name = AAZStrArg(
            options=["--event-hub-name"],
            arg_group="Destination",
            help="Optional. Allows to define an Event Hub name. Not applicable when destination is Storage Account.",
        )
        _args_schema.destination = AAZStrArg(
            options=["--destination"],
            arg_group="Destination",
            help="The destination resource ID. It should be a storage account, an event hub namespace. If event hub namespace is provided without --event-hub-name, event hub would be created for each table automatically.",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.enable = AAZBoolArg(
            options=["--enable"],
            arg_group="Properties",
            help="Active when enabled.",
        )
        _args_schema.tables = AAZListArg(
            options=["-t", "--tables"],
            arg_group="Properties",
            help="An array of tables to export.",
            required=True,
        )

        tables = cls._args_schema.tables
        tables.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DataExportsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    # @register_callback
    def pre_operations(self):
        pass

    # @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DataExportsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataExports/{dataExportName}",
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
                    "dataExportName", self.ctx.args.data_export_name,
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
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2020-08-01",
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
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("destination", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("enable", AAZBoolType, ".enable")
                properties.set_prop("tableNames", AAZListType, ".tables", typ_kwargs={"flags": {"required": True}})

            destination = _builder.get(".properties.destination")
            if destination is not None:
                destination.set_prop("metaData", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
                destination.set_prop("resourceId", AAZStrType, ".destination", typ_kwargs={"flags": {"required": True}})

            meta_data = _builder.get(".properties.destination.metaData")
            if meta_data is not None:
                meta_data.set_prop("eventHubName", AAZStrType, ".event_hub_name")

            table_names = _builder.get(".properties.tableNames")
            if table_names is not None:
                table_names.set_elements(AAZStrType, ".")

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
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.created_date = AAZStrType(
                serialized_name="createdDate",
            )
            properties.data_export_id = AAZStrType(
                serialized_name="dataExportId",
            )
            properties.destination = AAZObjectType(
                flags={"required": True},
            )
            properties.enable = AAZBoolType()
            properties.last_modified_date = AAZStrType(
                serialized_name="lastModifiedDate",
            )
            properties.table_names = AAZListType(
                serialized_name="tableNames",
                flags={"required": True},
            )

            destination = cls._schema_on_200_201.properties.destination
            destination.meta_data = AAZObjectType(
                serialized_name="metaData",
                flags={"client_flatten": True},
            )
            destination.resource_id = AAZStrType(
                serialized_name="resourceId",
                flags={"required": True},
            )
            destination.type = AAZStrType(
                flags={"read_only": True},
            )

            meta_data = cls._schema_on_200_201.properties.destination.meta_data
            meta_data.event_hub_name = AAZStrType(
                serialized_name="eventHubName",
            )

            table_names = cls._schema_on_200_201.properties.table_names
            table_names.Element = AAZStrType()

            return cls._schema_on_200_201


__all__ = ["Create"]
