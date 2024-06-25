import sys
input = sys.stdin.readline

# x*y//A == B
# x//A == B//y
# y == A*B//x
# A의 배수 탐색
A,B = map(int,input().split())
prev = int(1e9)
res = [0,0]

M = A*B
def gcd(x,y):
    xy = x*y
    while y:
        x,y = y,x%y
    if x==A and xy//A == B:
        return True
    return False

for x in range(A,int(M**0.5)+1,A):
    y = M/x
    if y%1==0 and y%A==0:   # x*y = gcd*lcm 으로 1차필터링
        y = int(y)
        if gcd(x,y):    # x로 유도하여 구한 y <-> A,B 조건 일치 검사
            if prev > x+y:
                prev = x+y
                res[0] = x
                res[1] = y
print(*res)