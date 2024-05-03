# N과 M (7)
import sys

N,M = map(int,sys.stdin.readline().split())

nums = list(map(int,sys.stdin.readline().split()))
p = [0 for i in range(M)]   # 매번 출력될 값 저장 공간

nums.sort()
# 재귀func(인덱스,N,M)
# 인덱스가 M과 같아지면 수열의 길이가 끝나므로 출력
# 중복 가능이므로 전부 출력
def recursion(idx):
    if idx==M:
        print(*p)
        return
    for i in range(N):
        p[idx] = nums[i]
        recursion(idx+1)

recursion(0)