# LCA
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
R = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
parentInfo = [0]*(N+1)
depths = [0]*(N+1)
Q = deque()

for _ in range(N-1):
    n1,n2 = map(int,input().split())
    R[n1].append(n2)
    R[n2].append(n1)

Q.append(1)
visit[1] = True
parentInfo[1] = 0 # 루트 노드의 부모를 0으로 설정
depths[1] = 0
depth = 1
while len(Q) != 0:
    cycle = len(Q)
    for idx in range(cycle):
        current = Q.popleft()
        for node in R[current]:
            if not visit[node]:
                parentInfo[node] = current  # 각 노드의 부모와 깊이 정보
                depths[node] = depth
                Q.append(node)
                visit[node] = True
    depth += 1

# 최소 공통 조상 탐색
def LCA(node1, node2):
    parent1 = node1
    parent2 = node2
    while depths[parent1] != depths[parent2]:
        if depths[parent1] >= depths[parent2]:    # 깊이 맞추기
            parent1 = parentInfo[parent1]
        else:
            parent2 = parentInfo[parent2]
    while parent1 != parent2:   # 공통 조상 찾기
        parent1 = parentInfo[parent1]
        parent2 = parentInfo[parent2]
    print(parent1)

for _ in range(int(input())):
    n1,n2 = map(int,input().split())
    LCA(n1,n2)