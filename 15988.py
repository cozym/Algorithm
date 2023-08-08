# 1,2,3 더하기 3
import sys

# n[x] = n[x-1]+n[x-2]+n[x-3] / 1,2,3 사전 초기화ㅎ
n = [0 for i in range(1000001)]
n[1] = 1
n[2] = 2
n[3] = 4

for j in range(4,1000001):
    n[j] = (n[j-1]+n[j-2]+n[j-3])%1000000009

for t in range(int(sys.stdin.readline())):
    print(n[int(sys.stdin.readline())])