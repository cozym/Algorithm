# 외판원 순회 2
import sys

N = int(sys.stdin.readline())
W = []  # 도시간 이동 비용
for i in range(N):
    W.append(list(map(int,sys.stdin.readline().split())))
used = [False for i in range(N)]
check = [0 for i in range(N+1)]
res = -1

# 인덱스를 순열화하여 모든 경우 계산
def recursion(idx,N):
    if idx==N:
        check[N] = check[0]
        cost(check)
        return
    for i in range(N):
        if used[i]:
            continue
        used[i]=True
        check[idx] = i
        recursion(idx+1,N)
        used[i]=False

# 순회 비용 계산
def cost(check_in):
    sum = 0
    global res
    for i in range(1,N+1):
        tmp = W[check_in[i-1]][check_in[i]]
        if tmp==0: # 길이 없는 경우
            return
        else:
            sum += tmp
    if res<0: # 초기값 설정
        res = sum
    elif res > sum:
        res = sum

recursion(0,N)
print(res)