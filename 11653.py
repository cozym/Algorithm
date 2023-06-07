# 소인수분해
import sys

N = int(sys.stdin.readline())
Prime_nums = []
Primes = [True for i in range(10000001)]
k=0

for i in range(2,int(10000001**0.5)+1):
    if Primes[i]:
        Prime_nums.append(i)
        for j in range(i*2,10000001,i):
            if Primes[j]:
                Primes[j] = False

while True:
    if N==1:
        break
    if Primes[N]:
        print(N)
        break
    elif N%Prime_nums[k]==0:
        print(Prime_nums[k])
        N //= Prime_nums[k]
    else:
        k+=1