# LCA
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
R = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
parentInfo = {}
Q = deque()

for _ in range(N-1):
    n1,n2 = map(int,input().split())
    R[n1].append(n2)
    R[n2].append(n1)

Q.append(1)
visit[1] = True
parentInfo[1] = [0,0] # 루트 노드의 부모를 0으로 설정
depth = 1
while len(Q) != 0:
    cycle = len(Q)
    for idx in range(cycle):
        current = Q.popleft()
        for node in R[current]:
            if not visit[node]:
                parentInfo[node] = [current,depth]
                Q.append(node)
                visit[node] = True
    depth += 1

# 최소 공통 조상 탐색
def LCA(node1, node2):
    ancestor = []
    parent1 = node1
    parent2 = node2
    # if parent1 == parent2:
    #     print(parent1)
    #     return
    # elif parentInfo[parent1][0] == parent2:
    #     print(parent2)
    #     return
    # elif parent1 == parentInfo[parent2][0]:
    #     print(parent1)
    #     return
    while True:
        if parent1 == parent2:
            print(parent1)
            break
        # if parentInfo[parent1][0] == parentInfo[parent2][0]:
        #     print(parentInfo[parent1][0])
        #     break
        if parentInfo[parent1][1] >= parentInfo[parent2][1]:
            parent1 = parentInfo[parent1][0]
        else:
            parent2 = parentInfo[parent2][0]
    
    # parent = node2
    # while True:
    #     if parent == 0: # 조상이 루트 노드에 닿으면 스탑
    #         break
    #     ancestor.append(parent)
    #     parent = parentInfo[parent]
    # parent = node1
    # while True:
    #     if parent in ancestor:
    #         print(parent)
    #         break
    #     if parent == 0:
    #         break
    #     parent = parentInfo[parent]

for _ in range(int(input())):
    n1,n2 = map(int,input().split())
    LCA(n1,n2)