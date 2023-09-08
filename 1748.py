# 수 이어 쓰기 1
import sys

N = int(sys.stdin.readline())
d = 10
res = 0

# 10부터 10씩 곱해가며 나눴을 때 0이 아니라면 9*(d//10)*(len(d)-1)
# 나눴을 때 0이라면 (N%(d//10)+1) * (len(d)-1)
while True:
    if N<10:
        res = N
        break
    if N//d == 0:
        res += (N%(d//10)+1)*(len(str(d))-1)
        break
    else:
        res += 9*(d//10)*(len(str(d))-1)
    d *= 10

print(res)