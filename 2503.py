# 숫자 야구
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
component = ['1','2','3','4','5','6','7','8','9']
nums = list(permutations(component,3))
wrong = []

for _ in range(N):
    guess,strike,ball = map(int,input().split())
    guess = list(str(guess))
    for num in nums:
        s,b = 0,0
        for idx in range(3):
            if num[idx]==guess[idx]:
                s += 1
            elif num[idx] in guess:
                b += 1
        if strike != s or ball != b:
            if num not in wrong:
                wrong.append(num)

print(len(nums)-len(wrong))