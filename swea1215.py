# 회문
T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    pad = []
    for i in range(8):
        line = input()
        pad.append([])
        for s in line:
            pad[i].append(s)
            
    res = 0
    for i in range(8):
        for j in range(9-n):
            r = []
            c = []
            for idx in range(n):
                r.append(pad[i][j+idx])
                c.append(pad[j+idx][i])
            if r == list(reversed(r)):
                res += 1
            if c == list(reversed(c)):
                res += 1

    print('#{} {}'.format(test_case,res))
    # ///////////////////////////////////////////////////////////////////////////////////