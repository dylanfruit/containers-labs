#!/usr/bin/env bash
# Author: Juan Medina
# Date: Mar 2025
# Description: Setup Microservices Class System

# Cause pipelines to return the exit status of the last command that failed.
set -o pipefail

# --- Configuration ---
PLAYBOOK="class-setup.yml"
# Tags to run from the playbook
PLAYBOOK_TAGS="repos,container_packages,extra_packages,configurations,security,cockpit,looks,background,containers_looks,final"
# --- End Configuration ---

# === Pre-flight Checks ===

# 1. Check for root privileges
if [[ ${UID} -ne 0 ]]; then
    echo "Error: This script must be executed with sudo." >&2
    exit 1
fi

# 2. Check if running in a live environment
if id "liveuser" &>/dev/null || [ -f /etc/live-release ] || [[ "$(findmnt -n -o FSTYPE /)" =~ (squashfs|overlay) ]]; then
    echo "Error: This script should not be run as the 'liveuser' or from the live ISO environment." >&2
    echo "Please complete the Fedora installation and log in as a regular user before running this script." >&2
    exit 1
fi

# 3. Check if running on Fedora
if ! grep -q '^ID=fedora$' /etc/os-release || [ ! -f /etc/fedora-release ] || ! command -v dnf &>/dev/null; then
    echo "Error: This script is designed to run on Fedora Linux only." >&2
    echo "Please run this script on a Fedora Linux System." >&2
    exit 1
fi

# 4. Check for internet connectivity (using curl to check Google)
if [[ $(wget -q --spider http://google.com; echo $?) -ne 0 ]]; then 
    echo "Internet connection required"
    exit 2
fi

# === Setup ===

# 5. Install required packages
echo "Preflight configuration..."
if ! dnf install -yq ansible git figlet lolcat curl
then
    echo "Error: Failed to install prerequisite packages." >&2
    exit 1
fi

# 6. Prepare visuals
clear
echo "Starting Microservices Class Workstation Setup..."
sleep 5
figlet "Microservices Class Setup" | lolcat

# === Execution ===

if ! ansible-playbook "$PLAYBOOK" --tags "$PLAYBOOK_TAGS"
then
    echo "Error: Ansible playbook execution failed." >&2
    # You might want to exit here to prevent rebooting a misconfigured system
    exit 1
fi

# === Completion ===

figlet "Setup completed!" | lolcat
echo "The system will automatically reboot in 20 seconds..."
echo "      press Ctrl+c if you need to cancel the reboot process"
sleep 20
echo "Rebooting now!"
reboot
