# 소수 구하기 (1929)
# 에라토스테네스의 체
import sys

mn = list(map(int,sys.stdin.readline().split()))
ans = list(range(mn[0],mn[1]+1))

for i in ans:
    flag = 0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            flag = 1
            break
    if flag == 0:
        print(i)
