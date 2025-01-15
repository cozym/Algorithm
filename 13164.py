# 행복 유치원
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
diff = []

for i in range(N-1):
    diff.append(arr[i+1] - arr[i])

diff.sort(reverse=True)

print(sum(diff[K-1:]))