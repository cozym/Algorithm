# 트리의 지름
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
R = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
endNodes = []
res = 0
for _ in range(n-1):
    a,b,cost = map(int,input().split())
    R[a].append((b,cost))
    R[b].append((a,cost))

# 종단 노드들 탐색
def searchEndNodes(node):
    visited[node] = True
    isEndNode = True
    for nextNode, nextCost in R[node]:
        if visited[nextNode]:
            continue
        isEndNode = False
        searchEndNodes(nextNode)

    if isEndNode:
        endNodes.append(node)

searchEndNodes(1)

# 시작 노드부터 다른 종단 노드까지의 길이를 측정하고 max를 저장
def getMaxDistance(node, depth):
    global res
    visited[node] = True
    res = max(res, depth)
    for nextNode, nextCost in R[node]:
        if visited[nextNode]:
            continue
        getMaxDistance(nextNode, depth+nextCost)

# 미리 구해둔 종단 노드들로만 탐색하여 최적화
for startNode in endNodes:
    visited = [False for _ in range(n+1)]
    getMaxDistance(startNode, 0)

print(res)