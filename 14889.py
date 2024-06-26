# 스타트와 링크
import sys

N = int(sys.stdin.readline())
S = []
part_set = []
compare_value = -1

for i in range(N):
    S.append(list(map(int,sys.stdin.readline().split())))

# 재귀 부분집합 반복검사
def start_link(idx, pointer):
    if idx >= N/2:
        compare_team(part_set)
        return
    if pointer >= N:
        return
    part_set.append(pointer)
    start_link(idx+1,pointer+1)
    part_set.pop()
    start_link(idx,pointer+1)

# 집합 간 능력치 비교
def compare_team(part_set):
    global compare_value
    A_team = 0
    B_team = 0
    for i in range(N):
        if i in part_set:
            for j in part_set:
                A_team += S[i][j]
        else:
            for j in range(N):
                if j in part_set:
                    continue
                B_team += S[i][j]
    if compare_value == -1:
        compare_value = abs(A_team-B_team)
    if compare_value > abs(A_team-B_team):
        compare_value = abs(A_team-B_team)

start_link(0,0)
print(compare_value)