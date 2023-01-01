import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rsplit()))
F = {}
result = [-1 for i in range(N)]
NGF = []

for i in A:
    if i in F:
        F[i] += 1
    else:
        F[i] = 1

for i in range(N):
        while NGF and F[A[i]] > F[A[NGF[-1]]]:
            result[NGF.pop()] = A[i]
        NGF.append(i)

print(*result)
