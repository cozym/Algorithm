# 풍선 터트리기
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

visited = [True] * N
ans = [1]

step = arr[0]
visited[0] = False
idx = 0
while True in visited:
    cnt = 0
    mark = 1
    if step < 0:    # 음수면 뒤로
        step *= -1
        mark = -1
    while cnt < step:
        idx += mark
        idx %= N
        if visited[idx]:
            cnt += 1
    visited[idx] = False
    step = arr[idx]
    ans.append(idx + 1)

print(*ans)