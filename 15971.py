# 두 로봇
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N,a,b = map(int,input().split())
R = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
costBetweenab = []
res = 0
for _ in range(N-1):
    x,y,cost = map(int,input().split())
    R[x].append((y,cost))
    R[y].append((x,cost))

def dfs(node):
    visited[node] = True
    # global res
    if node == b:
        if costBetweenab:
            print(sum(costBetweenab)-max(costBetweenab))
        else:
            print(0)
        return

    for next_node,cost in R[node]:
        if not visited[next_node]:
            # visited[next_node] = True
            # res += cost
            costBetweenab.append(cost)
            dfs(next_node)
            costBetweenab.remove(cost)
            # visited[next_node] = False

dfs(a)