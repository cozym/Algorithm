# 부분수열의 합
import sys

N,S = map(int, sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
sets_sum = 0
pointer = 0
count = 0

# 주어진 수열의 i번째 값을 더하는 경우와 더하지 않는 경우 재귀 검토
def part_sequence(sets_sum,pointer):
    if pointer >= N:
        return
    sets_sum += nums[pointer]
    if sets_sum == S:
        global count
        count += 1
    part_sequence(sets_sum,pointer+1)
    part_sequence(sets_sum-nums[pointer],pointer+1)

part_sequence(0,0)
print(count)