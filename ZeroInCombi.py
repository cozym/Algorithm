# 조합 0의 개수 2004
import sys

# 특정 수를 소인수분해 하였을 때 2와 5의 개수를 카운트하기 위한 함수
def CountZero(limit,repeat):
    zero = 0
    i=repeat
    while(limit >= i):
        zero += limit//i
        i *= repeat
    return zero

nm = list(map(int,sys.stdin.readline().split()))

five = 0
two = 0

two = CountZero(nm[0],2)-CountZero(nm[0]-nm[1],2)-CountZero(nm[1],2)
five = CountZero(nm[0],5)-CountZero(nm[0]-nm[1],5)-CountZero(nm[1],5)

print(min(two,five))