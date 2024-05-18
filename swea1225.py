# 암호생성기
from collections import deque
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    t = int(input())
    password = deque(map(int,input().split()))
    m = 1
    while True:
        tmp = password.popleft()
        if tmp - m <= 0:
            password.append(0)
            break
        password.append(tmp - m)
        m += 1
        if m == 6:
            m = 1

    print('#{} '.format(test_case),end='')
    for i in password:
        print(i,end=' ')
    else:
        print()
    # ///////////////////////////////////////////////////////////////////////////////////