#!/bin/bash
# Check if the script is running as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as the root user."
    exit 1
fi

# Turn off swap
echo "Running: swapoff -a"
sudo swapoff -a

# Create a swap file
echo "Running: dd if=/dev/zero of=/swapfile bs=8M count=4096"
sudo dd if=/dev/zero of=/swapfile bs=8M count=4096

# Make the swap file
echo "Running: mkswap /swapfile"
sudo mkswap /swapfile

# Enable swap
echo "Running: swapon /swapfile"
sudo swapon /swapfile


# Get UUID of /dev/nvme0n1p2 and extract the second column (UUID)
UUID=$(sudo blkid /dev/nvme0n1p2 | awk '{print $2}' | sed 's/"//g')

# Get physical offset from /swapfile and remove trailing ".."
PHYSICAL_OFFSET=$(sudo filefrag -v /swapfile | awk '{print $4}' | awk 'NR % 4 == 0' | head -n 1 | sed 's/\.\.//')

UUID1="resume=$UUID"
#echo $UUID1

PHYSICAL_OFFSET1="resume_offset=$PHYSICAL_OFFSET"
#echo $PHYSICAL_OFFSET1

sed -i "s/GRUB_CMDLINE_LINUX=\"/GRUB_CMDLINE_LINUX=\"$UUID1 $PHYSICAL_OFFSET1 /g" /etc/default/grub

# Update GRUB
echo "Running: sudo update-grub"
sudo update-grub

# Prompt the user to reboot
echo "Please reboot your system for the changes to take effect."

