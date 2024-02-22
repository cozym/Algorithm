# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int,input().split())

R = [[] for i in range(N+1)]
visit = [False for i in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    R[x].append(y)
    R[y].append(x)

for i in range(1,N+1):
    R[i].sort()
    print(R[i])

def DFS(node):
    visit[node] = True
    print(node,end=" ")
    for nextNode in R[node]:
        if visit[nextNode] == False:
            DFS(nextNode)

def BFS(node):
    Q = deque()
    Q.append(node)
    visit[node] = True
    while len(Q) != 0:
        currentNode = Q.popleft()
        print(currentNode,end=" ")
        for nextNode in R[currentNode]:
            if visit[nextNode] == False:
                Q.append(nextNode)
                visit[nextNode] = True

DFS(V)

visit = [False for i in range(N+1)]
print()

# for idx in range(1,N+1):
#     if visit[idx] == False:
BFS(V)