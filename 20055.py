# 컨베이어 벨트 위의 로봇
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().split())
A = deque(map(int, input().split()))
robot = [0] * n
robot = deque(robot)

step = 1
while True:
    A.appendleft(A.pop())   # 벨트 이동
    robot.appendleft(robot.pop())

    robot[-1] = 0   # 로봇 내리고
    for i in range(1, n):   # 로봇 이동
        if robot[n-i-1] == 1 and robot[n-i] == 0:   # 뒤부터
            if A[n-i] > 0:  # 내구도 검사
                robot[n-i-1] = 0
                robot[n-i] = 1
                A[n-i] -= 1
    robot[-1] = 0

    if A[0] > 0:    # 로봇 올리고
        robot[0] = 1
        A[0] -= 1

    if A.count(0) >= k:
        break

    step += 1

print(step)

# deque로 각 칸의 내구도 컨트롤
# 올리는 칸, 내리는 칸 고정해놓고 한쪽으로 밀기
# 로봇의 위치를 나타내는 큐로 뒤에서부터 한칸씩 밀기 (내구도, 범위 고려)
# 내구도 카운트