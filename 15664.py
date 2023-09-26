# N과 M (10)
import sys

N,M = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
used_idx = [False for i in range(N)]    # 사용된 인덱스 체크 용도
p = [0 for i in range(M)]  # 출력용

nums.sort() # 입력받은 수 정렬 > 사전순 출력 목적

def recursion_sequence(idx,N,M):
    used_num = []   # 같은 인덱스에 중복된 수 체크 용도
    if idx==M:
        print(*p)
        return
    for i in range(N):
        if used_idx[i]:
            continue
        if nums[i] in used_num:
            continue
        used_num.append(nums[i])
        used_idx[i] = True
        p[idx] = nums[i]
        recursion_sequence(idx+1,N,M)
        used_idx[i] = False

recursion_sequence(0,N,M)
