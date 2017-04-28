# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from enum import Enum


class EnableStatus(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class NotificationStatus(Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class SourceControlType(Enum):

    vso_git = "VsoGit"
    git_hub = "GitHub"


class StorageType(Enum):

    standard = "Standard"
    premium = "Premium"


class CostThresholdStatus(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class WindowsOsState(Enum):

    non_sysprepped = "NonSysprepped"
    sysprep_requested = "SysprepRequested"
    sysprep_applied = "SysprepApplied"


class LinuxOsState(Enum):

    non_deprovisioned = "NonDeprovisioned"
    deprovision_requested = "DeprovisionRequested"
    deprovision_applied = "DeprovisionApplied"


class CustomImageOsType(Enum):

    windows = "Windows"
    linux = "Linux"
    none = "None"


class HostCachingOptions(Enum):

    none = "None"
    read_only = "ReadOnly"
    read_write = "ReadWrite"


class NotificationChannelEventType(Enum):

    auto_shutdown = "AutoShutdown"
    cost = "Cost"


class TransportProtocol(Enum):

    tcp = "Tcp"
    udp = "Udp"


class VirtualMachineCreationSource(Enum):

    from_custom_image = "FromCustomImage"
    from_gallery_image = "FromGalleryImage"


class FileUploadOptions(Enum):

    upload_files_and_generate_sas_tokens = "UploadFilesAndGenerateSasTokens"
    none = "None"


class PremiumDataDisk(Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class TargetCostStatus(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ReportingCycleType(Enum):

    calendar_month = "CalendarMonth"
    custom = "Custom"


class CostType(Enum):

    unavailable = "Unavailable"
    reported = "Reported"
    projected = "Projected"


class PolicyStatus(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class PolicyFactName(Enum):

    user_owned_lab_vm_count = "UserOwnedLabVmCount"
    user_owned_lab_premium_vm_count = "UserOwnedLabPremiumVmCount"
    lab_vm_count = "LabVmCount"
    lab_premium_vm_count = "LabPremiumVmCount"
    lab_vm_size = "LabVmSize"
    gallery_image = "GalleryImage"
    user_owned_lab_vm_count_in_subnet = "UserOwnedLabVmCountInSubnet"
    lab_target_cost = "LabTargetCost"


class PolicyEvaluatorType(Enum):

    allowed_values_policy = "AllowedValuesPolicy"
    max_value_policy = "MaxValuePolicy"


class UsagePermissionType(Enum):

    default = "Default"
    deny = "Deny"
    allow = "Allow"
