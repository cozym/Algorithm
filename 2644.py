# 촌수 계산
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a,b = map(int,input().split())
R = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
res = 0
isRelative = False

for _ in range(int(input())):
    x,y = map(int,input().split())
    R[x].append(y)
    R[y].append(x)

def bfs(node):
    q = deque()
    q.append(node)
    global res, isRelative
    
    while q:
        L = len(q)
        res += 1
        for i in range(L):
            current = q.popleft()
            for next_node in R[current]:
                if next_node == b:
                    isRelative = True
                    return
                if visited[next_node]:
                    continue
                visited[next_node] = True
                q.append(next_node)

bfs(a)

print(res if isRelative else -1)