# 이전 순열
import sys
import itertools

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

# 첫 수열일 경우 -1
if arr == sorted(arr):
    print(-1)
    exit(0)

line_value = arr[N-1]
line_index = 0
swap_idx = 1

# 뒤에서부터 시작하여 내림차순의 마지막 인덱스 i 탐색
for e in reversed(arr):
    if line_value < e:
        break
    line_value = e
    line_index += 1

# i~N중 arr[i]보다 작은 가장 큰 수의 인덱스 j를 탐색
for m in arr[-1:-line_index-1:-1]:
    if m < arr[-line_index-1]:
        break
    swap_idx += 1

# i-1과 j swap
swap = arr[-line_index-1]
arr[-line_index-1] = arr[-swap_idx]
arr[-swap_idx] = swap

# i~N인덱스 뒤집어서 재결합
arr = arr[:-line_index] + list(reversed(arr[-line_index:]))
print(*arr)