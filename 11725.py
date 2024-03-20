# 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
R = [[] for _ in range(N+1)]
res = [0 for _ in range(N+1)]
Q = deque()

for _ in range(N-1):
    l,r = map(int,input().split())
    R[l].append(r)
    R[r].append(l)

for node in R[1]:
    res[node] = 1
    Q.append(node)

while len(Q) != 0:
    current = Q.popleft()
    for node in R[current]:
        if res[node] == 0:
            res[node] = current
            Q.append(node)

for i in range(2,N+1):
    print(res[i])