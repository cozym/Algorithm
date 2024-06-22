# 2로 몇 번 나누어질까
import sys
input = sys.stdin.readline

#1 2 3 4 5 6 7 8
#  1   1   1   1 > 8//2 > ~8까지 2로 나누어지는 수가 4개
#      1       1 > 8//2**2 > ~8까지 2**2로 나누어지는 수가 2개
#              1 > 8//2**3 > ~8까지 2**3으로 나누어지는 수가 1개
# 위에서부터 cnt[n] = cnt[n] - cnt[n+1]

#N = 9
#1 2 3 4 5 6 7 8 9
#1 1 1 1 1 1 1 1 1 > 9//1
#  1   1   1   1   > 9//2
#      1       1   > 9//4

A,B = map(int,input().split())

def getSumofBigPrimes(N):
    toN = N
    div = 2
    while N//div:
        prev = div//2
        toN -= (N//div)*prev
        toN += (N//div)*div
        div *= 2
    return toN

print(getSumofBigPrimes(B)-getSumofBigPrimes(A-1))