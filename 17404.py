# RGB거리 2
import sys

N = int(sys.stdin.readline())
dp_r = []
dp_g = []
dp_b = []
r,g,b = map(int,sys.stdin.readline().split())

# dp_[0][x]를 -1000000으로 초기화하여 1번 집 선택의 색을 강제
dp_r.append([-1000000,g,b])
dp_g.append([r,-1000000,b])
dp_b.append([r,g,-1000000])

# 
for i in range(1,N):
    A = list(map(int,sys.stdin.readline().split()))
    dp_r.append([min(dp_r[i-1][1],dp_r[i-1][2])+A[0],min(dp_r[i-1][0],dp_r[i-1][2])+A[1],min(dp_r[i-1][0],dp_r[i-1][1])+A[2]])
    dp_g.append([min(dp_g[i-1][1],dp_g[i-1][2])+A[0],min(dp_g[i-1][0],dp_g[i-1][2])+A[1],min(dp_g[i-1][0],dp_g[i-1][1])+A[2]])
    dp_b.append([min(dp_b[i-1][1],dp_b[i-1][2])+A[0],min(dp_b[i-1][0],dp_b[i-1][2])+A[1],min(dp_b[i-1][0],dp_b[i-1][1])+A[2]])

dp_r[N-1] = list(map(lambda x:x+1000000+r, dp_r[N-1]))
dp_g[N-1] = list(map(lambda x:x+1000000+g, dp_g[N-1]))
dp_b[N-1] = list(map(lambda x:x+1000000+b, dp_b[N-1]))

min(dp_r[N-1][1],dp_r[N-1][2],dp_g[N-1][0],dp_g[N-1][2],dp_b[N-1][0],dp_b[N-1][1])

print(min(dp_r[N-1][1],dp_r[N-1][2],dp_g[N-1][0],dp_g[N-1][2],dp_b[N-1][0],dp_b[N-1][1]))