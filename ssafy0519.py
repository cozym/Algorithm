T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def dfs(depth):
    for i in range(N+1):
        if False in read[i]:
            break
    else:
        return

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    R = [[] for _ in range(N+1)]
    read = [[False]*(N+1) for _ in range(N+1)]
    res = 0
    for _ in range(2):
        line = list(map(int,input().split()))
        for i in range(1,N+1):
            R[i].append(line[i-1])
            read[i][line[i-1]] = True
        
    print('#{} {}'.format(test_case, 2))
    # ///////////////////////////////////////////////////////////////////////////////////