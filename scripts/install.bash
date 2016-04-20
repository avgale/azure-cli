#!/usr/bin/env bash
# 
# Bash script to install the Azure CLI
#
INSTALL_SCRIPT_URL=http://azure-cli-nightly.cloudapp.net/install.py
_TTY=/dev/tty

install_script=$(mktemp -t azure_cli_install_tmp_XXXX) || exit
echo "Downloading Azure CLI install script from $INSTALL_SCRIPT_URL to $install_script."
curl -# $INSTALL_SCRIPT_URL > $install_script || exit
chmod 775 $install_script
echo "Running install script."

if [[ -z "$AZURE_CLI_DISABLE_PROMPTS" && -t 1 ]]; then
    $install_script < $_TTY
else
    export AZURE_CLI_DISABLE_PROMPTS=1
    $install_script
fi
