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
