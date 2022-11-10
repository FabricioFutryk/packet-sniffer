import socket as sk
from libs.logger import Logger
from libs.unpacker import Unpacker


class PacketSniffer():
    def __init__(self, gui, host="0.0.0.0"):
        self.gui = gui
        self.logger = Logger(self.gui)
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

                if not self.gui.statistics.minTTL or ipv4_header["ttl"] < self.gui.statistics.minTTL:
                    self.gui.statistics.minTTL = ipv4_header["ttl"]

                if not self.gui.statistics.maxTTL or ipv4_header["ttl"] > self.gui.statistics.maxTTL:
                    self.gui.statistics.maxTTL = ipv4_header["ttl"]

                self.gui.statistics.originsValues.add(
                    f'{ipv4_header["source"]}:{packet["sourcePort"]}')
                self.gui.statistics.destinationValues.add(
                    f'{ipv4_header["target"]}:{packet["destinationPort"]}')

                self.logger.log(ipv4_header, packet)
                self.gui.statistics.refresh()

        except KeyboardInterrupt:
            print("Packet Sniffing Ended!")
