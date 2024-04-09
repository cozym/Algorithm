import sys
input = sys.stdin.readline

n = int(input())
seats = [[0,0] for _ in range(n+1)]    # 각 자리의 왼쪽/오른쪽 승객까지의 거리 저장
seatState = [0 for _ in range(n+1)]
occupied = list(map(int,input().split()))
res = [0 for _ in range(n+1)]

# 0은 빈자리
for i in occupied:
    seatState[i] = 1

def seatUpdate(position):
    seatState[position] = 1 # 앉은 자리 표시
    r = position + 1    # 앉은 자리 기준 오른쪽방향 업데이트
    while seatState[r] == 0 and r < n:  # 오른쪽으로 한자리씩 자리가 없을때까지
        seats[r][0] = r-position    # 빈 자리의 왼쪽 승객까지의 거리 저장
        r += 1
    seats[position][1] = r-position # 빈 자리가 끝나면 찬 자리까지 업데이트
    seats[r][0] = r-position
    
    l = position - 1
    while seatState[l] == 0 and l >= 0:
        seats[l][1] = position-l
        l -= 1
    seats[position][0] = position-l
    seats[l][1] = position-l

for i in occupied:
    seatUpdate(i)

for i in range(n-len(occupied)):
    tmp = seats.index(max(seats))
    print(tmp)
    seatUpdate(tmp)