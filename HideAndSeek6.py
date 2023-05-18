import sys

n,s = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A.append(s)
A.sort()

#유클리드 호제법
def GCD(a,b):
    while(a%b!=0):
        t=b
        b=a%b
        a=t
    return b


gcd = A[1]-A[0]
for i in range(1,len(A)):
    gcd = GCD(gcd,A[i]-A[i-1])  #간격끼리 최대공약수를 반복하여 구해줌


print(gcd)
