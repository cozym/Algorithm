# 금민수의 개수
import sys
input = sys.stdin.readline

A,B = map(int,input().split())
res = 0

def check(n):
    global res
    num = int(n)

    if num > 1e9:
        return
    
    if A <= num and num <= B:
        res += 1

    check(n+'4')
    check(n+'7')

check('0')

print(res)