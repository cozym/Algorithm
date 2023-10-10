# 차이를 최대로
import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
used = [False for i in range(N)]
check = [0 for i in range(N)]
ans = 0

arr.sort()

# 배열을 순열로 하여 모든 순서를 탐색
def recursion(idx,N):
    if idx==N:
        s = abs_max(check)
        global ans
        if ans < s:
            ans = s
        return
    for i in range(N):
        if used[i]:
            continue
        used[i]=True
        check[idx] = arr[i]
        recursion(idx+1,N)
        used[i]=False

# 주어진 식에 대입
def abs_max(check):
    sum = abs(check[0]-check[1])
    for i in range(3,N+1):
        sum += abs(check[i-2]-check[i-1])
    return sum

recursion(0,N)
print(ans)