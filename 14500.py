# 테트로미노
import sys

N,M = map(int,sys.stdin.readline().split())
pad = []

for i in range(N):
    pad.append(list(map(int,sys.stdin.readline().split())))

# 각 도형의 회전, 대칭한 모든 경우의 가로/세로와 무효좌표 저장
a = [[1,4],[4,1]] # 2경우
b = [[2,2]] # 1경우
c = [[3,2,[0,1],[1,1]],[2,3,[1,1],[1,2]],[3,2,[1,0],[2,0]],[2,3,[0,0],[0,1]],[3,2,[0,0],[1,0]],[2,3,[0,1],[0,2]],[3,2,[1,1],[2,1]],[2,3,[1,0],[1,1]]] # 8경우
d = [[3,2,[0,1],[2,0]],[2,3,[0,0],[1,2]],[3,2,[0,0],[2,1]],[2,3,[0,2],[1,0]]]    # 4경우
e = [[2,3,[0,0],[0,2]],[3,2,[0,0],[2,0]],[2,3,[1,0],[1,2]],[3,2,[0,1],[2,1]]]   # 4경우
res = 0

def check(kinds,res):
    for i in kinds: # 도형의 회전, 대칭한 경우를 하나씩 검토
        for r in range(N-i[0]+1):   #시작 행 좌표
            for c in range(M-i[1]+1):   #시작 열 좌표
                s = 0
                for a in range(i[0]):   #시작 좌표에서 범위만큼 검토
                    s += sum(pad[r+a][c:c+i[1]])
                for minus in range(2,len(i)): #무효 좌표 빼주기
                    s -= pad[r+i[minus][0]][c+i[minus][1]]
                if s > res:
                    res = s
    return res

# 좌측 상단을 시작좌표로 하여 가로*세로 범위의 합 - 무효좌표를 검토
res = check(a,res)
res = check(b,res)
res = check(c,res)
res = check(d,res)
res = check(e,res)

print(res)