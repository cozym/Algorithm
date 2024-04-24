# 배열 돌리기
import sys
input = sys.stdin.readline

T = int(input())

def front45(arr,n):
    tmpArr = [a[:] for a in arr]
    for x in range(n):
        tmpArr[x][(n+1)//2-1] = arr[x][x]
        tmpArr[x][n-x-1] = arr[x][(n+1)//2-1]
        tmpArr[(n+1)//2-1][n-x-1] = arr[x][n-x-1]
        tmpArr[n-x-1][n-x-1] = arr[(n+1)//2-1][n-x-1]
        
    print(tmpArr)

for _ in range(T):
    n,d = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    
    front45(arr,n)