#팩토리얼 10872
import sys

N = int(sys.stdin.readline())
fac = 1

for i in range(1,N+1):
    fac = fac*i

print(fac)