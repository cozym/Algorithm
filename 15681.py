# 트리와 쿼리
import sys
from collections import deque
input = sys.stdin.readline

N,R,Q = map(int,input().split())
Rel = [[] for _ in range(N+1)]
Tree = [[] for _ in range(N+1)]
visit = [False]*(N+1)
q = deque()

for _ in range(N-1):
    n1,n2 = map(int,input().split())
    Rel[n1].append(n2)
    Rel[n2].append(n1)

q.append(R)
visit[R] = True
while len(q) != 0:
    current = q.popleft()
    for node in Rel[current]:
        if visit[node] == False:
            Tree[current].append(node)
            visit[node] = True
            q.append(node)

for _ in range(Q):
    cnt = 0
    #visit = [False]*(N+1)
    q.clear()
    q.append(int(input()))
    while len(q) != 0:
        current = q.popleft()
        for node in Tree[current]:
            q.append(node)
            cnt += 1
    print(cnt+1)