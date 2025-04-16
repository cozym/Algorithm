# 잃어버린 괄호
import sys
input = sys.stdin.readline

s = input().rstrip().split('-')

nums = []
for part in s:
    nums.append(sum(map(int, part.split('+'))))

print(nums[0]-sum(nums[1:]))