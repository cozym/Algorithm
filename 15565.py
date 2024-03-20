# 귀여운 라이언
import sys
#from queue import Queue
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
dolls = list(map(int,input().split()))

res = N+10
rion_cnt = 0
rion_pointer = deque()

for idx in range(N):
    if dolls[idx] == 1:
        rion_pointer.append(idx)
        rion_cnt += 1
    if rion_cnt == K:
        first = rion_pointer.popleft()
        if res > idx-first+1:
            res = idx-first+1
        rion_cnt -= 1
    
if res==N+10:
    print(-1)
else:
    print(res)