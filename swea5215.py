# 햄버거 다이어트
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def recur(idx, flavor, calories):
    if calories > L:
        return
    if idx == N:
        global res
        res = max(res, flavor)
        return
    recur(idx+1, flavor, calories)
    recur(idx+1, flavor + info[idx][0], calories + info[idx][1])

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,L = map(int,input().split())
    info = []
    res = 0
    for _ in range(N):
        f,c = map(int,input().split())
        info.append((f,c))

    recur(0,0,0)

    print('#{} {}'.format(test_case,res))
    # ///////////////////////////////////////////////////////////////////////////////////