import ipaddress

dev = ipaddress.ip_network("192.168.50.0/25")
ops = ipaddress.ip_network("192.168.50.64/26")

print(dev.overlaps(ops))
