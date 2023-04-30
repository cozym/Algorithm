import sys

r = int(sys.stdin.readline())

#소수판별
def Prime(n):
    for j in range(1,int(n**0.5)+1):
        if j==1:
            continue
        elif n%j==0:
            return False
    return True

while(r):
    for i in range(2,r//2+1):
        if (Prime(i) and Prime(r-i)):
            print(r," = ",i," + ",r-i)
            break
        if i == r//2:
            print("Goldbach's conjecture is wrong.")
    r = int(sys.stdin.readline().rstrip())