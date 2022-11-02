import struct
from libs.utils import Utils


class Unpacker():
    @staticmethod
    def unpack_ipv4(data):
        version_header_length = data[0]

        version = version_header_length >> 4
        header_length = (version_header_length & 15) * 4

        ttl, protocol, source, target = struct.unpack(
            "! 8x B B 2x 4s 4s", data[:20])

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
        source_port, destination_port, sequence, acknowledgment, offset_reserved_flags = struct.unpack(
            '! H H L L H', ipv4_data[:14])
        offset = (offset_reserved_flags >> 12) * 4
        flag_urg = (offset_reserved_flags & 32) >> 5
        flag_ack = (offset_reserved_flags & 16) >> 4
        flag_psh = (offset_reserved_flags & 8) >> 3
        flag_rst = (offset_reserved_flags & 4) >> 2
        flag_syn = (offset_reserved_flags & 2) >> 1
        flag_fin = offset_reserved_flags & 1

        output = {
            "sourcePort": source_port,
            "destinationPort": destination_port,
            "sequence":  sequence,
            "acknowledgment": acknowledgment,
            "flags": {
                "urg": flag_urg,
                "ack": flag_ack,
                "psh": flag_psh,
                "rst": flag_rst,
                "syn": flag_syn,
                "fin": flag_fin,
            },
            "payload": ipv4_data[offset:],
        }

        return output

    @staticmethod
    def unpack_udp(ipv4_data):
        source_port, destination_port, size = struct.unpack(
            '! H H 2x H', ipv4_data[:8])

        output = {
            "sourcePort": source_port,
            "destinationPort": destination_port,
            "size":  size,
            "payload": ipv4_data[8:],
        }

        return output

    @staticmethod
    def unpack_icmp(ipv4_data):
        _type, code, checksum = struct.unpack('! B B H', ipv4_data[:4])

        output = {
            "type": _type,
            "code": code,
            "checksum": checksum,
            "payload": ipv4_data[4:],
        }

        return output
