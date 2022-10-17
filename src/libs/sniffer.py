import socket as sk
from libs.logger import Logger
from libs.unpacker import Unpacker
from libs.utils import Utils


class PacketSniffer():
    def __init__(self, logger_args, host="0.0.0.0"):
        self.logger = Logger(logger_args)
        self.socket = sk.socket(sk.AF_INET, sk.SOCK_RAW, sk.IPPROTO_IP)

        self.socket.bind((host, 0))
        self.socket.setsockopt(sk.IPPROTO_IP, sk.IP_HDRINCL, 1)

    def start_sniffing(self):
        unpacking_func = {
            "TCP": Unpacker.unpack_tcp,
            "UDP": Unpacker.unpack_udp,
            "ICMP": Unpacker.unpack_icmp,
        }

        try:
            while True:
                raw_data, _ = self.socket.recvfrom(65535)

                ipv4_header = Unpacker.unpack_ipv4(raw_data)
                protocol, payload = ipv4_header["protocol"], ipv4_header["payload"]

                packet = unpacking_func[protocol](payload)

                self.logger.log(ipv4_header, packet)

        except KeyboardInterrupt:
            print("Packet Sniffing Ended!")
