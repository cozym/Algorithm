# 신입 사원
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    scores = []
    for _ in range(N):
        a, b = map(int, input().split())
        scores.append([a, b])
    scores = sorted(scores, key=lambda x:x[0])

    big = scores[0][1]
    cnt = 1
    for idx in range(1, N):
        if scores[idx][1] < big:
            cnt += 1
            big = scores[idx][1]

    print(cnt)

# 한 점수 기준 정렬

# 1 4
# 2 3
# 3 2
# 4 1
# 5 5

# 가장 많이 뽑을 수 있는 최대, 최소

# 1 4
# 2 5
# 3 6
# 4 2
# 5 7
# 6 1
# 7 3