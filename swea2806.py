# N-Queen

# 행, 열, 대각 +1 넘겨주고
# 풀고 다음
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def attackCheck(x,y,p):
    for i in range(N):    # 행, 열 처리
        board[x][i] += p
        board[i][y] += p
    for j in range(1,N):  # 대각 처리
        if 0 <= x+j < N and 0 <= y+j < N:
            board[x+j][y+j] += p
        if 0 <= x+j < N and 0 <= y-j < N:
            board[x+j][y-j] += p
        if 0 <= x-j < N and 0 <= y+j < N:
            board[x-j][y+j] += p
        if 0 <= x-j < N and 0 <= y-j < N:
            board[x-j][y-j] += p
    board[x][y] -= p    # 중복 계산 빼기

def recur(idx):
    if idx == N:
        global res
        res += 1
        return
    if 0 not in board[idx]:
        return
    for i in range(N):
        if board[idx][i] != 0:
            continue
        attackCheck(idx,i,1)
        recur(idx+1)
        attackCheck(idx,i,-1)

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    res = 0
    board = [[0]*N for _ in range(N)]

    recur(0)

    print('#{} {}'.format(test_case,res))
    # ///////////////////////////////////////////////////////////////////////////////////