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
        source_port, destination_port, size = struct.unpack('! H H 2x H', raw_data[:8])

        output = {
            "source_port": source_port,
            "destination_port": destination_port,
            "size":  size,
            "payload": ipv4_data[8:],
        }

        return output

    @staticmethod
    def unpack_icmp(ipv4_data):
        type, code , checksum = struct.unpack('! B B H', raw_data[:4])
        
        output = {
            "type": type,
            "code": code,
            "checksum": checksum,
            "payload": ipv4_data[4:],
        }

        return output
