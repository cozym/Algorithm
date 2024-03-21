# 나무 위의 빗물
# 고인물 / 리프노드 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N,W = map(int,input().split())
R = [[] for _ in range(N+1)]
visit = [False]*(N+1)
leaf = 0

for _ in range(N-1):
    U,V = map(int,input().split())
    R[U].append(V)
    R[V].append(U)

def countLeaf(node):
    cnt = 0
    visit[node] = True
    for child in R[node]:
        if not visit[child]:
            cnt += 1
            countLeaf(child)
    if cnt == 0:
        global leaf
        leaf += 1
    
countLeaf(1)
print(W/leaf)