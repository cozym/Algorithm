# 사촌
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
nodes = list(int,input().split())
Tree = {}
sequenceK = 0
Q = deque()

parent = nodes[0]
depth = 0
Tree[nodes[0]] = [0,0]

sequence = 0
Q.append(nodes[0])
for idx in range(1,n):
    # parent = Q.popleft()
    while nodes[idx] == nodes[idx-1]+1:
        Tree[nodes[idx]] = depth
        Q.append(nodes[idx])
        idx += 1
    depth += 1
    Tree[nodes[idx]] = depth