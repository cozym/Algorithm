# 돌 게임 4
import sys
input = sys.stdin.readline

N = int(input())
pattern = (N-1) % 7
print("CY" if pattern==0 or pattern==2 else "SK")
# 1 = C
# 2 = S
# 3 = C
# 4 = S
# 5 = S
# 6 = S
# 7 = S
# 8 = C
# 9 = S