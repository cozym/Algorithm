# 트리와 쿼리
import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N,R,Q = map(int,input().split())
Rel = [[] for _ in range(N+1)]
Tree = [[] for _ in range(N+1)]
visit = [False]*(N+1)
q = deque()
subTree = [0 for _ in range(N+1)]

# 노드 인접리스트 생성
for _ in range(N-1):
    n1,n2 = map(int,input().split())
    Rel[n1].append(n2)
    Rel[n2].append(n1)

# BFS로 트리의 부모자식 관계 형성
q.append(R)
visit[R] = True
while len(q) != 0:
    current = q.popleft()
    for node in Rel[current]:
        if visit[node] == False:
            Tree[current].append(node)
            visit[node] = True
            q.append(node)

# DFS와 DP로 서브트리의 정점 수 저장
def DFS(treeNode):
    for node in Tree[treeNode]:
        if subTree[node] == 0:
            DFS(node)
        subTree[treeNode] += subTree[node]
    subTree[treeNode] += 1

for idx in range(1,N+1):
    if subTree[idx] == 0:
        DFS(idx)

# 출력
for _ in range(Q):
    print(subTree[int(input())])