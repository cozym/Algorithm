# 테트로미노
import sys

r,c = map(int,sys.stdin.readline().split())
pad = []

for i in range(r):
    pad.append(list(map(int,sys.stdin.readline().split())))

# 각 도형의 회전, 대칭한 모든 경우의 가로/세로와 무효좌표 저장
a = [[1,4]] # 4경우
b = [[2,2]] # 1경우
c = [[3,2,(0,1)]] # 8경우
d = [[2,2,]]    # 4경우
e = [[2,3]] # 4경우

# 좌측 상단을 시작좌표로 하여 가로*세로 범위의 합 - 무효좌표를 검토
for i in range(r):

#print(pad)