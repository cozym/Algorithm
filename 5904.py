# Moo 게임
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

seq, k = 3, 0
while seq < N:
    k += 1
    seq = seq * 2 + (k + 3)

def recur(seq, mid, n):
    left = (seq - mid) // 2
    if n <= left:
        return recur(left, mid - 1, n)
    elif n > left + mid:
        return recur(left, mid - 1, n - left - mid)
    else:
        if n - left - 1 == 0:
            return 'm'
        else:
            return 'o'

ans = recur(seq, k+3, N)
print(ans)