# SW Expert Academy 파리 퇴치
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    area = []
    N,M = map(int,input().split())
    for _ in range(N):
        area.append(list(map(int,input().split())))
    res = 0

    for x in range(N-M+1):
        for y in range(N-M+1):
            s = 0
            for r in range(x,x+M):
                s += sum(area[r][y:y+M])
            res = max(res, s)
    print("#{} {}".format(test_case,res))
    # ///////////////////////////////////////////////////////////////////////////////////