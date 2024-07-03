# 숫자 고르기
import sys
input = sys.stdin.readline

N = int(input())
R = [0 for _ in range(N+1)]
visitedStart = [False for _ in range(N+1)]
resCnt = 0
for up in range(1,N+1):
    R[up] = int(input())

def dfs(node):
    visited[node] = True
    first.append(node)
    second.append(R[node])
    if not visited[R[node]]:
        dfs(R[node])
    else:
        first.sort()
        second.sort()
        if first == second:
            global resCnt
            for e in first:
                resCnt += 1
                visitedStart[e] = True

for idx in range(1,N+1):
    visited = [False for _ in range(N+1)]
    first = []
    second = []
    if not visitedStart[idx]:
        dfs(idx)

print(resCnt)
for i in range(1,N+1):
    if visitedStart[i]:
        print(i)