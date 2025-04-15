# 뱀과 사다리 게임
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
connect = {}
for _ in range(N+M):
    x, y = map(int, input().split())
    connect[x] = y

visited = [True] * 101
visited[1] = False
q = deque([1])
cnt = 0
flag = False
while q:
    l = len(q)
    for _ in range(l):
        cur = q.popleft()
        if cur == 100:
            flag = True
            break
        for i in range(1,7):
            next = cur + i
            if next > 100:
                break
            if visited[next]:
                visited[next] = False
                if next in connect:
                    visited[connect[next]] = False
                    q.append(connect[next])
                else:
                    q.append(next)
    if flag:
        break
    cnt += 1

print(cnt)