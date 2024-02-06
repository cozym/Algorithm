# 약수의 합
import sys

MAX_N = 1000001

fa = [0]*MAX_N
gx = [0]*MAX_N

for i in range(1,int(MAX_N**0.5)+1):
    for j in range(i,MAX_N,i):
        fa[j] += i

for i in range(1,MAX_N):
    gx[i] = gx[i-1]+fa[i]

for T in range(int(sys.stdin.readline())):
    print(gx[int(sys.stdin.readline())])