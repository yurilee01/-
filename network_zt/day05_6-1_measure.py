# 3개 회선의 ping 결과 10번씩 (단위: ms). None은 응답이 없었던 것(손실)이다
LINES = {
    "회선 A": [22, 21, 23, 22, 21, 22, 23, 22, 21, 22],
    "회선 B": [18, 19, 95, 17, 18, 110, 19, 18, 92, 17],
    "회선 C": [40, 41, None, 42, 40, None, 41, 43, None, 40],
}

def jitter(got):
    """
    이웃한 응답 시간의 차이를 평균 내어 지터를 구하는 함수이다.
    입력: 응답을 받은 시간 값들의 리스트 got
    리턴: 이웃한 응답 시간 차이의 평균값
    """
    total = 0
    for i in range(1, len(got)):
        total += abs(got[i] - got[i - 1])
    return total / (len(got) - 1)

def measure(name, data):
    got = []
    for v in data:
        if v != None:
            got.append(v)

    delay = sum(got) / len(got)
    jitter_value = jitter(got)
    loss = (len(data) - len(got)) / len(data) * 100

    print(name, "| 지연", round(delay, 1), "ms | 지터", round(jitter_value, 1), "ms | 손실", round(loss), "%")

for name in LINES:
    measure(name, LINES[name])