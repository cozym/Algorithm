# 원재의 메모리 복구하기
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    now = '0'
    res = 0
    goal = input()
    for c in goal:
        if c == now:
            continue
        res += 1
        now = c
    print('#{} {}'.format(test_case,res))
    # ///////////////////////////////////////////////////////////////////////////////////