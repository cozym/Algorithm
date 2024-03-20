# N과 M (2)
import sys

N,M = map(int,sys.stdin.readline().split())

p = [0 for i in range(M)]
used = [False for i in range(N+1)]

# 재귀func(인덱스,N,M)
# 인덱스가 M과 같아지면 수열의 길이가 끝나므로 출력
# 함수로 들어갈때마다 N만큼 반복문을 돌리고 사용되지 않은 수를 used로 체크하여 사용
def recursion(idx,N,M):
    if idx==M:
        if p==sorted(p):
            print(*p)
        return
    for i in range(1,N+1):
        if used[i]:
            continue
        used[i] = True
        p[idx] = i
        recursion(idx+1,N,M)
        used[i] = False

recursion(0,N,M)