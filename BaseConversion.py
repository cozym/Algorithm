# Base Conversion 11576
import sys

A,B = map(int,sys.stdin.readline().split())
count = int(sys.stdin.readline())
Num_list = list(map(int,sys.stdin.readline().split()))
ten = 0
res = ""

for i in range(1,count+1):
    ten += Num_list[i-1]*(A**(count-i))
    
while(ten//B):
    res = str(ten%B)+' '+res
    ten //= B
res = str(ten)+' '+res.rstrip()
print(res)