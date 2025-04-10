# 순서쌍의 곱의 합
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
rest = sum(nums)

ans = 0
for i in nums:
    rest -= i
    ans += i*rest

print(ans)