# 다음 순열
import sys
import itertools

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

# 마지막 수열일 경우 -1
if arr == sorted(arr,reverse=True):
    print(-1)
    exit(0)

line_value = arr[N-1]
line_index = 0
swap_idx = 1

# 뒤에서부터 시작하여 오름차순의 마지막 인덱스 i 탐색
for e in reversed(arr):
    if line_value > e:
        break
    line_value = e
    line_index += 1

# i~N중 arr[i]보다 큰 가장 작은 수의 인덱스 j를 탐색
for m in reversed(arr[-line_index:]):
    if m > arr[-line_index-1]:
        break
    swap_idx += 1

# i-1과 j swap
swap = arr[-line_index-1]
arr[-line_index-1] = arr[-swap_idx]
arr[-swap_idx] = swap

# i~N인덱스 뒤집어서 재결합
arr = arr[:-line_index] + list(reversed(arr[-line_index:]))
print(*arr)