from colorama import Back, Fore
from libs.utils import Utils


class Logger():
    def __init__(self, args):
        if args["filter"] is not None:
            self.filter = args["filter"].split("/")
        else:
            self.filter = None

        if args["sourcePorts"] is not None:
            self.sP = set()

            for arg in args["sourcePorts"].split(","):
                if ":" in arg:
                    start, end = map(int, arg.split(":"))
                    self.sP.update(set(range(start, end)))
                else:
                    self.sP.add(int(arg))

            print(self.sP)
        else:
            self.sP = None

        if args["destinationPorts"] is not None:
            self.dP = set()

            for arg in args["destinationPorts"].split(","):
                if ":" in arg:
                    start, end = map(int, arg.split(":"))
                    self.dP.update(set(range(start, end)))
                else:
                    self.dP.add(int(arg))

            print(self.dP)
        else:
            self.dP = None

    def check_filters(self, ipv4_header, packet):
        if self.filter is not None and ipv4_header["protocol"] not in self.filter:
            return False

        if ipv4_header["protocol"] in ["TCP", "UDP"]:
            if packet["sourcePort"] not in self.sP or packet["destinationPort"] not in self.dP:
                return False

        return True

    def log(self, ipv4_header, packet):
        if not self.check_filters(ipv4_header, packet):
            return

        protocol, ttl = ipv4_header["protocol"], ipv4_header["ttl"]
        source, target = ipv4_header["source"], ipv4_header["target"]

        message = Utils.protocol_to_color(
            protocol) + "[{}] " + Fore.RESET + "{}: -> {}: TTL: {}"

        if protocol == "TCP":
            message += "\n"

            for flag, state in packet["flags"]:
                if state:
                    message += Back.GREEN + \
                        f" {flag.upper()} " + Back.RESET + " "
                else:
                    message += Back.RED + \
                        f" {flag.upper()} " + Back.RESET + " "
        elif protocol == "ICMP":
            pass

        print(message.format(protocol, source, target, ttl))
