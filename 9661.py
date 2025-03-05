# 돌 게임 7
import sys
input = sys.stdin.readline

N = int(input())
print("CY" if N%5==0 or N%5==2 else "SK")