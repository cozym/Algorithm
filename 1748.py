# 수 이어 쓰기 1
import sys

N = int(sys.stdin.readline())
i=1
res=0

for i in range(1,len(str(N))):
    res += 9*(10**(i-1))*i
res += (N - 10**(len(str(N))-1) + 1) * len(str(N))

print(res)