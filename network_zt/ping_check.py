
LIMIT = 100  # 이 값(ms)을 넘으면 느리다고 본다

# 미리 채워 둔 줄입니다. 고치지 않습니다
results = [
    {"target": "8.8.8.8", "ms": 34},
    {"target": "1.1.1.1", "ms": 120},
    {"target": "192.0.2.1", "ms": None},
]

for r in results:
    # 1. 응답이 없으면 실패
    if r["ms"] is None:
        print(f"[실패] {r['target']} 응답 없음")

    # 2. 응답 시간이 100ms보다 크면 느림
    elif r["ms"] > LIMIT:
        print(f"[느림] {r['target']} {r['ms']}ms")

    # 3. 나머지는 정상
    else:
        print(f"[정상] {r['target']} {r['ms']}ms")
