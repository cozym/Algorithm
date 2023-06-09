#GCD 합
import sys

r = int(sys.stdin.readline())
arr = []

#유클리드 호제법
def GCD(a,b):
    t=0
    while(a%b!=0):
        t = b
        b = a%b
        a = t
    return b


for i in range(r):
    sum = 0
    arr = list(map(int,sys.stdin.readline().split()))
    for j in range(1,arr[0]):
        for k in range(j+1,arr[0]+1):
            sum+=GCD(arr[j],arr[k])
    print(sum)