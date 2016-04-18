from os import environ

from azure.cli.commands import COMMON_PARAMETERS as GLOBAL_COMMON_PARAMETERS
from azure.cli._locale import L

from ._validators import (
    validate_container_permission, validate_datetime, validate_datetime_as_string, validate_id,
    validate_ip_range, validate_key_value_pairs, validate_resource_types, validate_services,
    validate_tags, validate_lease_duration)

# HELPER METHODS

def extend_parameter(parameter_metadata, **kwargs):
    modified_parameter_metadata = parameter_metadata.copy()
    modified_parameter_metadata.update(kwargs)
    return modified_parameter_metadata

def get_account_name(string):
    return string if string != 'query' else environ.get('AZURE_STORAGE_ACCOUNT')

def get_account_key(string):
    return string if string != 'query' else environ.get('AZURE_STORAGE_KEY')

def get_connection_string(string):
    return string if string != 'query' else environ.get('AZURE_STORAGE_CONNECTION_STRING')

def get_sas_token(string):
    return string if string != 'query' else environ.get('AZURE_SAS_TOKEN')

# BASIC PARAMETER CONFIGURATION

PARAMETER_ALIASES = GLOBAL_COMMON_PARAMETERS.copy()
PARAMETER_ALIASES.update({
    'account_key': {
        'name': '--account-key -k',
        'help': L('the storage account key'),
        # While account key *may* actually be required if the environment variable hasn't been
        # specified, it is only required unless the connection string has been specified
        'required': False,
        'type': get_account_key,
        'default': 'query'
    },
    'account_name': {
        'name': '--account-name -n',
        'help': L('the storage account name'),
        # While account name *may* actually be required if the environment variable hasn't been
        # specified, it is only required unless the connection string has been specified
        'required': False,
        'type': get_account_name,
        'default': 'query'
    },
    'account_name_required': {
        # this is used only to obtain the connection string. Thus, the env variable default
        # does not apply and this is a required parameter
        'name': '--account-name -n',
        'help': L('the storage account name'),
        'required': True
    },
    'blob_name': {
        'name': '--blob-name -b',
        'help': L('the name of the blob'),
        'required': True
    },
    'container_name': {
        'name': '--container-name -c',
        'required': True
    },
    'connection_string': {
        'name': '--connection-string',
        'help': L('the storage connection string'),
        # You can either specify connection string or name/key. There is no convenient way
        # to express this kind of relationship in argparse...
        # TODO: Move to exclusive group
        'type': get_connection_string,
        'required': False,
        'default': 'query'
    },
    'expiry': {
        'name': '--expiry',
        'help': L('expiration UTC datetime of SAS token (Y-m-d\'T\'H:M\'Z\')'),
        'type': validate_datetime_as_string
    },
    'if_modified_since': {
        'name': '--if-modified-since',
        'help': L('alter only if modified since supplied UTC datetime (Y-m-d\'T\'H:M\'Z\')'),
        'type': validate_datetime,
        'required': False,
    },
    'id': {
        'name': '--id',
        'help': L('stored access policy id (up to 64 characters)'),
        'type': validate_id
    },
    'if_unmodified_since': {
        'name': '--if-unmodified-since',
        'help': L('alter only if unmodified since supplied UTC datetime (Y-m-d\'T\'H:M\'Z\')'),
        'type': validate_datetime,
        'required': False,
    },
    'ip': {
        'name': '--ip',
        'help': L('specifies the IP address or range of IP addresses from which to accept ' + \
                  'requests.'),
        'type': validate_ip_range
    },
    'lease_break_period': {
        'name': '--lease-break-period',
        'metavar': 'DURATION',
        'help': L('break period. 15-60 seconds or -1 for infinite.'),
        'type': validate_lease_duration
    },
    'lease_duration': {
        'name': '--lease-duration',
        'metavar': 'DURATION',
        'help': L('lease duration. 15-60 seconds or -1 for infinite.'),
        'type': validate_lease_duration
    },
    'lease_id': {
        'name': '--lease-id',
        'metavar': 'ID',
        'help': L('lease ID in GUID format.')
    },
    'metadata': {
        'name': '--metadata',
        'metavar': 'METADATA',
        'type': validate_key_value_pairs,
        'help': L('metadata in "a=b;c=d" format')
    },
    'optional_resource_group_name':
        extend_parameter(GLOBAL_COMMON_PARAMETERS['resource_group_name'], required=False),
    'permission': {
        'name': '--permission',
        'help': L('permissions granted: (r)ead (w)rite (d)elete (l)ist. Can be combined.'),
        'metavar': 'PERMISSION',
        # TODO: This will be problematic because the other sas types take different permissions
        'type': validate_container_permission
    },
    'public_access': {
        'name': '--public-access',
        'metavar': 'SPECIFIERS',
        'choices': ['blob', 'container']
    },
    'resource_types': {
        'name': '--resource-types',
        'help': L('the resource types the SAS is applicable for. Allowed values: (s)ervice ' + \
                  '(c)ontainer (o)bject. Can be combined.'),
        'type': validate_resource_types
    },
    'sas_token': {
        'name': '--sas-token',
        'help': L('a shared access signature token'),
        'type': get_sas_token,
        'default': 'query'
    },
    'services': {
        'name': '--services',
        'help': L('the storage services the SAS is applicable for. Allowed values: (b)lob ' + \
                  '(f)ile (q)ueue (t)able. Can be combined.'),
        'type': validate_services
    },
    'share_name': {
        'name': '--share-name',
        'help': L('the name of the file share'),
        'required': True,
    },
    'signed_identifiers': {
        'name': '--signed-identifiers',
        'help': L(''),
        'metavar': 'IDENTIFIERS'
    },
    'start': {
        'name': '--start',
        'help': L('start UTC datetime of SAS token (Y-m-d\'T\'H:M\'Z\'). Defaults to time ' + \
                  'of request.'),
        'type': validate_datetime_as_string
    },
    'tags' : {
        'name': '--tags',
        'metavar': 'TAGS',
        'help': L('individual and/or key/value pair tags in "a=b;c" format'),
        'required': False,
        'type': validate_tags
    },
    'timeout': {
        'name': '--timeout',
        'help': L('timeout in seconds'),
        'required': False,
        'type': int
    }
})

# SUPPLEMENTAL (EXTRA) PARAMETER SETS

STORAGE_DATA_CLIENT_ARGS = {
    'account_name': PARAMETER_ALIASES['account_name'],
    'account_key': PARAMETER_ALIASES['account_key'],
    'connection_string': PARAMETER_ALIASES['connection_string'],
    'sas_token': PARAMETER_ALIASES['sas_token']
}
