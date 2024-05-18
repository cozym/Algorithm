# Magnetic
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    res = 0
    table = []
    for _ in range(N):
        table.append(list(map(int,input().split())))
    
    for c in range(N):
        now = 2
        cnt = 0
        for r in range(N):
            if table[r][c] != 0 and table[r][c] != now:
                cnt += 1
                now = table[r][c]
        res += cnt//2

    print('#{} {}'.format(test_case, res))
    # ///////////////////////////////////////////////////////////////////////////////////