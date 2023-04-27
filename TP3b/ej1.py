import os
from abc import ABC, abstractmethod

class Ping(ABC):
    """
    The Ping interface declares common operations for both RealPing and
    the ProxyPing.
    """

    @abstractmethod
    def execute(self, address: str) -> None:
        pass

class Ping:
    def __init__(self):
        pass

    def execute(self, ip_address):
        if ip_address.startswith("192."):
            for i in range(10):
                response = os.system(f"ping -n 1 {ip_address}")
                if response == 0:
                    print(f"Ping {i+1}: {ip_address} is up!")
                else:
                    print(f"Ping {i+1}: {ip_address} is down.")
        else:
            print("Error: IP address must start with '192.'")
    
    def executefree(self, ip_address):
        for i in range(10):
            response = os.system(f"ping -n 1 {ip_address}")
            if response == 0:
                print(f"Ping {i+1}: {ip_address} is up!")
            else:
                print(f"Ping {i+1}: {ip_address} is down.")
class PingProxy:
    def __init__(self):
        self.ping = Ping()
    
    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)

proxy = PingProxy()
proxy.execute("192.168.0.254")  # hace ping a www.google.com
proxy.execute("192.168.1.1")    # hace ping a 192.168.1.1
