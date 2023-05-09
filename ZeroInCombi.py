import sys

<<<<<<< HEAD
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
=======
mn = list(map(int,sys.stdin.readline().split()))

upcount = 0
downcount = 0

for i in range(mn[0]-mn[1],mn[0]+1,i*2):
    upcount += mn[0]//i

for i in range(5,mn[0]-mn[1]+1,i*5):
    upcount -= 
    

print(upcount-downcount)
>>>>>>> f2bdd6bceecd2cd670595284bdeb4a42aa28ea6f
