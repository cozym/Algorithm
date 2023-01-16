import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rsplit()))
F = {}  # 각 정수의 개수를 담을 딕셔너리
result = [-1 for i in range(N)]
NGF = []    # 인덱스를 담을 스택

# 각 정수 개수 저장
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
