# 베스킨라빈스 31
import sys
input = sys.stdin.readline

num = 1
l = 10001
for idx in range(1, int(input())+1):
    j, m = map(int, input().split())

    r = (j-1) % (m+1)
    turn = ((j-r) // (m+1)) * 2 + 2
    if turn < l:
        num, l = idx, turn
    
print(num, l)