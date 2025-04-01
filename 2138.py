# 전구와 스위치
import sys
input = sys.stdin.readline

N = int(input())
cur = list(map(int, input().strip()))
goal = list(map(int, input().strip()))

def change(cur, idx):   # 스위치 상태변환
    for i in (idx-1, idx, idx+1):
        cur[i] = 0 if cur[i]==1 else 1
    return cur

def check(cur, cnt):
    for idx in range(1, N-1):
        if cur[idx-1] != goal[idx-1]:
            cnt += 1
            cur = change(cur, idx)
    if cur[N-1] != goal[N-1] and cur[N-2] != goal[N-2]:   # 마지막꺼 처리
        return cnt + 1
    elif cur[N-1] == goal[N-1] and cur[N-2] == goal[N-2]:
        return cnt
    else:
        return 100001

ans = check(cur[:], 0)
cur[0] = 0 if cur[0]==1 else 1
cur[1] = 0 if cur[1]==1 else 1
ans = min(ans, check(cur[:], 1))

print(ans if ans!=100001 else -1)

# 000
# 110
# 001
# 010