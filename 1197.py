# 최소 스패닝 트리
import sys
input = sys.stdin.readline

# 크루스칼 & union find
V,E = map(int,input().split())
nodes = [True for _ in range(V+1)]
edges = []
roots = []
res = 0

# 싸이클 검사를 위한 루트노드 생성
roots.append(0)
for idx in range(V):
    roots.append(idx+1)

for _ in range(E):
    A,B,C = map(int,input().split())
    edges.append((A,B,C))

edges.sort(key=lambda x:x[2])

# 조상 노드 찾기, 업데이트
def find(r):
    if r != roots[r]:
        roots[r] = find(roots[r])
    return roots[r]

# 조상 노드 비교 => 싸이클 검사
def union(a,b):
    if nodes[a] or nodes[b]:
        a_root = find(a)
        b_root = find(b)
        if a_root != b_root:
            if a_root > b_root:
                roots[a_root] = b_root
            else:
                roots[b_root] = a_root
            return True
    return False    
    
for a,b,cost in edges:
    if union(a,b):
        res += cost

print(res)