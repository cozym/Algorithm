# 링크와 스타트
import sys

N = int(sys.stdin.readline())
S = []
start = []
link = []
compare_value = -1

for i in range(N):
    S.append(list(map(int,sys.stdin.readline().split())))

# 재귀 부분집합 반복검사
def start_link(idx, pointer):
    if pointer >= N and (idx >= 1 or idx <= N//2):
        compare_team(start,link)
        return
    start.append(pointer)
    start_link(idx+1,pointer+1)
    start.pop()
    link.append(pointer)
    start_link(idx,pointer+1)
    link.pop()

#집합 간 능력치 비교
def compare_team(start, link):
    global compare_value     
    A_team = 0
    B_team = 0
    for i in start:
        for j in start:
            A_team += S[i][j]
    for l in link:
        for m in link:
            B_team += S[l][m]
    if compare_value == -1:
        compare_value = abs(A_team-B_team)
    if compare_value > abs(A_team-B_team):
        compare_value = abs(A_team-B_team)

start_link(0,0)
print(compare_value)