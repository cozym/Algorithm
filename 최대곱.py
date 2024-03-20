import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().rsplit()))
res = []

A.sort()    # 정렬

res.append(A[0]*A[1])   # 음수*음수
res.append(A[-1]*A[-2]) # 양수*양수
res.append(A[-1]*A[-2]*A[-3])   # 양*양*양
res.append(A[-1]*A[0]*A[1])    # 양*음*음

print(max(res))