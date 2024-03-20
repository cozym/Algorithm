# N과 M (9)
import sys

N,M = map(int,sys.stdin.readline().split())

nums = list(map(int,sys.stdin.readline().split()))
p = [0 for i in range(M)]   # 매번 출력될 값 저장 공간
used = [0 for i in range(N)]
already = []

nums.sort()
# 재귀func(인덱스,N,M)
# 인덱스가 M과 같아지면 수열의 길이가 끝나므로 출력
# 
def recursion(idx,N,M):
    if idx==M:
        if p not in already:
            print(p)
            already.append(p)
        print(already)
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        p[idx] = nums[i]
        recursion(idx+1,N,M)
        used[i] = False

recursion(0,N,M)