mac_table = {}  # 빈 MAC 주소 표를 만든다
mac_table["AA"] = 1  # AA가 1번 포트에 있다고 기록한다
dest = "BB"  # 목적지 MAC 주소는 BB

if dest in mac_table:  # 목적지가 표에 있는지 확인한다
    print("포트", mac_table[dest], "로만")
else:
    print("모든 포트로")
