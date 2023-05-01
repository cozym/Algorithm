import sys

#에라토스테네스
PrimeArr = [True for i in range(1000001)]
PrimeArr[0],PrimeArr[1] = False,False

for i in range(2,1000001):
    if PrimeArr[i]:
        for j in range(i+i,1000001,i):
            PrimeArr[j]=False

while(1):
    r = int(sys.stdin.readline())
    if r==0:
        break
    flag = 0
    for i in range(3,r,2):
        if PrimeArr[i] and PrimeArr[r-i]:
            print(r,"=",i,"+",r-i)
            flag = 1
            break
    if (not flag):
        print("Goldbach's conjecture is wrong.")