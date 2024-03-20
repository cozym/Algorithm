# 트리
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nodes = list(map(int,input().split()))
removeNode = int(input())
Tree = [[] for _ in range(N)]
Q = deque()
leafNode = 0

for child,parent in enumerate(nodes):
    if parent == -1:
        root = child
    elif child == removeNode:
        continue
    else:
        Tree[parent].append(child)

Q.append(root)
while len(Q) != 0:
    currentNode = Q.popleft()
    if len(Tree[currentNode]) == 0:
        leafNode += 1
    for node in Tree[currentNode]:
        Q.append(node)

if removeNode == root:
    print(0)
else:
    print(leafNode)