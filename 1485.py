# 정사각형
import sys
from math import sqrt
from itertools import permutations
input = sys.stdin.readline

def get_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def checkSquare(loc_p):
    for loc in list(permutations(loc_p, 4)):
        if get_distance(loc[0], loc[1]) == get_distance(loc[0], loc[2]) == get_distance(loc[3], loc[1]) == get_distance(loc[3], loc[2]):
            if get_distance(loc[0], loc[3]) == get_distance(loc[1], loc[2]):
                return 1
    return 0


for _ in range(int(input())):
    loc = set()
    for _ in range(4):
        r, c = map(int, input().split())
        loc.add((r, c))
    print(checkSquare(loc))