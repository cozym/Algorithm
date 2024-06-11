# 소수의 연속합
import sys
input = sys.stdin.readline

N = int(input())
filter = [True for _ in range(4000001)]
primes = []
res = 0

# 에라토스테네스 체
for i in range(2,4000001):
    if filter[i]:
        primes.append(i)
        for j in range(i+i,4000001,i):
            filter[j] = False

l,r = 0,0
s = primes[0]
L = len(primes)
while r < L:
    if s < N:
        r += 1
        if r == L:
            break
        s += primes[r]
    elif s == N:
        res += 1
        s -= primes[l]
        l += 1
    else:
        s -= primes[l]
        l += 1
        
print(res)