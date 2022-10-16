import struct
from libs.utils import Utils

class Unpacker():
    @staticmethod
    def unpack_ipv4(data):
        version_header_length = data[0]

        version = version_header_length >> 4
        header_length = version_header_length & 15

        ttl, protocol, source, target = struct.unpack("! 8x B B 2x 4s 4s", data[:20])

        output = {
            "version": version,
            "ttl":  ttl,
            "protocol":  Utils.format_protocol(protocol),
            "source": Utils.format_ipv4(source),
            "target": Utils.format_ipv4(target),
            "payload": data[header_length:],
        }

        return output

    @staticmethod
    def unpack_tcp(ipv4_data):
        pass

    @staticmethod
    def unpack_udp(ipv4_data):
        pass

    @staticmethod
    def unpack_icmp(ipv4_data):
        pass
