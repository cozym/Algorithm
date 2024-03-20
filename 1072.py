# 게임
import sys
input = sys.stdin.readline

X,Y = map(int,input().split())
startZ = (Y*100)//X

l,r = 0,X
game = -1
while l<=r:
    h = (l+r)//2
    currentZ = ((Y+h)*100)//(X+h)
    if currentZ != startZ:
        game = h
        r = h-1
    else:
        l = h+1

print(game)