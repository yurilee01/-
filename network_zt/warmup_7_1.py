import ipaddress

my_ip = "172.16.8.40"
prefix = 24

net = ipaddress.ip_network(f"{my_ip}/{prefix}", strict=False)
ip = ipaddress.ip_address(my_ip)

print("내 IP:", ip)
print("사설 IP 여부:", ip.is_private)
print("서브넷 마스크:", net.netmask)
print("네트워크 주소:", net.network_address)
print("브로드캐스트 주소:", net.broadcast_address)

other_ip = ipaddress.ip_address("172.16.8.50")
other_net = ipaddress.ip_network(f"{other_ip}/{prefix}", strict=False)

print("상대 IP:", other_ip)
print("같은 망 여부:", net == other_net)
