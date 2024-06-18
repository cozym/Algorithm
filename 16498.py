# 작은 벌점
import sys
input = sys.stdin.readline

A,B,C = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
res = int(1e9)

a.sort()
b.sort()
c.sort()

def searchClose(n,arr):
    l,r = 0,len(arr)-1
    num = int(1e9)
    while l <= r:
        mid = (l+r)//2
        if abs(n-arr[mid]) < abs(n-num):
            num = arr[mid]
        if arr[mid] > n:
            r = mid - 1
        elif arr[mid] < n:
            l = mid + 1
        else:
            num = arr[mid]
            return num
    return num

for i in a:
    nearAwithB = searchClose(i,b)
    nearAwithC = searchClose(i,c)
    nearBwithC = searchClose(nearAwithB,c)
    res = min(res,(max(i,nearAwithB,nearAwithC) - min(i,nearAwithB,nearAwithC)),(max(i,nearAwithB,nearBwithC) - min(i,nearAwithB,nearBwithC)))


print(res)