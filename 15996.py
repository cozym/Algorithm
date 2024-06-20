# 팩토리얼 나누기
import sys
input = sys.stdin.readline

N,A = map(int,input().split())

# 9! 3

# 1 2 3 4 5 6 7 8 9
#     1     1     1 => 9//3
#                 1 => 9//3**2
res = 0
up = A
while N//up != 0:
    res += N//up
    up *= A

print(res)