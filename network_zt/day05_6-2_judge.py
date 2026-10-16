
# 3개 회선의 ping 결과 10번씩 (단위: ms). None은 응답이 없었던 것(손실)이다
LINES = {
    "회선 A": [22, 21, 23, 22, 21, 22, 23, 22, 21, 22],
    "회선 B": [18, 19, 95, 17, 18, 110, 19, 18, 92, 17],
    "회선 C": [40, 41, None, 42, 40, None, 41, 43, None, 40],
}

# 화상회의에 쓸 수 있는 기준
MAX_DELAY = 150
MAX_JITTER = 30
MAX_LOSS = 1


def measure(data):
    # 1. 응답을 받은 값만 got 리스트에 모은다
    got = []
    for v in data:
        if v != None:
            got.append(v)

    # 2. 평균 지연
    delay = sum(got) / len(got)

    # 3. 지터
    total = 0
    for i in range(1, len(got)):
        total = total + abs(got[i] - got[i - 1])
    jitter = total / (len(got) - 1)

    # 4. 손실률
    loss = (len(data) - len(got)) / len(data) * 100

    return delay, jitter, loss


for name in LINES:
    delay, jitter, loss = measure(LINES[name])

    # 5. 세 기준을 모두 지키면 True
    ok = (
        delay <= MAX_DELAY
        and jitter <= MAX_JITTER
        and loss <= MAX_LOSS
    )

    # 6. 어느 기준에 걸렸는지 확인
    reasons = []
    if delay > MAX_DELAY:
        reasons.append("지연")
    if jitter > MAX_JITTER:
        reasons.append("지터")
    if loss > MAX_LOSS:
        reasons.append("손실")

    # 7. 결과 출력
    if ok:
        print(name, "→ 적합")
    else:
        print(name, "→ 부적합 (걸린 기준:", ", ".join(reasons) + ")")
