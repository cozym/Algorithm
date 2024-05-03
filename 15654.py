# N과 M (5)
import sys

N,M = map(int,sys.stdin.readline().split())

nums = list(map(int,sys.stdin.readline().split()))
p = [0 for i in range(M)]   # 매번 출력될 값 저장 공간
used = [False for i in range(N)]    # 사용 여부 체크

nums.sort()

def recursion(idx):
    if idx==M:
        print(*p)
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        p[idx] = nums[i]
        recursion(idx+1)
        used[i] = False 

recursion(0)