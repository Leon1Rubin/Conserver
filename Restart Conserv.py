import paramiko
import time
import socket

# Get user input for station and slot from the console
rack = input("Enter the station number: ")
cell = input("Enter the slot number: ")

# VM details
ip_address = f"10.42.{rack}.{cell}0"
username = "U"
password = "P"

def is_vm_available(ip_address, port=22, timeout=3):
    """Check if the VM is available by attempting a socket connection."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip_address, port))
            return True
    except socket.error:
        return False

def restart_vm(ip_address, username, password):
    # SSH connection setup
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to VM
        print(f"Connecting to {ip_address}...")
        ssh.connect(ip_address, username=username, password=password)

        # Issue reboot command
        print(f"Issuing reboot command...")
        stdin, stdout, stderr = ssh.exec_command("sudo reboot")

        # Wait for the VM to reboot (adjust the sleep time if needed)
        print(f"Sleeping for 45 seconds...")
        time.sleep(45)

        # Check VM availability
        print(f"Checking VM availability...")
        if is_vm_available(ip_address):
            print(f"VM at {ip_address} successfully rebooted.")
        else:
            print(f"Failed to connect to {ip_address}. The VM may not have rebooted successfully.")

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your username and password.")
    except paramiko.SSHException as e:
        print(f"Unable to establish SSH connection: {e}")
    finally:
        # Close SSH connection
        ssh.close()

# Call the function with user input values
if is_vm_available(ip_address, port=22, timeout=3):
    print(f"VM at {ip_address} is available.")
else:
    print(f"VM at {ip_address} is not available. Restarting...")

print(f"Restarting VM at 10.42.{rack}.{cell}0...")
restart_vm(ip_address, username, password)
print("Restart complete.")