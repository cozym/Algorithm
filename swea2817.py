# 부분 수열의 합
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def recur(idx, S):
    if S == K:
        global res
        res += 1
    if S >= K or idx == N:
        return
    recur(idx+1, S+e[idx])
    recur(idx+1, S)

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,K = map(int,input().split())
    e = list(map(int,input().split()))
    e.sort(reverse=True)
    res = 0

    recur(0,0)

    print('#{} {}'.format(test_case, res))
    # ///////////////////////////////////////////////////////////////////////////////////