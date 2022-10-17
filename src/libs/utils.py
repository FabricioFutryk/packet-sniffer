from colorama import Fore


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

    @staticmethod
    def protocol_to_color(protocol):
        colors = {
            "TCP": Fore.LIGHTBLUE_EX,
            "UDP": Fore.RED,
            "ICMP": Fore.YELLOW,
        }

        return colors[protocol]
