# Farm
import sys
input = sys.stdin.readline

a,b,n,w = map(int,input().split())
cnt = 0

for c in range(1,n):
    if c * a + (n-c) * b == w:
        sheep = c
        goat = n-c
        cnt += 1

if cnt == 1:
    print(sheep,goat)
else:
    print(-1)