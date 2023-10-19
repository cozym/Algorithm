# 퇴사
import sys

N = int(sys.stdin.readline())
T = []
P = []
check = []
max_sum = 0

for i in range(N):
    t,p = map(int,sys.stdin.readline().split())
    T.append(t)
    P.append(p)

# N 최대가 15이므로 재귀를 통한 완전탐색
# i번째 인덱스를 포함할 지 말지 결정
# 포함 할 경우 i인덱스의 T값을 더해줘서 포인트 점프
# 포함 안 할 경우 포인터값만 +1
def Resignation(idx,s):
    if idx == N+1:
        global max_sum
        if max_sum < s:
            max_sum = s
        return
    if idx > N+1:
        return
        #global max_sum
        T_sum = 0
        P_sum = 0
        # for i in check:
        #     P_sum += P[i]
        # if P_sum > max_sum:
        #     max_sum = P_sum
        #     print(max_sum)
        #return 
    Resignation(idx+1,s)    
    Resignation(idx+T[idx-1],s+P[idx-1])   

Resignation(1,0)
print(max_sum)