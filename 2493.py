# 탑
import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

ans = []
stack = []

for idx in range(N):
    while stack:
        if stack[-1][1] >= towers[idx]:
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([idx, towers[idx]])

print(*ans)