# 주몽
import sys
input = sys.stdin.readline

count = 0
N = int(input())
M = int(input())
nums = list(map(int,input().split()))

nums.sort()
s,e = 0,len(nums)-1

while s<e:
    plus = nums[s]+nums[e]
    if plus == M:
        count += 1
        e -= 1
    elif plus < M:
        s += 1
    else:
        e -= 1

print(count)