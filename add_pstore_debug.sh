#Author: shashir s , Oct 2023
#!/bin/bash
# Check if the script is running as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as the root user."
    exit 1
fi

sed -i "s/GRUB_CMDLINE_LINUX=\"/GRUB_CMDLINE_LINUX=\"printk.always_kmsg_dump=y /g" /etc/default/grub

# Update GRUB
echo "Running: sudo update-grub"
sudo update-grub

# Prompt the user to reboot
echo "Please reboot your system for the changes to take effect."
