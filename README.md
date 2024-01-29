# Restart_Conserv.py

## Overview
The `Restart_Conserv.py` script is a Python utility for remotely restarting virtual machines (VMs) over SSH. It is designed to be used in situations where you need to automate the process of restarting VMs in a specific network configuration.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Functions](#functions)
  - [is_vm_available](#is_vm_available)
  - [get_system_uptime](#get_system_uptime)
  - [validate_uptime](#validate_uptime)
  - [restart_vm](#restart_vm)
- [Main Function](#main-function)
- [Example](#example)
- [License](#license)

## Prerequisites
Before using this script, ensure you have the following prerequisites in place:
- Python 3.x installed
- The `paramiko` library for SSH connections. You can install it using `pip`:
pip install paramiko

- Access to the VMs over SSH with appropriate credentials.

## Usage
To use the script, run it from the command line with the following arguments:

python Restart_Conserv.py <rack> <cell> <username> <password>

- `<rack>`: The station number.
- `<cell>`: The slot number.
- `<username>`: The SSH username for VM access.
- `<password>`: The SSH password for VM access.

## Functions
The script includes several functions to manage the VMs:

### is_vm_available
This function checks if a VM is reachable over the network by attempting to create a socket connection to it.

### get_system_uptime
This function runs the 'uptime' command on the VM and returns its output.

### validate_uptime
This function uses regular expressions to check if the VM's uptime indicates it was recently rebooted.

### restart_vm
This function restarts a VM by issuing a 'sudo reboot' command over SSH. It also handles the reconnection to the VM after the reboot.

## Main Function
The `main` function is the entry point of the script. It parses command-line arguments and initiates the VM restart process.

## Example
Here is an example of how to use the script:

`python Restart_Conserv.py (rack) (cell) (username) (password)`

This command will restart the VM located at IP address 10.42.(rack).(cell)0 with the provided username and password.

## License
This script is provided under the MIT License.
