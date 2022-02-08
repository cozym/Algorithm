import sys

str = list(input())
count = int(input())
cursor = len(str)

for i in range(count):
    commend = sys.stdin.readline().split()

    if commend[0] == "P":
        str.insert(cursor,commend[1])
        cursor += 1
    elif commend[0] == "L" and cursor != 0:
        cursor -= 1
    elif commend[0] == "D" and cursor < len(str):
        cursor += 1
    elif commend[0] == "B" and cursor != 0:
        del str[cursor-1]
        cursor -= 1

for i in str:
    print(i,end='')