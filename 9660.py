# 돌 게임 6
import sys
input = sys.stdin.readline

N = int(input())
print("CY" if N%7==0 or N%7==2 else "SK")