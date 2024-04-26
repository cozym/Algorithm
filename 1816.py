# 암호 키
import sys
input = sys.stdin.readline

isPrime = [False for _ in range(1000001)]
primes = []
for i in range(2, 1000001):
    if not isPrime[i]:
        primes.append(i)
    for j in range(i*2, 1000001, i):
        isPrime[j] = True

N = int(input())

for _ in range(N):
    k = int(input())
    for p in primes:
        if k%p==0:
            print("NO")
            break
    else:
        print("YES")