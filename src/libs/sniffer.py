import socket as sk
from libs.unpacker import Unpacker

class PacketSniffer():
    def __init__(self, host = "0.0.0.0"):
        self.socket = sk.socket(sk.AF_INET, sk.SOCK_RAW, sk.IPPROTO_IP)

        self.socket.bind((host,0))
        self.socket.setsockopt(sk.IPPROTO_IP, sk.IP_HDRINCL, 1)

    def start_sniffing(self):
        try:
            while True:
                raw_data, _ = self.socket.recvfrom(65535) 

                ipv4_header = Unpacker.unpack_ipv4(raw_data)
                print(ipv4_header)

        except KeyboardInterrupt:
            print("Packet Sniffing Ended!")
            

    def log(self, info):
        pass