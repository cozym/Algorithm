# LCS 2
import sys
input = sys.stdin.readline

str_1 = input().rstrip()
str_2 = input().rstrip()

dp_str = [['' for _ in range(len(str_2)+1)] for _ in range(len(str_1)+1)]
ans = ''

for r in range(1,len(str_1)+1):
    for c in range(1,len(str_2)+1):
        if str_1[r-1] == str_2[c-1]:
            dp_str[r][c] = dp_str[r-1][c-1] + str_1[r-1]
        else:
            if len(dp_str[r-1][c]) > len(dp_str[r][c-1]):
                dp_str[r][c] = dp_str[r-1][c]
            else:
                dp_str[r][c] = dp_str[r][c-1]
        if len(ans) < len(dp_str[r][c]):
            ans = dp_str[r][c]

print(len(ans))
print(ans)