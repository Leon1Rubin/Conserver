<details>

<summary>VM Restart Script</summary>

# VM Restart Script

## Overview
This script provides an automated way to restart a virtual machine (VM) using SSH. 
It checks the VM's availability, restarts it, and verifies the reboot by checking the system's uptime. 

## Features  
-  **VM Availability Check**: Determines if the VM is reachable over the network before attempting a restart. 
-  **Automated VM Restart**: Restarts the VM using SSH commands. 
-  **Uptime Validation**: Validates the VM's reboot by checking its uptime. 
-  **Logging**: Detailed logging for each step of the process for better tracking and debugging. 
-  **Modular Design**: Code is structured into functions for better readability and maintenance. 

## Requirements  
- Python 3.x - Paramiko library for SSH connections 
- A VM that is accessible over the network 
## Installation  
1. Ensure Python 3.x is installed on your system. 
2. 2. Install Paramiko using pip: `pip install paramiko`
## Usage 
Run the script from the command line with the required arguments:
`python restart_vm.py [rack] [cell] [username] [password]`

Replace `[rack]`, `[cell]`, `[username]`, and `[password]` with appropriate values for your VM. 
## Functions  
-  `is_vm_available`: Checks if the VM is available over the network. 
-  `validate_uptime`: Validates if the VM's uptime indicates a recent reboot. 
-  `create_ssh_client`: Creates a new SSH client. 
-  `establish_ssh_connection`: Establishes an SSH connection with the VM. 
-  `execute_ssh_command`: Executes a command on the VM via SSH. 
-  `reboot_vm`: Sends a reboot command to the VM. 
-  `reconnect_to_vm`: Attempts to reconnect to the VM after a reboot.
-  `main_argument_parser`: Parses command-line arguments. 
-  `main_logic`: Encapsulates the main logic for restarting the VM. 
-  `main`: Entry point of the script. ## License Specify your license here. 

</details>
<details>

<summary>IP Availability Checker</summary>


# IP Availability Checker

This Python script checks the availability of IP addresses within a specified rack and slot in a data center or network environment. It uses the `ping` command to verify if each IP address is reachable from the host system where the script is executed.

## Features

- Supports specifying rack and slot for targeted IP address checks.
- Maps each IP address to its designated location, such as "Conserve", "Canister 1 BF1", etc., for easy identification.
- Provides immediate feedback on the availability status of each IP address.

## IP Address Configuration

The script contains a predefined mapping (`ip_map`) of rack and slot combinations to their respective IP addresses and locations. This configuration can be easily extended or modified within the script to match the actual setup in your environment.

## Requirements

- Python 3.x
- A Unix-like operating system (for the given `ping` syntax) or modifications to the script for compatibility with other operating systems (e.g., Windows).

## Usage

To use the script, you need to provide the rack and slot numbers as command-line arguments. The script will then check the availability of all IP addresses associated with that rack and slot, printing the status and location of each IP.

```bash
python check_ip_availability.py <rack_number> <slot_number>
```

### Example

`python check_ip_availability.py 5 3` 

This command checks and prints the availability of all IP addresses in rack 5, slot 3, along with their designated locations.

## Extending the IP Configuration

To add or modify the IP address configurations, edit the `ip_map` dictionary in the script. Each entry should follow the format:

`(rack, slot): [
    ("IP_address", "Location"),
    ...
],` 

## Note

The script currently uses a `ping` command suitable for Unix-like systems. If running on Windows, adjust the `ping` command parameters in the `ping_ip` function to match the Windows `ping` syntax.

## Disclaimer

This script is for informational and educational purposes. Ensure you have permission to ping the specified IP addresses in your network.

<details>
