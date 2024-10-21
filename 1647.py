# 도시 분할 계획
import sys
input = sys.stdin.readline

# 부모가 있으면 반복 탐색하여 최상위 부모를 반환
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a,b):
    a = find(a)  # 조상찾기
    b = find(b)
    # 작은놈을 조상으로 하여 합치기
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
R = []
res = 0
expensive_road = 0

for _ in range(M):
    A,B,C = map(int, input().split())
    R.append((A,B,C))

R.sort(key = lambda x:x[2])

# 크루스칼
for road in R:
    if find(road[0]) != find(road[1]):
        union(road[0], road[1])
        res += road[2]
        expensive_road = max(expensive_road, road[2])

print(res - expensive_road)