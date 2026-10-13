my_ip = "192.168.100.251"
parts = my_ip.split(".")

for part in parts:
    number = int(part)
    bits = format(number, "08b")
    print(part, bits)