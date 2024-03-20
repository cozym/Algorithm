import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rsplit()))
Count = 0
ans = 0

for i in A:
    Count = 0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            Count += 1
    if Count==0:
        ans+=1

if 1 in A:
    ans -= 1

print(ans)