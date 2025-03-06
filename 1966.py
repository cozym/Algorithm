# 프린터 큐
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    cnt = 0     # 인쇄 순서
    N, i = map(int, input().split())
    docs = deque(map(int, input().split()))
    ans = -1

    while True:
        current = docs.popleft()
        for d in docs:      # 더 높은 우선순위 검사
            if current < d:
                docs.append(current)
                break
        else:       # 없으면 인쇄
            cnt += 1
            if i == 0:
                ans = cnt
        
        if ans != -1:
            print(ans)
            break

        i -= 1
        if i < 0:
            i = len(docs) - 1