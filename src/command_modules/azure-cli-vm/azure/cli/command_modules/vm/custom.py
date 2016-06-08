﻿# pylint: disable=no-self-use,too-many-arguments
import re
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse # pylint: disable=import-error
from six.moves.urllib.request import urlopen #pylint: disable=import-error,unused-import

from azure.mgmt.compute.models import DataDisk, VirtualMachineScaleSet
from azure.mgmt.compute.models.compute_management_client_enums import DiskCreateOptionTypes
from azure.cli.commands import LongRunningOperation
from azure.cli.commands.client_factory import get_mgmt_service_client, get_data_service_client
from azure.cli._util import CLIError
from ._vm_utils import read_content_if_is_file, load_json, get_default_linux_diag_config

from ._actions import (load_images_from_aliases_doc,
                       load_extension_images_thru_services,
                       load_images_thru_services)
from ._factory import _compute_client_factory

def _vm_get(resource_group_name, vm_name, expand=None):
    '''Retrieves a VM'''
    client = _compute_client_factory()
    return client.virtual_machines.get(resource_group_name,
                                       vm_name,
                                       expand=expand)

def _vm_set(instance):
    '''Update the given Virtual Machine instance'''
    instance.resources = None # Issue: https://github.com/Azure/autorest/issues/934
    client = _compute_client_factory()
    parsed_id = _parse_rg_name(instance.id)
    poller = client.virtual_machines.create_or_update(
        resource_group_name=parsed_id[0],
        vm_name=parsed_id[1],
        parameters=instance)
    return LongRunningOperation()(poller)

def _parse_rg_name(strid):
    '''From an ID, extract the contained (resource group, name) tuple
    '''
    parts = re.split('/', strid)
    if parts[3] != 'resourceGroups':
        raise KeyError()

    return (parts[4], parts[8])

_LINUX_ACCESS_EXT = 'VMAccessForLinux'
_WINDOWS_ACCESS_EXT = 'VMAccessAgent'
_LINUX_DIAG_EXT = 'LinuxDiagnostic'
extension_mappings = {
    _LINUX_ACCESS_EXT: {
        'version': '1.4',
        'publisher': 'Microsoft.OSTCExtensions'
        },
    _WINDOWS_ACCESS_EXT: {
        'version': '2.0',
        'publisher': 'Microsoft.Compute'
        },
    _LINUX_DIAG_EXT:{
        'version': '2.3',
        'publisher': 'Microsoft.OSTCExtensions'
        }
    }

def _get_access_extension_upgrade_info(extensions, name):
    version = extension_mappings[name]['version']
    publisher = extension_mappings[name]['publisher']

    auto_upgrade = None

    if extensions:
        extension = next((e for e in extensions if e.name == name), None)
        #pylint: disable=no-name-in-module,import-error
        from distutils.version import LooseVersion
        if extension and LooseVersion(extension.type_handler_version) < LooseVersion(version):
            auto_upgrade = True
        elif extension and LooseVersion(extension.type_handler_version) > LooseVersion(version):
            version = extension.type_handler_version

    return publisher, version, auto_upgrade


def _get_storage_management_client():
    from azure.mgmt.storage import StorageManagementClient, StorageManagementClientConfiguration
    return get_mgmt_service_client(StorageManagementClient,
                                   StorageManagementClientConfiguration)

def _trim_away_build_number(version):
    #workaround a known issue: the version must only contain "major.minor", even though
    #"extension image list" gives more detail
    return '.'.join(version.split('.')[0:2])

def list_vm(resource_group_name=None):
    ''' List Virtual Machines. '''
    ccf = _compute_client_factory()
    vm_list = ccf.virtual_machines.list(resource_group_name=resource_group_name) \
        if resource_group_name else ccf.virtual_machines.list_all()
    return list(vm_list)

def list_vm_images(image_location=None, publisher=None, offer=None, sku=None, all=False): # pylint: disable=redefined-builtin
    '''vm image list
    :param str image_location:Image location
    :param str publisher:Image publisher name
    :param str offer:Image offer name
    :param str sku:Image sku name
    :param bool all:Retrieve all versions of images from all publishers
    '''
    load_thru_services = all

    if load_thru_services:
        all_images = load_images_thru_services(publisher, offer, sku, image_location)
    else:
        all_images = load_images_from_aliases_doc(publisher, offer, sku)

    for i in all_images:
        i['urn'] = ':'.join([i['publisher'], i['offer'], i['sku'], i['version']])
    return all_images

def list_vm_extension_images(
        image_location=None, publisher=None, name=None, version=None, latest=False):
    '''vm extension image list
    :param str image_location:Image location
    :param str publisher:Image publisher name
    :param str name:Image name
    :param str version:Image version
    :param bool latest: Show the latest version only.
    '''
    return load_extension_images_thru_services(
        publisher, name, version, image_location, latest)

def list_ip_addresses(resource_group_name=None, vm_name=None):
    ''' Get IP addresses from one or more Virtual Machines
    :param str resource_group_name:Name of resource group.
    :param str vm_name:Name of virtual machine.
    '''
    from azure.mgmt.network import NetworkManagementClient, NetworkManagementClientConfiguration

    # We start by getting NICs as they are the smack in the middle of all data that we
    # want to collect for a VM (as long as we don't need any info on the VM than what
    # is available in the Id, we don't need to make any calls to the compute RP)
    #
    # Since there is no guarantee that a NIC is in the same resource group as a given
    # Virtual Machine, we can't constrain the lookup to only a single group...
    network_client = get_mgmt_service_client(NetworkManagementClient,
                                             NetworkManagementClientConfiguration)
    nics = network_client.network_interfaces.list_all()
    public_ip_addresses = network_client.public_ip_addresses.list_all()

    ip_address_lookup = {pip.id: pip for pip in list(public_ip_addresses)}

    result = []
    for nic in [n for n in list(nics) if n.virtual_machine]:
        nic_resource_group, nic_vm_name = _parse_rg_name(nic.virtual_machine.id)

        # If provided, make sure that resource group name and vm name match the NIC we are
        # looking at before adding it to the result...
        if (resource_group_name in (None, nic_resource_group)
                and vm_name in (None, nic_vm_name)):

            network_info = {
                'privateIpAddresses': [],
                'publicIpAddresses': []
            }
            for ip_configuration in nic.ip_configurations:
                network_info['privateIpAddresses'].append(ip_configuration.private_ip_address)
                if ip_configuration.public_ip_address:
                    public_ip_address = ip_address_lookup[ip_configuration.public_ip_address.id]
                    network_info['publicIpAddresses'].append({
                        'id': public_ip_address.id,
                        'name': public_ip_address.name,
                        'ipAddress': public_ip_address.ip_address,
                        'ipAllocationMethod': public_ip_address.public_ip_allocation_method
                        })

            result.append({
                'virtualMachine': {
                    'resourceGroup': nic_resource_group,
                    'name': nic_vm_name,
                    'network': network_info
                    }
                })

    return result

def attach_new_disk(resource_group_name, vm_name, lun, diskname, vhd, disksize=1023):
    ''' Attach a new disk to an existing Virtual Machine'''
    vm = _vm_get(resource_group_name, vm_name)
    disk = DataDisk(lun=lun, vhd=vhd, name=diskname,
                    create_option=DiskCreateOptionTypes.empty,
                    disk_size_gb=disksize)
    vm.storage_profile.data_disks.append(disk) # pylint: disable=no-member
    _vm_set(vm)

def attach_existing_disk(resource_group_name, vm_name, lun, diskname, vhd, disksize=1023):
    ''' Attach an existing disk to an existing Virtual Machine '''
    # TODO: figure out size of existing disk instead of making the default value 1023
    vm = _vm_get(resource_group_name, vm_name)
    disk = DataDisk(lun=lun, vhd=vhd, name=diskname,
                    create_option=DiskCreateOptionTypes.attach,
                    disk_size_gb=disksize)
    vm.storage_profile.data_disks.append(disk) # pylint: disable=no-member
    _vm_set(vm)

def detach_disk(resource_group_name, vm_name, diskname):
    ''' Detach a disk from a Virtual Machine '''
    vm = _vm_get(resource_group_name, vm_name)
    # Issue: https://github.com/Azure/autorest/issues/934
    vm.resources = None
    try:
        disk = next(d for d in vm.storage_profile.data_disks if d.name == diskname) # pylint: disable=no-member
        vm.storage_profile.data_disks.remove(disk) # pylint: disable=no-member
    except StopIteration:
        raise CLIError("No disk with the name '{}' found".format(diskname))
    _vm_set(vm)

def resize_vm(resource_group_name, vm_name, size):
    '''Update vm size
    :param str size: sizes such as Standard_A4, Standard_F4s, etc
    '''
    vm = _vm_get(resource_group_name, vm_name)
    vm.hardware_profile.vm_size = size #pylint: disable=no-member
    return _vm_set(vm)

def list_disks(resource_group_name, vm_name):
    ''' List disks for a Virtual Machine '''
    vm = _vm_get(resource_group_name, vm_name)
    return vm.storage_profile.data_disks # pylint: disable=no-member

def set_windows_user_password(
        resource_group_name, vm_name, username, password):
    '''Update the password.
    You can only change the password. Adding a new user is not supported.
    '''
    vm = _vm_get(resource_group_name, vm_name, 'instanceView')

    client = _compute_client_factory()

    from azure.mgmt.compute.models import VirtualMachineExtension

    extension_name = _WINDOWS_ACCESS_EXT
    publisher, version, auto_upgrade = _get_access_extension_upgrade_info(
        vm.resources, extension_name)

    ext = VirtualMachineExtension(vm.location,#pylint: disable=no-member
                                  publisher=publisher,
                                  virtual_machine_extension_type=extension_name,
                                  protected_settings={'Password': password},
                                  type_handler_version=version,
                                  settings={'UserName': username},
                                  auto_upgrade_minor_version=auto_upgrade)

    return client.virtual_machine_extensions.create_or_update(
        resource_group_name, vm_name, extension_name, ext)

def set_linux_user(
        resource_group_name, vm_name, username, password=None, ssh_key_value=None):
    '''create or update a user credential
    :param ssh_key_value: SSH key file value or key file path
    '''
    vm = _vm_get(resource_group_name, vm_name, 'instanceView')
    client = _compute_client_factory()

    from azure.mgmt.compute.models import VirtualMachineExtension

    if password is None and ssh_key_value is None:
        raise CLIError('Please provide either password or ssh public key.')

    protected_settings = {}
    protected_settings['username'] = username
    if password:
        protected_settings['password'] = password

    if ssh_key_value:
        protected_settings['ssh_key'] = read_content_if_is_file(ssh_key_value)

    extension_name = _LINUX_ACCESS_EXT
    publisher, version, auto_upgrade = _get_access_extension_upgrade_info(
        vm.resources, extension_name)

    ext = VirtualMachineExtension(vm.location,#pylint: disable=no-member
                                  publisher=publisher,
                                  virtual_machine_extension_type=extension_name,
                                  protected_settings=protected_settings,
                                  type_handler_version=version,
                                  settings={},
                                  auto_upgrade_minor_version=auto_upgrade)

    return client.virtual_machine_extensions.create_or_update(
        resource_group_name, vm_name, extension_name, ext)

def delete_linux_user(
        resource_group_name, vm_name, username):
    '''Remove the user '''
    vm = _vm_get(resource_group_name, vm_name, 'instanceView')
    client = _compute_client_factory()

    from azure.mgmt.compute.models import VirtualMachineExtension

    extension_name = _LINUX_ACCESS_EXT
    publisher, version, auto_upgrade = _get_access_extension_upgrade_info(
        vm.resources, extension_name)

    ext = VirtualMachineExtension(vm.location,#pylint: disable=no-member
                                  publisher=publisher,
                                  virtual_machine_extension_type=extension_name,
                                  protected_settings={'remove_user':username},
                                  type_handler_version=version,
                                  settings={},
                                  auto_upgrade_minor_version=auto_upgrade)

    return client.virtual_machine_extensions.create_or_update(
        resource_group_name, vm_name, extension_name, ext)

def disable_boot_diagnostics(resource_group_name, vm_name):
    vm = _vm_get(resource_group_name, vm_name)
    diag_profile = vm.diagnostics_profile
    if not (diag_profile and
            diag_profile.boot_diagnostics and
            diag_profile.boot_diagnostics.enabled):
        return

    # Issue: https://github.com/Azure/autorest/issues/934
    vm.resources = None
    diag_profile.boot_diagnostics.enabled = False
    diag_profile.boot_diagnostics.storage_uri = None
    _vm_set(vm)

def enable_boot_diagnostics(resource_group_name, vm_name, storage):
    '''Enable boot diagnostics
    :param storage:a storage account name or a uri like
    https://your_stoage_account_name.blob.core.windows.net/
    '''
    vm = _vm_get(resource_group_name, vm_name)
    if urlparse(storage).scheme:
        storage_uri = storage
    else:
        storage_mgmt_client = _get_storage_management_client()
        storage_accounts = storage_mgmt_client.storage_accounts.list()
        storage_account = next((a for a in list(storage_accounts)
                                if a.name.lower() == storage.lower()), None)
        if storage_account is None:
            raise CLIError('{} does\'t exist.'.format(storage))
        storage_uri = storage_account.primary_endpoints.blob

    if (vm.diagnostics_profile and
            vm.diagnostics_profile.boot_diagnostics and
            vm.diagnostics_profile.boot_diagnostics.enabled and
            vm.diagnostics_profile.boot_diagnostics.storage_uri and
            vm.diagnostics_profile.boot_diagnostics.storage_uri.lower() == storage_uri.lower()):
        return

    from azure.mgmt.compute.models import DiagnosticsProfile, BootDiagnostics
    boot_diag = BootDiagnostics(True, storage_uri)
    if vm.diagnostics_profile is None:
        vm.diagnostics_profile = DiagnosticsProfile(boot_diag)
    else:
        vm.diagnostics_profile.boot_diagnostics = boot_diag

    # Issue: https://github.com/Azure/autorest/issues/934
    vm.resources = None
    _vm_set(vm)

def get_boot_log(resource_group_name, vm_name):
    import sys
    import io

    from azure.storage.blob import BlockBlobService

    client = _compute_client_factory()

    virtual_machine = client.virtual_machines.get(
        resource_group_name,
        vm_name,
        expand='instanceView')

    blob_uri = virtual_machine.instance_view.boot_diagnostics.serial_console_log_blob_uri # pylint: disable=no-member

    # Find storage account for diagnostics
    storage_mgmt_client = _get_storage_management_client()
    if not blob_uri:
        raise CLIError('No console log available')
    try:
        storage_accounts = storage_mgmt_client.storage_accounts.list()
        matching_storage_account = (a for a in list(storage_accounts)
                                    if blob_uri.startswith(a.primary_endpoints.blob))
        storage_account = next(matching_storage_account)
    except StopIteration:
        raise CLIError('Failed to find storage accont for console log file')

    regex = r'/subscriptions/[^/]+/resourceGroups/(?P<rg>[^/]+)/.+'
    match = re.search(regex, storage_account.id, re.I)
    rg = match.group('rg')
    # Get account key
    keys = storage_mgmt_client.storage_accounts.list_keys(rg, storage_account.name)

    # Extract container and blob name from url...
    container, blob = urlparse(blob_uri).path.split('/')[-2:]

    storage_client = get_data_service_client(
        BlockBlobService,
        storage_account.name,
        keys.key1) # pylint: disable=no-member

    class StreamWriter(object): # pylint: disable=too-few-public-methods

        def __init__(self, out):
            self.out = out

        def write(self, str_or_bytes):
            if isinstance(str_or_bytes, bytes):
                self.out.write(str_or_bytes.decode())
            else:
                self.out.write(str_or_bytes)

    storage_client.get_blob_to_stream(container, blob, StreamWriter(sys.stdout))

def list_extensions(resource_group_name, vm_name):
    vm = _vm_get(resource_group_name, vm_name)
    extension_type = 'Microsoft.Compute/virtualMachines/extensions'
    result = [r for r in vm.resources if r.type == extension_type]
    return result

def set_extension(
        resource_group_name, vm_name, vm_extension_name, publisher, version, public_config=None,
        private_config=None, auto_upgrade_minor_version=False):
    '''create/update extensions for a VM in a resource group. You can use
    'extension image list' to get extension details
    :param vm_name: the name of virtual machine.
    :param vm_extension_name: the name of the extension
    :param publisher: the name of extension publisher
    :param version: the version of extension.
    :param public_config: public configuration content or a file path
    :param private_config: private configuration content or a file path
    :param auto_upgrade_minor_version: auto upgrade to the newer version if available
    '''
    vm = _vm_get(resource_group_name, vm_name)
    client = _compute_client_factory()

    from azure.mgmt.compute.models import VirtualMachineExtension

    protected_settings = load_json(private_config) if not private_config else {}
    settings = load_json(public_config) if public_config else None

    version = _trim_away_build_number(version)

    ext = VirtualMachineExtension(vm.location,#pylint: disable=no-member
                                  publisher=publisher,
                                  virtual_machine_extension_type=vm_extension_name,
                                  protected_settings=protected_settings,
                                  type_handler_version=version,
                                  settings=settings,
                                  auto_upgrade_minor_version=auto_upgrade_minor_version)
    return client.virtual_machine_extensions.create_or_update(
        resource_group_name, vm_name, vm_extension_name, ext)

def set_diagnostics_extension(
        resource_group_name, vm_name, storage_account, public_config=None):
    '''Enable diagnostics

    :param vm_name: the name of virtual machine
    :param storage_account: the storage account to upload diagnostics log
    :param public_config: the config file which defines data to be collected.
    Default will be provided if missing
    '''
    vm = _vm_get(resource_group_name, vm_name, 'instanceView')
    client = _compute_client_factory()

    from azure.mgmt.compute.models import VirtualMachineExtension
    #pylint: disable=no-member
    if public_config:
        public_config = load_json(public_config)
    else:
        public_config = get_default_linux_diag_config(vm.id)

    storage_mgmt_client = _get_storage_management_client()
    keys = storage_mgmt_client.storage_accounts.list_keys(resource_group_name, storage_account)

    private_config = {
        'storageAccountName': storage_account,
        'storageAccountKey': keys.key1
        }

    vm_extension_name = _LINUX_DIAG_EXT
    publisher, version, auto_upgrade = _get_access_extension_upgrade_info(
        vm.resources, vm_extension_name
    )

    ext = VirtualMachineExtension(vm.location,
                                  publisher=publisher,
                                  virtual_machine_extension_type=vm_extension_name,
                                  protected_settings=private_config,
                                  type_handler_version=version,
                                  settings=public_config,
                                  auto_upgrade_minor_version=auto_upgrade)

    return client.virtual_machine_extensions.create_or_update(resource_group_name,
                                                              vm_name,
                                                              vm_extension_name,
                                                              ext)

def show_default_diagnostics_configuration():
    '''show the default config file which defines data to be collected'''
    return get_default_linux_diag_config()


def vmss_scale(resource_group_name, vm_scale_set_name, new_capacity):
    '''change the number of VMs in an virtual machine scale set

    :param int new_capacity: number of virtual machines in a scale set
    '''
    client = _compute_client_factory()
    vmss = client.virtual_machine_scale_sets.get(resource_group_name, vm_scale_set_name)
    #pylint: disable=no-member
    if vmss.sku.capacity == new_capacity:
        return
    else:
        vmss.sku.capacity = new_capacity
    vmss_new = VirtualMachineScaleSet(vmss.location, sku=vmss.sku)
    return client.virtual_machine_scale_sets.create_or_update(resource_group_name,
                                                              vm_scale_set_name,
                                                              vmss_new)

def vmss_update_instances(resource_group_name, vm_scale_set_name, instance_ids):
    '''upgrade virtual machines in a virtual machine scale set

    :param str instance_ids: space separated ids, such as 0 2 3.
    '''
    client = _compute_client_factory()
    return client.virtual_machine_scale_sets.update_instances(resource_group_name,
                                                              vm_scale_set_name,
                                                              instance_ids)

def vmss_get_instance_view(resource_group_name, vm_scale_set_name, instance_id=None):
    '''get instance view.

    :param str instance_id: instance id
    '''
    client = _compute_client_factory()
    if instance_id:
        return client.virtual_machine_scale_set_vms.get_instance_view(resource_group_name,
                                                                      vm_scale_set_name,
                                                                      instance_id)
    else:
        return client.virtual_machine_scale_sets.get_instance_view(resource_group_name,
                                                                   vm_scale_set_name)

def vmss_deallocate(resource_group_name, vm_scale_set_name, instance_ids=None):
    '''deallocate virtual machines in a virtual machine scale set.

    :param str instance_ids: space separated ids, such as 0 2 3
    '''
    client = _compute_client_factory()
    if  instance_ids and len(instance_ids) == 1:
        return client.virtual_machine_scale_set_vms.deallocate(resource_group_name,
                                                               vm_scale_set_name,
                                                               instance_ids[0])
    else:
        return client.virtual_machine_scale_sets.deallocate(resource_group_name,
                                                            vm_scale_set_name,
                                                            instance_ids)

def vmss_delete_instances(resource_group_name, vm_scale_set_name, instance_ids):
    '''delete virtual machines in a virtual machine scale set.

    :param str instance_ids: space separated ids, such as 0 2 3
    '''
    client = _compute_client_factory()
    if len(instance_ids) == 1:
        return client.virtual_machine_scale_set_vms.delete(resource_group_name,
                                                           vm_scale_set_name,
                                                           instance_ids[0])
    else:
        return client.virtual_machine_scale_sets.delete_instances(resource_group_name,
                                                                  vm_scale_set_name,
                                                                  instance_ids)

def vmss_power_off(resource_group_name, vm_scale_set_name, instance_ids=None):
    '''power off (stop) virtual machines in a virtual machine scale set.

    :param str instance_ids: space separated ids, such as 0 2 3
    '''
    client = _compute_client_factory()
    if instance_ids and len(instance_ids) == 1:
        return client.virtual_machine_scale_set_vms.power_off(resource_group_name,
                                                              vm_scale_set_name,
                                                              instance_ids[0])
    else:
        return client.virtual_machine_scale_sets.power_off(resource_group_name,
                                                           vm_scale_set_name,
                                                           instance_ids)

def vmss_reimage(resource_group_name, vm_scale_set_name, instance_id=None):
    '''reimage virtual machines in a virtual machine scale set.

    :param str instance_id: instance id
    '''
    client = _compute_client_factory()
    if instance_id:
        return client.virtual_machine_scale_set_vms.reimage(resource_group_name,
                                                            vm_scale_set_name,
                                                            instance_id)
    else:
        return client.virtual_machine_scale_sets.reimage(resource_group_name,
                                                         vm_scale_set_name)

def vmss_restart(resource_group_name, vm_scale_set_name, instance_ids=None):
    '''restart virtual machines in a virtual machine scale set.

    :param str instance_ids: space separated ids, such as 0 2 3
    '''
    client = _compute_client_factory()
    if instance_ids and len(instance_ids) == 1:
        return client.virtual_machine_scale_set_vms.restart(resource_group_name,
                                                            vm_scale_set_name,
                                                            instance_ids[0])
    else:
        return client.virtual_machine_scale_sets.restart(resource_group_name,
                                                         vm_scale_set_name,
                                                         instance_ids)

def vmss_start(resource_group_name, vm_scale_set_name, instance_ids=None):
    '''start virtual machines in a virtual machine scale set.

    :param str instance_ids: space separated ids, such as 0 2 3
    '''
    client = _compute_client_factory()
    if instance_ids and len(instance_ids) == 1:
        return client.virtual_machine_scale_set_vms.start(resource_group_name,
                                                          vm_scale_set_name,
                                                          instance_ids[0])
    else:
        return client.virtual_machine_scale_sets.start(resource_group_name,
                                                       vm_scale_set_name,
                                                       instance_ids)

