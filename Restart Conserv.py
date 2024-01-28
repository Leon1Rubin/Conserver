import paramiko
import time
import subprocess

def restart_vm(station, slot):
    # VM details
    ip_address = f"10.42.{station}.{slot}0"
    username = "u"
    password = "p"

    # SSH connection setup
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to VM
        ssh.connect(ip_address, username=username, password=password)

        # Issue reboot command
        stdin, stdout, stderr = ssh.exec_command("sudo reboot")

        print("Sleeping for 10 seconds...")
        # Wait for the VM to reboot (adjust the sleep time if needed)
        time.sleep(10)

        # Check VM availability with ping
        print("Checking VM availability...")
        ping_cmd = subprocess.Popen(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ping_cmd.communicate()

        if ping_cmd.returncode == 0:
            print(f"VM at {ip_address} successfully rebooted.")
        else:
            print(f"Failed to ping {ip_address}. The VM may not have rebooted successfully.")

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your username and password.")
    except paramiko.SSHException as e:
        print(f"Unable to establish SSH connection: {e}")
    finally:
        # Close SSH connection
        ssh.close()

# Get user input for station and slot from the console
station_input = input("Enter the station number: ")
slot_input = input("Enter the slot number: ")

# Convert user input to integers
try:
    station_value = int(station_input)
    slot_value = int(slot_input)
except ValueError:
    print("Invalid input. Please enter valid integers for station and slot.")
    exit()

# Call the function with user input values

print(f"Restarting VM at 10.42.{station_value}.{slot_value}0...")
restart_vm(station_value, slot_value)
print("Restart complete.")
