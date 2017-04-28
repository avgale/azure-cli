# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from .week_details import WeekDetails
from .day_details import DayDetails
from .hour_details import HourDetails
from .notification_settings import NotificationSettings
from .schedule import Schedule
from .applicable_schedule import ApplicableSchedule
from .week_details_fragment import WeekDetailsFragment
from .day_details_fragment import DayDetailsFragment
from .hour_details_fragment import HourDetailsFragment
from .notification_settings_fragment import NotificationSettingsFragment
from .schedule_fragment import ScheduleFragment
from .applicable_schedule_fragment import ApplicableScheduleFragment
from .artifact_parameter_properties import ArtifactParameterProperties
from .artifact_install_properties import ArtifactInstallProperties
from .apply_artifacts_request import ApplyArtifactsRequest
from .parameters_value_file_info import ParametersValueFileInfo
from .arm_template import ArmTemplate
from .arm_template_info import ArmTemplateInfo
from .arm_template_parameter_properties import ArmTemplateParameterProperties
from .artifact import Artifact
from .artifact_deployment_status_properties import ArtifactDeploymentStatusProperties
from .artifact_deployment_status_properties_fragment import ArtifactDeploymentStatusPropertiesFragment
from .artifact_parameter_properties_fragment import ArtifactParameterPropertiesFragment
from .artifact_install_properties_fragment import ArtifactInstallPropertiesFragment
from .artifact_source import ArtifactSource
from .artifact_source_fragment import ArtifactSourceFragment
from .attach_disk_properties import AttachDiskProperties
from .attach_new_data_disk_options import AttachNewDataDiskOptions
from .bulk_creation_parameters import BulkCreationParameters
from .compute_data_disk import ComputeDataDisk
from .compute_data_disk_fragment import ComputeDataDiskFragment
from .compute_vm_instance_view_status import ComputeVmInstanceViewStatus
from .compute_vm_instance_view_status_fragment import ComputeVmInstanceViewStatusFragment
from .compute_vm_properties import ComputeVmProperties
from .compute_vm_properties_fragment import ComputeVmPropertiesFragment
from .percentage_cost_threshold_properties import PercentageCostThresholdProperties
from .cost_threshold_properties import CostThresholdProperties
from .windows_os_info import WindowsOsInfo
from .linux_os_info import LinuxOsInfo
from .custom_image_properties_from_vm import CustomImagePropertiesFromVm
from .custom_image_properties_custom import CustomImagePropertiesCustom
from .custom_image import CustomImage
from .data_disk_properties import DataDiskProperties
from .detach_data_disk_properties import DetachDataDiskProperties
from .detach_disk_properties import DetachDiskProperties
from .disk import Disk
from .environment_deployment_properties import EnvironmentDeploymentProperties
from .dtl_environment import DtlEnvironment
from .evaluate_policies_properties import EvaluatePoliciesProperties
from .evaluate_policies_request import EvaluatePoliciesRequest
from .policy_violation import PolicyViolation
from .policy_set_result import PolicySetResult
from .evaluate_policies_response import EvaluatePoliciesResponse
from .event import Event
from .event_fragment import EventFragment
from .export_resource_usage_parameters import ExportResourceUsageParameters
from .external_subnet import ExternalSubnet
from .external_subnet_fragment import ExternalSubnetFragment
from .gallery_image_reference import GalleryImageReference
from .inbound_nat_rule import InboundNatRule
from .shared_public_ip_address_configuration import SharedPublicIpAddressConfiguration
from .network_interface_properties import NetworkInterfaceProperties
from .lab_virtual_machine_creation_parameter import LabVirtualMachineCreationParameter
from .formula_properties_from_vm import FormulaPropertiesFromVm
from .formula import Formula
from .gallery_image import GalleryImage
from .gallery_image_reference_fragment import GalleryImageReferenceFragment
from .parameter_info import ParameterInfo
from .generate_arm_template_request import GenerateArmTemplateRequest
from .generate_upload_uri_parameter import GenerateUploadUriParameter
from .generate_upload_uri_response import GenerateUploadUriResponse
from .identity_properties import IdentityProperties
from .inbound_nat_rule_fragment import InboundNatRuleFragment
from .lab import Lab
from .target_cost_properties import TargetCostProperties
from .lab_cost_summary_properties import LabCostSummaryProperties
from .lab_cost_details_properties import LabCostDetailsProperties
from .lab_resource_cost_properties import LabResourceCostProperties
from .lab_cost import LabCost
from .lab_fragment import LabFragment
from .lab_vhd import LabVhd
from .lab_virtual_machine import LabVirtualMachine
from .shared_public_ip_address_configuration_fragment import SharedPublicIpAddressConfigurationFragment
from .network_interface_properties_fragment import NetworkInterfacePropertiesFragment
from .lab_virtual_machine_fragment import LabVirtualMachineFragment
from .notification_channel import NotificationChannel
from .notification_channel_fragment import NotificationChannelFragment
from .notify_parameters import NotifyParameters
from .policy import Policy
from .policy_fragment import PolicyFragment
from .port import Port
from .port_fragment import PortFragment
from .resource import Resource
from .secret import Secret
from .service_runner import ServiceRunner
from .user_identity import UserIdentity
from .user_secret_store import UserSecretStore
from .user import User
from .subnet import Subnet
from .subnet_shared_public_ip_address_configuration import SubnetSharedPublicIpAddressConfiguration
from .subnet_override import SubnetOverride
from .virtual_network import VirtualNetwork
from .retarget_schedule_properties import RetargetScheduleProperties
from .shutdown_notification_content import ShutdownNotificationContent
from .subnet_fragment import SubnetFragment
from .subnet_shared_public_ip_address_configuration_fragment import SubnetSharedPublicIpAddressConfigurationFragment
from .subnet_override_fragment import SubnetOverrideFragment
from .user_identity_fragment import UserIdentityFragment
from .user_secret_store_fragment import UserSecretStoreFragment
from .user_fragment import UserFragment
from .virtual_network_fragment import VirtualNetworkFragment
from .lab_paged import LabPaged
from .lab_vhd_paged import LabVhdPaged
from .schedule_paged import SchedulePaged
from .artifact_source_paged import ArtifactSourcePaged
from .arm_template_paged import ArmTemplatePaged
from .artifact_paged import ArtifactPaged
from .custom_image_paged import CustomImagePaged
from .formula_paged import FormulaPaged
from .gallery_image_paged import GalleryImagePaged
from .notification_channel_paged import NotificationChannelPaged
from .policy_paged import PolicyPaged
from .service_runner_paged import ServiceRunnerPaged
from .user_paged import UserPaged
from .disk_paged import DiskPaged
from .dtl_environment_paged import DtlEnvironmentPaged
from .secret_paged import SecretPaged
from .lab_virtual_machine_paged import LabVirtualMachinePaged
from .virtual_network_paged import VirtualNetworkPaged
from .dev_test_labs_client_enums import (
    EnableStatus,
    NotificationStatus,
    SourceControlType,
    StorageType,
    CostThresholdStatus,
    WindowsOsState,
    LinuxOsState,
    CustomImageOsType,
    HostCachingOptions,
    NotificationChannelEventType,
    TransportProtocol,
    VirtualMachineCreationSource,
    FileUploadOptions,
    PremiumDataDisk,
    TargetCostStatus,
    ReportingCycleType,
    CostType,
    PolicyStatus,
    PolicyFactName,
    PolicyEvaluatorType,
    UsagePermissionType,
)

__all__ = [
    'WeekDetails',
    'DayDetails',
    'HourDetails',
    'NotificationSettings',
    'Schedule',
    'ApplicableSchedule',
    'WeekDetailsFragment',
    'DayDetailsFragment',
    'HourDetailsFragment',
    'NotificationSettingsFragment',
    'ScheduleFragment',
    'ApplicableScheduleFragment',
    'ArtifactParameterProperties',
    'ArtifactInstallProperties',
    'ApplyArtifactsRequest',
    'ParametersValueFileInfo',
    'ArmTemplate',
    'ArmTemplateInfo',
    'ArmTemplateParameterProperties',
    'Artifact',
    'ArtifactDeploymentStatusProperties',
    'ArtifactDeploymentStatusPropertiesFragment',
    'ArtifactParameterPropertiesFragment',
    'ArtifactInstallPropertiesFragment',
    'ArtifactSource',
    'ArtifactSourceFragment',
    'AttachDiskProperties',
    'AttachNewDataDiskOptions',
    'BulkCreationParameters',
    'ComputeDataDisk',
    'ComputeDataDiskFragment',
    'ComputeVmInstanceViewStatus',
    'ComputeVmInstanceViewStatusFragment',
    'ComputeVmProperties',
    'ComputeVmPropertiesFragment',
    'PercentageCostThresholdProperties',
    'CostThresholdProperties',
    'WindowsOsInfo',
    'LinuxOsInfo',
    'CustomImagePropertiesFromVm',
    'CustomImagePropertiesCustom',
    'CustomImage',
    'DataDiskProperties',
    'DetachDataDiskProperties',
    'DetachDiskProperties',
    'Disk',
    'EnvironmentDeploymentProperties',
    'DtlEnvironment',
    'EvaluatePoliciesProperties',
    'EvaluatePoliciesRequest',
    'PolicyViolation',
    'PolicySetResult',
    'EvaluatePoliciesResponse',
    'Event',
    'EventFragment',
    'ExportResourceUsageParameters',
    'ExternalSubnet',
    'ExternalSubnetFragment',
    'GalleryImageReference',
    'InboundNatRule',
    'SharedPublicIpAddressConfiguration',
    'NetworkInterfaceProperties',
    'LabVirtualMachineCreationParameter',
    'FormulaPropertiesFromVm',
    'Formula',
    'GalleryImage',
    'GalleryImageReferenceFragment',
    'ParameterInfo',
    'GenerateArmTemplateRequest',
    'GenerateUploadUriParameter',
    'GenerateUploadUriResponse',
    'IdentityProperties',
    'InboundNatRuleFragment',
    'Lab',
    'TargetCostProperties',
    'LabCostSummaryProperties',
    'LabCostDetailsProperties',
    'LabResourceCostProperties',
    'LabCost',
    'LabFragment',
    'LabVhd',
    'LabVirtualMachine',
    'SharedPublicIpAddressConfigurationFragment',
    'NetworkInterfacePropertiesFragment',
    'LabVirtualMachineFragment',
    'NotificationChannel',
    'NotificationChannelFragment',
    'NotifyParameters',
    'Policy',
    'PolicyFragment',
    'Port',
    'PortFragment',
    'Resource',
    'Secret',
    'ServiceRunner',
    'UserIdentity',
    'UserSecretStore',
    'User',
    'Subnet',
    'SubnetSharedPublicIpAddressConfiguration',
    'SubnetOverride',
    'VirtualNetwork',
    'RetargetScheduleProperties',
    'ShutdownNotificationContent',
    'SubnetFragment',
    'SubnetSharedPublicIpAddressConfigurationFragment',
    'SubnetOverrideFragment',
    'UserIdentityFragment',
    'UserSecretStoreFragment',
    'UserFragment',
    'VirtualNetworkFragment',
    'LabPaged',
    'LabVhdPaged',
    'SchedulePaged',
    'ArtifactSourcePaged',
    'ArmTemplatePaged',
    'ArtifactPaged',
    'CustomImagePaged',
    'FormulaPaged',
    'GalleryImagePaged',
    'NotificationChannelPaged',
    'PolicyPaged',
    'ServiceRunnerPaged',
    'UserPaged',
    'DiskPaged',
    'DtlEnvironmentPaged',
    'SecretPaged',
    'LabVirtualMachinePaged',
    'VirtualNetworkPaged',
    'EnableStatus',
    'NotificationStatus',
    'SourceControlType',
    'StorageType',
    'CostThresholdStatus',
    'WindowsOsState',
    'LinuxOsState',
    'CustomImageOsType',
    'HostCachingOptions',
    'NotificationChannelEventType',
    'TransportProtocol',
    'VirtualMachineCreationSource',
    'FileUploadOptions',
    'PremiumDataDisk',
    'TargetCostStatus',
    'ReportingCycleType',
    'CostType',
    'PolicyStatus',
    'PolicyFactName',
    'PolicyEvaluatorType',
    'UsagePermissionType',
]
