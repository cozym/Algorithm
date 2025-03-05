# 이제는 더 이상 물러날 곳이 없다
import sys
input = sys.stdin.readline

N = int(input())
print("Goose" if N%2==1 else "Duck")