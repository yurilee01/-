RULES = [
    (1, "outside", "DMZ", 443, "permit"),
    (2, "DMZ", "inside", 445, "permit"),
]

def default_policy(src, dst):
    if src == dst:
        return "permit"
    if src == "inside":
        return "permit"
    if dst == "outside":
        return "permit"
    return "deny"

def match_rule(rule, src, dst, port):
    no, r_src, r_dst, r_port, action = rule
    return r_src == src and r_dst == dst and r_port == port

def judge(src, dst, port):
    for rule in RULES:
        if match_rule(rule, src, dst, port):
            return rule[4], rule[0]
    return default_policy(src, dst), 0

def allowed_ports(src, dst, ports):
    result = []
    for port in ports:
        action, no = judge(src, dst, port)
        if action == "permit":
            result.append(port)
    return result

PORTS = [22, 80, 443, 445, 3389]
print(allowed_ports("outside", "DMZ", PORTS))
print(allowed_ports("DMZ", "inside", PORTS))
print(allowed_ports("inside", "DMZ", PORTS))
print(allowed_ports("outside", "inside", PORTS))
