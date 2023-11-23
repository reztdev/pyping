from scapy.all import *
import time
import sys

"""
Simple ping tools, this tools a clone from 'ping tools'. But you can your like code to send the host with pyping. Use a protocol ICMP and TCP.
Please as root or administrator to run this tools.
example: 
    - from pyping import pyping
    - pyping.ping(host="192.168.10.123")

    with payload:
        - pyping.ping(host="192.168.10.123", count=10, payload="\x41\x00\x00")
"""
protos = {1: "icmp", 6: "tcp", 17: "udp"}


def print_ip_header(ip_packet):
    ihl = ip_packet.ihl
    tos = ip_packet.tos
    length = ip_packet.len
    identifier = ip_packet.id
    flags = ip_packet.flags
    protocol = protos.get(ip_packet.proto, ip_packet.proto)
    chksum = hex(ip_packet.chksum)
    print(f"IP Header: ihl={ihl}, tos={hex(tos)}, len={length}, id={identifier}, flags={flags}, proto={protocol}, chksum={chksum}")

                
def ping(host, ttl=20, count=5, payload=None, verbose=False, protocol='icmp'):
    try:
        sent_packets = 0
        received_packets = 0
        min_rtt = float('inf')
        max_rtt = float('-inf')
        total_rtt = 0
        packet_loss = 0

        for i in range(1, count+1):
            if protocol == 'icmp':
                packet = IP(dst=host, ttl=ttl)/ICMP()/Raw(load=payload)
            elif protocol == 'tcp':
                packet = IP(dst=host, ttl=ttl)/TCP()/Raw(load=payload)
            else:
                print("Invalid protocol specified. Supported protocol: icmp, tcp ")
                return

            start_time = time.time()
            reply = sr1(packet, timeout=2, verbose=0)
            end_time = time.time()
            if reply:
                times = (end_time - start_time) * 100
                print(f"{len(reply)} bytes {host} ({reply.src}) {protocol.upper()}_seq={i} ttl={reply.ttl} payload={packet[Raw].load} time={times:.2f} ms ")
                received_packets += 1
                min_rtt = min(min_rtt, times)
                max_rtt = max(max_rtt, times)
                total_rtt += times
                if verbose:
                    print_ip_header(reply)
                    print("Hex Data:")
                    hexdump(reply)
                    print("")
            else:
                print(f"{host} Request timed out {protocol.upper()}_seq={i}")
        
            sent_packets += 1
            time.sleep(1)
        
        packet_loss = (sent_packets - received_packets) / sent_packets * 100
        print(f"\n--- Ping statistics {host} ---:")
        print(f"  Packets: Sent = {sent_packets}, Received = {received_packets}, Lost = {sent_packets-received_packets} ({packet_loss:.0f}% loss)")
        if received_packets > 0:
            avg_rtt = total_rtt / received_packets
            print("--- Approximate round trip times in milli-seconds ---:")
            print(f"  Minimum = {min_rtt:.2f}ms, Maximum = {max_rtt:.2f}ms, Average = {avg_rtt:.2f}ms")

    except KeyboardInterrupt:
        print(f"\n--- {protocol.upper()} Ping statistics for {host} ---:")
        print(f"  Packets: Sent = {count}, Received = {received_packets}, Lost = {count-received_packets} ({packet_loss:.0f}% loss)")
    except socket.gaierror:
        print("No internet connection")
    except PermissionError:
        print("Operation not permitted (as Root/Admin)")


