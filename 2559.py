# 수열
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
temps = list(map(int,input().split()))

sequence_sum = []
sequence_sum.append(sum(temps[:K]))
for i in range(1,N-K+1):
    sequence_sum.append(sequence_sum[i-1]-temps[i-1]+temps[i+K-1])

print(max(sequence_sum))