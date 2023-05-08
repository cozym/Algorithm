import sys

mn = list(map(int,sys.stdin.readline().split()))

upcount = 0
downcount = 0

for i in range(mn[0]-mn[1],mn[0]+1,i*2):
    upcount += mn[0]//i

for i in range(5,mn[0]-mn[1]+1,i*5):
    upcount -= 
    

print(upcount-downcount)
