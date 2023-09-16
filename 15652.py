# N과 M (4)
import sys

N,M = map(int,sys.stdin.readline().split())

p = [0 for i in range(M)]
used = [False for i in range(N+1)]

# 재귀func(인덱스,N,M)
# 인덱스가 M과 같아지면 수열의 길이가 끝나므로 출력
# start변수를 통해 다음 인덱스에 올 수 있는 가장 작은 값을 제한해준다
def recursion(idx,N,M,start):
    if idx==M:
        print(*p)
        return
    for i in range(start,N+1):
        p[idx] = i
        recursion(idx+1,N,M,i)

recursion(0,N,M,1)