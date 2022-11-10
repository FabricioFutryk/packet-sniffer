class Utils():
    @staticmethod
    def format_ipv4(address):
        return ".".join(map(str, address))

    @staticmethod
    def format_protocol(protocol):
        protocols = {
            1: "ICMP",
            6: "TCP",
            17: "UDP"
        }

        return protocols[protocol]
