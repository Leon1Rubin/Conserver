# VM Restart Script

## Introduction
This script is designed to restart virtual machines remotely. 
It uses SSH for connection and allows specifying the VM's rack, cell, username, and password as command-line arguments.

## Requirements
-   Python 3.x
-   Paramiko library

## Installation
1.  Ensure Python 3.x is installed on your system.
2.  Install Paramiko using pip: `pip install paramiko`

## Usage
Run the script from the command line, providing the necessary arguments:

`python Restart_Conserv.py <rack> <cell> <username> <password>` 

### Arguments
-   `rack`: The rack number of the VM.
-   `cell`: The cell number of the VM.
-   `username`: SSH username for the VM.
-   `password`: SSH password for the VM.

### Example
To restart a VM located at rack 1, cell 2, with username 'admin' and password 'admin123', use:
`python Restart_Conserv.py 1 2 admin admin123` 

## Help
For a list of all available arguments, use the `-h` or `--help` flag:
`python Restart_Conserv.py --help`
