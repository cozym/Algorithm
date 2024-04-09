# 도영이가 만든 맛있는 음식
import sys
input = sys.stdin.readline

N = int(input())
ingredients = []
difference = 1e9

for _ in range(N):
    s,b = map(int,input().split())
    ingredients.append((s,b))

def makeClose(idx, S, B):
    global difference
    if abs(S-B) < difference and B != 0:
        difference = abs(S-B)
    if idx == N:
        return

    makeClose(idx + 1, S*ingredients[idx][0], B+ingredients[idx][1])
    makeClose(idx + 1, S, B)
    
makeClose(0,1,0)

print(difference)