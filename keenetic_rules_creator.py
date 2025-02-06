#!/usr/bin/env python3

import sys
import ipaddress

def usage():
    print(f"Usage: {sys.argv[0]} <filepath> <gateway>")


def parse_address(ip_address: str) -> ipaddress.IPv4Network:
    return ipaddress.ip_network(ip_address)


def main():
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    filepath = sys.argv[1]
    gateway = sys.argv[2]
    networks = []
    with open(filepath, 'r') as f:
        try:
            for line in f:
                # Remove whitespaces
                line = line.strip()
                if line.startswith('#') or len(line) == 0:
                    # Skip empty and comment
                    continue
                # Remove comments from the end of string
                line = line.split('#')[0].strip()
                network = parse_address(line)
                networks.append(network)
        except Exception as e:
            print(f'Invalid file: {e}')
            sys.exit(1)

    # Print rules to stdout
    for network in networks:
        print(f'route ADD {network.network_address} MASK {network.netmask} {gateway}')


if __name__ == '__main__':
    main()
