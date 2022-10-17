from libs.sniffer import PacketSniffer
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="packet-sniffer", description="Capture network packets")

    parser.add_argument('--filter', '-f', type=str,
                        help="Filter the packets that you want to be shown. Ex: TCP/UDP/ICMP")
    parser.add_argument('--sourcePorts', '-sP', type=str,
                        help="Filter the packets with specified source port. Ex: 25565 or 0:443")
    parser.add_argument('--destinationPorts', '-dP', type=str,
                        help="Filter the packets with specified destination port. Ex: 25565 or 0:443")

    args = parser.parse_args()

    sniffer = PacketSniffer(vars(args))
    sniffer.start_sniffing()
