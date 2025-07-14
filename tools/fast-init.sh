#!/usr/bin/env bash
# Author: Juan Medina
# Date: Jul 2025
# Description: Setup Microservices Class System
# curl -sL https://github.com/your-script.sh | bash

set -o pipefail

# 1. Check for root privileges
if [[ ${UID} -ne 0 ]]; then
    echo "Error: This script must be executed with sudo." >&2
    exit 1
fi

dnf install -yq \
    https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm 
    https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
dnf install -yq \
    ansible git curl podman podman-compose pip python vim yq jq
echo "vboxuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/vboxuser
systemctl enable --now sshd
echo "YOUR IP ADDRESS: $(ip a | grep -w inet | tail -1 | sed 's,/, ,g' |awk '{print $2}')"
# dnf upgrade -y
# dnf clean all
# systemctl reboot
