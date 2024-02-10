import sys
input = sys.stdin.readline

max = 100000

each = [0] * (max+1)
prefixSum = [0] * (max+1)

for i in range(1, max+1):
    j = 1
    while i * j <= max:
        each[i*j] += i # 2*j에 해당하는 값들은 2를 무조건 약수로 가지기 때문에 2를 더해준다
        j += 1
    prefixSum[i] = prefixSum[i-1] + each[i]

t = int(input())

for _ in range(t):
    n = int(input())
    print(prefixSum[n])