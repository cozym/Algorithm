# 나는야 포켓몬 마스터
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokedex = {}

for i in range(1, N+1):
    name = input().rstrip()
    num = str(i)
    pokedex[name] = num
    pokedex[num] = name

for _ in range(M):
    print(pokedex[input().rstrip()])