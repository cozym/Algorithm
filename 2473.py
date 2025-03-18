# 세 용액
import sys
input = sys.stdin.readline

N = int(input())
ph = list(map(int, input().split()))

ph.sort()

m = float('inf')
ans = []
for i in range(N-2):
    a = ph[i]
    b_i = i + 1
    c_i = N - 1
    while b_i < c_i:
        s = a + ph[b_i] + ph[c_i]
        if abs(s) <= abs(m):
            ans = [a, ph[b_i], ph[c_i]]
            m = s
        if s < 0:
            b_i += 1
        elif s > 0:
            c_i -= 1
        else:
            break

print(*ans)