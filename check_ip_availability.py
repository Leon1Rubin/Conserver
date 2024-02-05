import subprocess
import sys

# Updated IP address mapping based on rack and slot
ip_map = {
    (5, 1): [
        ("10.42.5.10", "Conserve"),
        ("10.42.5.11", "Canister 1 BF1"),
        ("10.42.5.13", "Canister 1 BF2"),
        ("10.42.5.12", "Canister 1 BMC"),
        ("10.42.5.15", "Canister 2 BF1"),
        ("10.42.5.17", "Canister 2 BF2"),
        ("10.42.5.16", "Canister 2 BMC"),
    ],
    (5, 2): [
        ("10.42.5.20", "Conserve"),
        ("10.42.5.21", "Canister 1 BF1"),
        ("10.42.5.23", "Canister 1 BF2"),
        ("10.42.5.22", "Canister 1 BMC"),
        ("10.42.5.25", "Canister 2 BF1"),
        ("10.42.5.27", "Canister 2 BF2"),
        ("10.42.5.26", "Canister 2 BMC"),
    ],
    (5, 3): [
        ("10.42.5.30", "Conserve"),
        ("10.42.5.31", "Canister 1 BF1"),
        ("10.42.5.33", "Canister 1 BF2"),
        ("10.42.5.32", "Canister 1 BMC"),
        ("10.42.5.35", "Canister 2 BF1"),
        ("10.42.5.37", "Canister 2 BF2"),
        ("10.42.5.36", "Canister 2 BMC"),
    ],
    (5, 4): [
        ("10.42.5.40", "Conserve"),
        ("10.42.5.41", "Canister 1 BF1"),
        ("10.42.5.43", "Canister 1 BF2"),
        ("10.42.5.42", "Canister 1 BMC"),
        ("10.42.5.45", "Canister 2 BF1"),
        ("10.42.5.47", "Canister 2 BF2"),
        ("10.42.5.46", "Canister 2 BMC"),
    ],
    (5, 5): [
        ("10.42.5.50", "Conserve"),
        ("10.42.5.51", "Canister 1 BF1"),
        ("10.42.5.53", "Canister 1 BF2"),
        ("10.42.5.52", "Canister 1 BMC"),
        ("10.42.5.55", "Canister 2 BF1"),
        ("10.42.5.57", "Canister 2 BF2"),
        ("10.42.5.56", "Canister 2 BMC"),
    ],
    (5, 6): [
        ("10.42.5.60", "Conserve"),
        ("10.42.5.61", "Canister 1 BF1"),
        ("10.42.5.63", "Canister 1 BF2"),
        ("10.42.5.62", "Canister 1 BMC"),
        ("10.42.5.65", "Canister 2 BF1"),
        ("10.42.5.67", "Canister 2 BF2"),
        ("10.42.5.66", "Canister 2 BMC"),
    ],
    (5, 7): [
        ("10.42.5.70", "Conserve"),
        ("10.42.5.71", "Canister 1 BF1"),
        ("10.42.5.73", "Canister 1 BF2"),
        ("10.42.5.72", "Canister 1 BMC"),
        ("10.42.5.75", "Canister 2 BF1"),
        ("10.42.5.77", "Canister 2 BF2"),
        ("10.42.5.76", "Canister 2 BMC"),
    ],
    (5, 8): [
        ("10.42.5.80", "Conserve"),
        ("10.42.5.81", "Canister 1 BF1"),
        ("10.42.5.83", "Canister 1 BF2"),
        ("10.42.5.82", "Canister 1 BMC"),
        ("10.42.5.85", "Canister 2 BF1"),
        ("10.42.5.87", "Canister 2 BF2"),
        ("10.42.5.86", "Canister 2 BMC"),
    ],
    (5, 9): [
        ("10.42.5.90", "Conserve"),
        ("10.42.5.91", "Canister 1 BF1"),
        ("10.42.5.93", "Canister 1 BF2"),
        ("10.42.5.92", "Canister 1 BMC"),
        ("10.42.5.95", "Canister 2 BF1"),
        ("10.42.5.97", "Canister 2 BF2"),
        ("10.42.5.96", "Canister 2 BMC"),
    ],
    (5, 10): [
        ("10.42.5.100", "Conserve"),
        ("10.42.5.101", "Canister 1 BF1"),
        ("10.42.5.103", "Canister 1 BF2"),
        ("10.42.5.102", "Canister 1 BMC"),
        ("10.42.5.105", "Canister 2 BF1"),
        ("10.42.5.107", "Canister 2 BF2"),
        ("10.42.5.106", "Canister 2 BMC"),
    ],
    (7, 1): [
        ("10.42.7.10", "Conserve"),
        ("10.42.7.11", "Canister 1 BF1"),
        ("10.42.7.13", "Canister 1 BF2"),
        ("10.42.7.12", "Canister 1 BMC"),
        ("10.42.7.15", "Canister 2 BF1"),
        ("10.42.7.17", "Canister 2 BF2"),
        ("10.42.7.16", "Canister 2 BMC"),
    ],
    (7, 2): [
        ("10.42.7.20", "Conserve"),
        ("10.42.7.21", "Canister 1 BF1"),
        ("10.42.7.23", "Canister 1 BF2"),
        ("10.42.7.22", "Canister 1 BMC"),
        ("10.42.7.25", "Canister 2 BF1"),
        ("10.42.7.27", "Canister 2 BF2"),
        ("10.42.7.26", "Canister 2 BMC"),
    ],
    (7, 3): [
        ("10.42.7.30", "Conserve"),
        ("10.42.7.31", "Canister 1 BF1"),
        ("10.42.7.33", "Canister 1 BF2"),
        ("10.42.7.32", "Canister 1 BMC"),
        ("10.42.7.35", "Canister 2 BF1"),
        ("10.42.7.37", "Canister 2 BF2"),
        ("10.42.7.36", "Canister 2 BMC"),
    ],
    (7, 4): [
        ("10.42.7.40", "Conserve"),
        ("10.42.7.41", "Canister 1 BF1"),
        ("10.42.7.43", "Canister 1 BF2"),
        ("10.42.7.42", "Canister 1 BMC"),
        ("10.42.7.45", "Canister 2 BF1"),
        ("10.42.7.47", "Canister 2 BF2"),
        ("10.42.7.46", "Canister 2 BMC"),
    ],
    (7, 5): [
        ("10.42.7.50", "Conserve"),
        ("10.42.7.51", "Canister 1 BF1"),
        ("10.42.7.53", "Canister 1 BF2"),
        ("10.42.7.52", "Canister 1 BMC"),
        ("10.42.7.55", "Canister 2 BF1"),
        ("10.42.7.57", "Canister 2 BF2"),
        ("10.42.7.56", "Canister 2 BMC"),
    ],
    (7, 6): [
        ("10.42.7.60", "Conserve"),
        ("10.42.7.61", "Canister 1 BF1"),
        ("10.42.7.63", "Canister 1 BF2"),
        ("10.42.7.62", "Canister 1 BMC"),
        ("10.42.7.65", "Canister 2 BF1"),
        ("10.42.7.67", "Canister 2 BF2"),
        ("10.42.7.66", "Canister 2 BMC"),
    ],
    (7, 7): [
        ("10.42.7.70", "Conserve"),
        ("10.42.7.71", "Canister 1 BF1"),
        ("10.42.7.73", "Canister 1 BF2"),
        ("10.42.7.72", "Canister 1 BMC"),
        ("10.42.7.75", "Canister 2 BF1"),
        ("10.42.7.77", "Canister 2 BF2"),
        ("10.42.7.76", "Canister 2 BMC"),
    ],
    (7, 8): [
        ("10.42.7.80", "Conserve"),
        ("10.42.7.81", "Canister 1 BF1"),
        ("10.42.7.83", "Canister 1 BF2"),
        ("10.42.7.82", "Canister 1 BMC"),
        ("10.42.7.85", "Canister 2 BF1"),
        ("10.42.7.87", "Canister 2 BF2"),
        ("10.42.7.86", "Canister 2 BMC"),
    ],
    (7, 9): [
        ("10.42.7.90", "Conserve"),
        ("10.42.7.91", "Canister 1 BF1"),
        ("10.42.7.93", "Canister 1 BF2"),
        ("10.42.7.92", "Canister 1 BMC"),
        ("10.42.7.95", "Canister 2 BF1"),
        ("10.42.7.97", "Canister 2 BF2"),
        ("10.42.7.96", "Canister 2 BMC"),
    ],
    (7, 10): [
        ("10.42.7.100", "Conserve"),
        ("10.42.7.101", "Canister 1 BF1"),
        ("10.42.7.103", "Canister 1 BF2"),
        ("10.42.7.102", "Canister 1 BMC"),
        ("10.42.7.105", "Canister 2 BF1"),
        ("10.42.7.107", "Canister 2 BF2"),
        ("10.42.7.106", "Canister 2 BMC"),
    ],
}


def ping_ip(ip_address):
    try:
        # Adjust for Windows: -n for count, -w for timeout in milliseconds
        output = subprocess.check_output(["ping", "-n", "1", "-w", "1000", ip_address], stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

def check_ips_for_location(rack, slot):
    key = (rack, slot)
    if key in ip_map:
        for ip, location in ip_map[key]:
            is_up = ping_ip(ip)
            status = "Up✅" if is_up else "Down❌"
            print(f"IP {ip} is {status} ({location})")
    else:
        print(f"No IP information for Rack {rack}, Slot {slot}.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python check_ip_availability.py <rack_number> <slot_number>")
    else:
        rack = int(sys.argv[1])
        slot = int(sys.argv[2])
        check_ips_for_location(rack, slot)
