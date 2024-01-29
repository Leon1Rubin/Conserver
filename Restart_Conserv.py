import paramiko  # Import the Paramiko library for SSH connections
import time      # Import the time library for sleep functionality
import socket    # Import the socket library for socket operations
import argparse  # Import the argparse library for parsing command-line arguments

# Define a function to check VM availability
def is_vm_available(ip_address: str, port: int = 22, timeout: int = 3) -> bool:
    """Check if the VM is available by attempting a socket connection."""
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)  # Set a timeout for the socket connection
            s.connect((ip_address, port))  # Try to connect to the given IP and port
            return True  # Return True if the connection is successful
    except socket.error:
        return False  # Return False if there is a socket error (VM is not available)

# Define a function to restart a VM
def restart_vm(ip_address: str, username: str, password: str) -> None:
    ssh = paramiko.SSHClient()  # Create an SSH client instance
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Set policy to automatically add the host key

    try:
        # Attempt to establish an SSH connection
        print(f"Connecting to {ip_address}...")
        ssh.connect(ip_address, username=username, password=password)  # Connect using the provided credentials

        # Send a command to reboot the VM
        print(f"Issuing reboot command...")
        stdin, stdout, stderr = ssh.exec_command("sudo reboot")

        # Wait for the VM to reboot
        print(f"Sleeping for 60 seconds...")
        time.sleep(60)

        # Check if the VM is available after reboot
        print(f"Checking VM availability...")
        if is_vm_available(ip_address):
            print(f"VM at {ip_address} successfully rebooted.")
        else:
            print(f"Failed to connect to {ip_address}. The VM may not have rebooted successfully.")

    except paramiko.AuthenticationException:
        raise Exception("Authentication failed. Check your username and password.")  # Handle authentication errors
    except paramiko.SSHException as e:
        print(f"Unable to establish SSH connection: {e}")  # Handle other SSH connection errors
    finally:
        ssh.close()  # Ensure the SSH connection is closed

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Restart a VM.')
    # Define required command-line arguments
    parser.add_argument('rack', type=int, help='The station number')
    parser.add_argument('cell', type=int, help='The slot number')
    parser.add_argument('username', type=str, help='Username for VM SSH')
    parser.add_argument('password', type=str, help='Password for VM SSH')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Construct the VM's IP address from the provided rack and cell values
    ip_address = f"10.42.{args.rack}.{args.cell}0"

    # Check if the VM is available
    if is_vm_available(ip_address):
        print(f"VM at {ip_address} is available.")
    else:
        print(f"VM at {ip_address} is not available. Restarting...")

    # Restart the VM
    print(f"Restarting VM at {ip_address}...")
    restart_vm(ip_address, args.username, args.password)
    print("Restart complete.")  # Print a completion message

if __name__ == "__main__":
    main()