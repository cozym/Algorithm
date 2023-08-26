# 사탕 게임
import sys

N = int(sys.stdin.readline())
A = []
columns = [[] for i in range(N)]

# 행
for i in range(N):
    row = sys.stdin.readline().rstrip()
    A.append([])
    for j in row:
        A[i].append(j)
    #rows.append(list(map(str,sys.stdin.readline().split(''))))
    #for j in range(N):   # 열 미리 구분저장
    #    columns[j].append(row[j])

# 두 원소 자리바꾸기
def Change_seat(r,c,isrow):
    if isrow:
        tmp = A[r][c]
        A[r][c] = A[r][c+1]
        A[r][c+1] = tmp
    else:
        tmp = A[r][c]
        A[r][c] = A[r+1][c]
        A[r+1][c] = tmp

# 가로, 세로로 같은 색 최대 개수 카운트
#def Count_max():


for k in range(N):
    for r in range(N-1):
        Change_seat(A[k][r],A[k][r+1],True)

        Change_seat(A[k][r],A[k][r+1],True)
    for c in range(N-1):
        Change_seat(A[c][k],A[c+1][k],False)

        Change_seat(A[c][k],A[c+1][k],False)


# for r in range(len(A)):
#     for e in range(len(A[r])):
#         print(A[r][e])

