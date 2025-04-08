# 부당한 퍼즐
import sys
input = sys.stdin.readline

def modi(L):
    loc_one = L.index(1)
    return L[loc_one:] + L[:loc_one]

n = int(input())
player = list(map(int, input().split()))
goal = list(map(int, input().split()))
goal_r = list(reversed(goal))

player = modi(player)

print("good puzzle" if player == modi(goal) or player == modi(list(reversed(goal))) else "bad puzzle")