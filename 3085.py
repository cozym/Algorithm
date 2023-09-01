# 사탕 게임
import sys

N = int(sys.stdin.readline())
A = []
columns = [[] for i in range(N)]
res = 0

# 행
for i in range(N):
    row = sys.stdin.readline().rstrip()
    A.append([])
    for j in row:
        A[i].append(j)

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
def Count_max(res):
    for i in range(N):
        count_r = 1 # 가로 최대 저장
        count_c = 1 # 세로 최대 저장
        for j in range(1,N):
            if A[i][j] == A[i][j-1]: # 해당 행의 연속 계산
                count_r += 1
                if res < count_r: # 최대 길이 저장
                    res = count_r
            else:
                count_r = 1
            if A[j][i] == A[j-1][i]: # 해당 열의 연속 계산
                count_c += 1
                if res < count_c: # 최대 길이 저장
                    res = count_c
            else:
                count_c = 1
    return res

# 오른쪽,아래쪽 방향으로 원소 교환 O(n**2)
for k in range(N):
    for r in range(N-1):
        Change_seat(k,r,True)
        res = Count_max(res)
        Change_seat(k,r,True)
    for c in range(N-1):
        Change_seat(c,k,False)
        res = Count_max(res)
        Change_seat(c,k,False)

print(res)