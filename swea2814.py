# 최장 경로
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def dfs(node, depth):
    global res
    res = max(res, depth)
    visit[node] = True
    for n in R[node]:
        if visit[n]:
            continue
        dfs(n,depth+1)
    visit[node] = False
 
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,M = map(int,input().split())
    R = [[] for _ in range(N+1)]
    visit = [False for _ in range(N+1)]
    res = 0
    for _ in range(M):
        e1,e2 = map(int,input().split())
        R[e1].append(e2)
        R[e2].append(e1)
     
    for idx in range(1,N+1):
        dfs(idx,1)
 
    print('#{} {}'.format(test_case, res))
    # ///////////////////////////////////////////////////////////////////////////////////