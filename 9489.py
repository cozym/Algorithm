# 사촌
import sys
from collections import deque
input = sys.stdin.readline

Q = deque()

while True:
    n,k = map(int,input().split())
    if n == 0 and k == 0:
        break
    nodes = list(map(int,input().split()))
    Tree = {}
    parentInfo = {}
    sequenceK = 0
    depth = 0

    # 조건에 맞는 트리 형성, 부모 정보 저장 추가
    Q.clear()
    Q.append(nodes[0])
    Tree[nodes[0]] = []
    for idx in range(1,n):
        Tree[nodes[idx]] = []
        if nodes[idx] != nodes[idx-1]+1:
            parent = Q.popleft()
        Tree[parent].append(nodes[idx])
        parentInfo[nodes[idx]] = parent
        Q.append(nodes[idx])

    # k의 사촌 수 판단
    Q.clear()
    if k == nodes[0]: # k가 루트 노드일 떄 예외
        print(0)
        continue
    elif parentInfo[k] == nodes[0]: # k가 루트 노드의 자식일 때 예외
        print(0)
        continue
    Q.append(parentInfo[parentInfo[k]])
    while len(Q) != 0:
        cycle = len(Q)
        if sequenceK != 0:
            depth = cycle
            break
        for idx in range(cycle):
            currentNode = Q.popleft()
            if len(Tree[currentNode]) != 0:
                for node in Tree[currentNode]:
                    Q.append(node)
                    if node == k:
                        sequenceK = len(Tree[currentNode])

    print(depth - sequenceK)