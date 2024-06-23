# 소수의 자격
# 에라토스테네스
# A이상 B이하 소수 전처리
import sys
input = sys.stdin.readline

A,B,D = map(int,input().split())
primes = [True]*(B+1)
D = str(D)
res = 0

for i in range(2,B+1):
    if primes[i]:
        if i>B:
            break
        if A <= i and D in str(i):
            res += 1
        for j in range(i*2,B+1,i):
            primes[j] = False

print(res)