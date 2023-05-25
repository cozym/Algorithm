# 골드바흐 파티션 17103
import sys

r = int(sys.stdin.readline())
Primes = [True for t in range(1000001)]

# 에라토스테네스의 채
for k in range(2,int(1000000**0.5)+1):
    if Primes[k]:
        for j in range(k*2, 1000001, k):
            Primes[j] = False

for i in range(r):
    N = int(sys.stdin.readline())
    count = 0
    for j in range(2,N//2+1):
        if Primes[j] and Primes[N-j]:
            count+=1
    print(count)