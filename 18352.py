# 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

N,M,K,X = map(int,input().split())
R = [[] for _ in range(N+1)]
visited = [True]*(N+1)
ans = []
for _ in range(M):
    A,B = map(int,input().split())
    R[A].append(B)

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = False
    d = -1

    while q:
        L = len(q)
        d += 1
        for idx in range(L):
            current_node = q.popleft()
            if d == K:  # 출발 노드부터 최단거리로 K만큼 이동했을 때
                ans.append(current_node)
            for next_node in R[current_node]:
                if visited[next_node]:
                    visited[next_node] = False
                    q.append(next_node)

bfs(X)

ans.sort()

if ans:
    for city in ans:
        print(city)
else:
    print(-1)