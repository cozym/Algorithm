# 수열
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
temps = list(map(int,input().split()))
res = -1e9

## 슬라이딩 윈도우
# sequence_sum = []
# sequence_sum.append(sum(temps[:K]))
# for i in range(1,N-K+1):
#     sequence_sum.append(sequence_sum[i-1]-temps[i-1]+temps[i+K-1])

# print(max(sequence_sum))


## 누적합
prefixSum = [0]*(N+1) 
for i in range(1,N+1):
    prefixSum[i] = prefixSum[i-1]+temps[i-1]

for idx in range(K,N+1):
    res = max(res, prefixSum[idx]-prefixSum[idx-K])

print(res)