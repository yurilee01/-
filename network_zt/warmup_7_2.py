import ipaddress

parent = ipaddress.ip_network("192.168.50.0/24")

for block in parent.subnets(new_prefix=27):
    print(block)