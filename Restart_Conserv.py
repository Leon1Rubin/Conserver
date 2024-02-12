import paramiko  # Import Paramiko for SSH operations
import time      # Import time module for sleep functionality
import socket    # Import socket module for checking VM availability
import argparse  # Import argparse for command-line argument parsing
import re        # Import re module for regular expression operations
import logging   # Import logging module for logging information and errors

# Configure the logging system to display information level logs and their messages
logging.basicConfig(level=logging.INFO, format='%(message)s')

def is_vm_available(ip_address: str, port: int = 22, timeout: int = 3) -> bool:
    """Check if a VM is reachable over the network."""
    try:
        # Create a socket object for network connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)  # Set a timeout for the socket operation
            s.connect((ip_address, port))  # Attempt to establish a socket connection
            return True  # Return True if connection is successful
    except socket.error:
        return False  # Return False if there's an error (VM not reachable)

def validate_uptime(uptime_str: str) -> bool:
    """Check if the VM's uptime indicates a recent reboot."""
    match = re.search(r"up\s+(\d+)\s+min", uptime_str)  # Use regex to search for uptime pattern
    if match:
        uptime_minutes = int(match.group(1))  # Extract minutes from the uptime string
        return uptime_minutes < 5  # Return True if uptime is less than 5 minutes (recent reboot)
    return False  # Return False if the condition is not met

def create_ssh_client():
    """Create and return a configured SSH client."""
    ssh = paramiko.SSHClient()  # Initialize a new SSH client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Set policy to automatically add unknown host keys
    return ssh  # Return the configured SSH client

def establish_ssh_connection(ssh, ip_address, username, password):
    """Establish an SSH connection with the given credentials."""
    try:
        ssh.connect(ip_address, username=username, password=password)  # Attempt to connect to the SSH server
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your username and password.")
        return False  # Return False if authentication fails
    return True  # Return True if connection is successful

def execute_ssh_command(ssh, command):
    """Execute a command via SSH and return the output."""
    stdin, stdout, stderr = ssh.exec_command(command)  # Execute command via SSH
    return stdout.read().decode().strip()  # Return the command output

def reboot_vm(ssh):
    """Send a reboot command to the VM."""
    execute_ssh_command(ssh, "sudo reboot")  # Execute the reboot command
    ssh.close()  # Close the SSH connection

def reconnect_to_vm(ip_address, username, password):
    """Attempt to reconnect to the VM."""
    ssh = create_ssh_client()  # Create a new SSH client
    reconnect_attempts = 0  # Initialize reconnect attempt counter
    while reconnect_attempts < 5:  # Attempt to reconnect up to 5 times
        if establish_ssh_connection(ssh, ip_address, username, password):
            print(f"Reconnected to {ip_address}.")
            return ssh  # Return the SSH client if reconnection is successful
        reconnect_attempts += 1  # Increment the attempt counter
        print(f"Reconnect attempt {reconnect_attempts} failed, trying again in 30 seconds...")
        time.sleep(30)  # Wait for 30 seconds before the next attempt
    print("Failed to reconnect after 5 attempts.")
    return None  # Return None if reconnection fails

def main_argument_parser():
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(description='Restart a VM.')  # Initialize argument parser
    # Add expected arguments
    parser.add_argument('rack', type=int, help='The station number')
    parser.add_argument('cell', type=int, help='The slot number')
    parser.add_argument('username', type=str, help='Username for VM SSH')
    parser.add_argument('password', type=str, help='Password for VM SSH')
    return parser.parse_args()  # Parse and return the arguments

def main_logic(args):
    """Main logic of the script."""
    ip_address = f"10.42.{args.rack}.{args.cell}0"  # Construct the IP address from arguments
    if not is_vm_available(ip_address):  # Check if VM is available
        logging.info(f"VM at {ip_address} is not available. Restarting...")

    ssh = create_ssh_client()  # Create an SSH client
    if establish_ssh_connection(ssh, ip_address, args.username, args.password):  # Establish SSH connection
        logging.info(f"Connected to {ip_address}.")
        logging.info("Rebooting the VM...")
        reboot_vm(ssh)  # Reboot the VM
        logging.info("Waiting 55 seconds for the VM to come back online...")
        time.sleep(55)  # Wait for the VM to reboot
        logging.info("Attempting to reconnect to the VM...")
        ssh = reconnect_to_vm(ip_address, args.username, args.password)  # Attempt to reconnect to the VM
        logging.info("Reconnected to the VM.")
        if ssh:
            logging.info("Checking if the VM has been rebooted recently...")
            uptime = execute_ssh_command(ssh, "uptime")  # Get system uptime
            logging.info(f"System uptime: {uptime}")
            if validate_uptime(uptime):  # Validate if the reboot was successful
                logging.info("Validation successful: The system has been recently rebooted ✅")
            else:
                logging.warning("Validation failed: The system may not have been rebooted recently ❌")
            ssh.close()  # Close the SSH connection

def main():
    """Entry point of the script."""
    args = main_argument_parser()  # Parse command-line arguments
    main_logic(args)  # Execute the main logic with the parsed arguments

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly