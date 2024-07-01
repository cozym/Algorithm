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
    if node == b:   # 방문한 노드가 반대쪽 로봇의 위치라면
        if costBetweenab:   # 로봇 사이의 코스트가 존재한다면
            print(sum(costBetweenab)-max(costBetweenab))
        else:   # 로봇이 붙어있는 경우
            print(0)
        return

    for next_node,cost in R[node]:
        if not visited[next_node]:
            costBetweenab.append(cost)
            dfs(next_node)
            costBetweenab.remove(cost)  # 진입했지만 반대쪽 로봇을 만나지 못했다면 cost 제거

dfs(a)