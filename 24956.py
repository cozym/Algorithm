# 나는 정말 휘파람을 못 불어

import sys
input = sys.stdin.readline

N = int(input())
e = [0]*(N+1)
h = 0
res = 0
S = input().rstrip()[::-1]

# 문자열을 뒤집어서 H가 컨트롤 할 수 있는 E의 개수를 누적합으로 쌓아가며 W를 만날 때 +해줌
for i in range(1,N+1):
    e[i] = e[i-1]   # E의 개수 누적
    if S[i-1] == 'E':
        e[i] += 1
    elif S[i-1] == 'H':
        h = (2**e[i] - e[i] - 1 + h) % 1000000007   # 해당 H위치에서 다룰 수 있는 E 카운트
    elif S[i-1] == 'W':
        res += h % 1000000007

print(res)


# > 8 - 3 - 1 = 4
# > 
# W A H E W H E E
# 1 1 1 1 2 2 2 2
# 0 0 1 1 1 2 2 2
# 0 0 0 1 1 1 2 3

# E E H W E H A W

# 1 2 2 2 3 3 3 3
# 0 0 1 1 1 2 2 2
# 0 0 0 1 1 1 1 2

# 0 1 1 1 4 4 4 4
# 0 0 1 1 1 5 5 5
# 0 0 1 1 1 2 2 2
# 0 0 0 1 1 1 1 