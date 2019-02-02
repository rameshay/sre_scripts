#!/usr/bin/env python3
import ipaddress

def get_ipaddr_from_range():
    '''
    Method that will return an ip address from the
    set of ranges.
    '''
    ip_ranges = [
        "54.66.195.72/29",
        "18.228.1.160/27",
        "35.183.38.96/27",
        "34.241.197.0/27",
        "54.154.127.248/29",
        "54.169.191.160/27",
        "34.226.36.128/27",
        "34.238.188.64/26",
        "54.210.63.224/28",
        "13.56.24.0/26",
        "54.241.190.144/28"
    ]
    for network in ip_ranges:
        ipv4_nw = ipaddress.IPv4Network(network, strict=True)
        for ip_addr in ipv4_nw.hosts():
            yield ip_addr

if __name__ == "__main__":
    for addr in get_ipaddr_from_range():
        print(addr)
