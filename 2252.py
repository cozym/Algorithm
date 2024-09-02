# 줄 세우기
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
frontMeCnt = [0 for _ in range(N+1)]    # 진입차수 (내 앞에 몇명있는지)
behindMe = [[] for _ in range(N+1)]     # 내 바로 뒤에 누구누구 있는지 (직계 자식노드?)
q = deque()
ans = []
for _ in range(M):
    a,b = map(int,input().split())
    behindMe[a].append(b)
    frontMeCnt[b] += 1

# 진입차수 0 선출 (내 앞에 아무도 없으면 먼저 줄 세우기)
for idx in range(1,N+1):
    if frontMeCnt[idx] == 0:
        q.append(idx)

# 줄 세우며 직계 자식노드로 진입차수 빼주고 0인 경우 줄 세우기 반복
while(q):
    next = q.popleft()
    ans.append(next)
    for m in behindMe[next]:
        frontMeCnt[m] -= 1
        if frontMeCnt[m] == 0:
            q.append(m)

print(*ans)