# 암호 만들기
import sys

# L개의 문자로 이루어진 오름차순 수열
# 한 개의 모음과 두 개의 자음 > C의 최솟값은 3이니 모음 하나만 체크
L,C = map(int,sys.stdin.readline().split())
arr = list(map(str,sys.stdin.readline().split()))
arr.sort()
vowels = ['a','e','i','o','u']  # 모음
check = []  # 출력

def Permutation(idx,pointer):
    if len(check)==L:   # 재귀 반환조건 : 출력 개수
        c = 0   # 모음 개수
        for i in vowels:    # 모음, 자음 검사
            c += check.count(i)
        if c != 0 and L-c >= 2:
            print(''.join(check))        
        return
    if pointer >= C:    # 재귀 반환조건 : 집합 검사 개수
        return
    check.append(arr[pointer])
    Permutation(idx+1,pointer+1)    # 해당 문자열 채택
    check.pop()
    Permutation(idx,pointer+1)  # 해당 문자열 미채택

Permutation(0,0)