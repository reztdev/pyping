#!/usr/bin/python3
import pyping
import argparse
from pyping import pyping


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pinging Tools Clone",
                    formatter_class=lambda prog: argparse.HelpFormatter(
                        prog, max_help_position=70, width=100))
    parser.add_argument("host", type=str, help="Host to ping (required)")
    parser.add_argument("-c", "--count", type=int, default=5, help="Number of packets to send (default: 5)")
    parser.add_argument("-p", "--payload", type=str, help="Pattern to use for the payload (default: None)")
    parser.add_argument('-pt', "--protocol", type=str, default="icmp", help="Specified protocol. Supported (icmp, tcp, udp)")
    parser.add_argument("-V", "--verbose", default=False, help="Write stdout more info results (default: False)")
    parser.add_argument("-v", "--version", action="version", version="Version: 1.0 (Mochammad Rizki)", help="Show version info")
    args = parser.parse_args()
    pyping.ping(args.host, count=args.count, payload=args.payload, verbose=args.verbose, protocol=args.protocol)

