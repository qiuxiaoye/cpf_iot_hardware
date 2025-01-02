import socket
import requests
import netifaces

class IPFetcher:
    def __init__(self):
        pass
    
    def get_device_ip():
        try:
            # Create a socket to connect to an external address
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Use a public IP address (does not need to be reachable)
            # s.connect(("8.8.8.8", 80))
            s.connect(("8.8.8.8", 80))
            # Get the local IP address
            ip_address = s.getsockname()[0]
            s.close()
            return ip_address
        except Exception as e:
            print(f"Error obtaining IP address: {e}")
            return None

    def get_public_ip():
        try:
            # Use a public API to fetch your public IP address
            response = requests.get("https://api.ipify.org?format=json")
            response.raise_for_status()
            return response.json().get("ip")
        except Exception as e:
            print(f"Error obtaining public IP address: {e}")
            return None
        
    def get_all_ip_with_netifaces():
        try:
            for interface in netifaces.interfaces():
                addresses = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addresses:
                    for addr in addresses[netifaces.AF_INET]:
                        print(f"Interface: {interface}, IP Address: {addr['addr']}")
        except Exception as e:
            print(f"Error listing IPs: {e}")

import netifaces

def get_wlan0_ip():
    interface = 'wlan0'
    try:
        # Get the addresses for the specified interface
        addresses = netifaces.ifaddresses(interface)
        # Retrieve the IPv4 address
        ip_info = addresses.get(netifaces.AF_INET)
        if ip_info:
            return ip_info[0]['addr']
        else:
            return "No IPv4 address found for wlan0"
    except ValueError:
        return "Interface wlan0 not found"
    except KeyError:
        return "No address assigned to wlan0"

    # def get_ip_by_interface(interface_name):
    #     """Get the IP address for a specific network interface."""
    #     try:
    #         # Retrieve the addresses associated with the interface
    #         addresses = netifaces.ifaddresses(interface_name)
    #         # Check if the interface has an IPv4 address
    #         if netifaces.AF_INET in addresses:
    #             # Return the first IPv4 address found
    #             return addresses[netifaces.AF_INET][0]['addr']
    #         else:
    #             return f"No IPv4 address found for interface {interface_name}"
    #     except ValueError:
    #         return f"Interface {interface_name} not found."
    #     except Exception as e:
    #         return f"Error retrieving IP address for {interface_name}: {e}"
