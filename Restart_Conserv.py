# Import necessary libraries
import paramiko  # SSH connection functionality
import time      # Time-related functions, such as sleep
import socket    # Network connection functionality
import argparse  # Command-line argument parsing
import re        # Regular expressions for pattern matching in strings

# Function to check if a VM is reachable over the network
def is_vm_available(ip_address: str, port: int = 22, timeout: int = 3) -> bool:
    """Attempts to create a socket connection to check if a VM is available."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Open a TCP socket
            s.settimeout(timeout)  # Set a timeout for the socket operation
            s.connect((ip_address, port))  # Try connecting to the IP address and port
            return True  # Return True if connection is successful
    except socket.error:
        return False  # Return False if there's an error (VM not available)

# Function to get the system's uptime via SSH
def get_system_uptime(ssh: paramiko.SSHClient) -> str:
    """Runs the 'uptime' command on the VM and returns its output."""
    stdin, stdout, stderr = ssh.exec_command("uptime")  # Execute the uptime command
    return stdout.read().decode().strip()  # Decode and strip the output, then return it

# Function to validate if the uptime indicates a recent reboot
def validate_uptime(uptime_str: str) -> bool:
    """Uses regex to check if the VM's uptime indicates it was recently rebooted."""
    match = re.search(r"up\s+(\d+)\s+min", uptime_str)  # Look for the 'up X min' pattern
    if match:
        uptime_minutes = int(match.group(1))  # Extract the number of minutes
        return uptime_minutes < 5  # True if uptime is less than 5 minutes, indicating a recent reboot
    return False  # False if uptime doesn't indicate a recent reboot

# Function to restart a VM
def restart_vm(ip_address, username, password):
    ssh = paramiko.SSHClient()  # Create a new SSH client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Set policy to add new host keys

    try:
        print(f"Connecting to {ip_address}...")  # Indicate start of connection
        ssh.connect(ip_address, username=username, password=password)  # Connect to VM

        print(f"Issuing reboot command...")  # Indicate reboot command being sent
        stdin, stdout, stderr = ssh.exec_command("sudo reboot")  # Send reboot command
        ssh.close()  # Close SSH session as reboot will disconnect it

        print(f"Sleeping for 55 seconds...")  # Wait for the VM to reboot
        time.sleep(55)  # Sleep for 55 seconds

        # Reconnect to VM after reboot
        reconnect_attempts = 0  # Counter for reconnect attempts
        while reconnect_attempts < 5:  # Attempt to reconnect up to 5 times
            try:
                ssh.connect(ip_address, username=username, password=password)  # Try reconnecting
                print(f"Reconnected to {ip_address}.")  # Indicate successful reconnection
                break  # Exit loop on successful reconnection
            except paramiko.SSHException:
                reconnect_attempts += 1  # Increment attempt counter
                print(f"Reconnect attempt {reconnect_attempts} failed, trying again in 30 seconds...")
                time.sleep(30)  # Wait 30 seconds before trying again

        if reconnect_attempts == 5:  # If 5 attempts failed
            print("Failed to reconnect after 5 attempts.")  # Indicate failure to reconnect
            return  # Exit function

        # Check system uptime
        uptime = get_system_uptime(ssh)  # Get system uptime
        print(f"System uptime: {uptime}")  # Print uptime

        # Validate uptime
        if validate_uptime(uptime):  # Check if uptime indicates a recent reboot
            print("Validation successful: The system has been recently rebooted.")
        else:
            print("Validation failed: The system may not have been rebooted recently.")

    except paramiko.AuthenticationException:  # Catch authentication errors
        print("Authentication failed. Please check your username and password.")
    except paramiko.SSHException as e:  # Catch SSH connection errors
        print(f"Unable to establish SSH connection: {e}")
    finally:
        ssh.close()  # Ensure SSH connection is always closed

# Main function to parse arguments and initiate VM restart
def main():
    parser = argparse.ArgumentParser(description='Restart a VM.')  # Set up argument parser
    parser.add_argument('rack', type=int, help='The station number')  # Define rack argument
    parser.add_argument('cell', type=int, help='The slot number')  # Define cell argument
    parser.add_argument('username', type=str, help='Username for VM SSH')  # Define username argument
    parser.add_argument('password', type=str, help='Password for VM SSH')  # Define password argument

    args = parser.parse_args()  # Parse arguments

    ip_address = f"10.42.{args.rack}.{args.cell}0"  # Construct the VM's IP address

    if is_vm_available(ip_address):  # Check if VM is available before restarting
        print(f"VM at {ip_address} is available.")
    else:
        print(f"VM at {ip_address} is not available. Restarting...")

    print(f"Restarting VM at {ip_address}...")  # Indicate VM restart
    restart_vm(ip_address, args.username, args.password)  # Restart VM
    print("Restart complete.")  # Indicate completion of restart

# Check if script is being run directly and not imported
if __name__ == "__main__":
    main()  # Execute main function if script is run directly
