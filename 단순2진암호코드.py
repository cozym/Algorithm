# SW Expert Academy 1240. 단순 2진 암호코드
T = int(input())

rule = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']

def changeToNum(codeLine):
    findNums = []
    startIndex = codeLine.index('1')-1
    front = startIndex
    while len(findNums) != 8:
        if codeLine[front:front+7] in rule:
            findNums.append(rule.index(codeLine[front:front+7]))
            front += 7
        else:
            startIndex -= 1
            front = startIndex
    return findNums

for test_case in range(1, T + 1):
    row,col = map(int,input().split())
    code = []
    odd,even = [],[]

    for i in range(row):
        code.append(input())
        if '1' in code[i]:
            nums = changeToNum(code[i])

    for i in range(len(nums)):
        if i%2==0:
            odd.append(int(nums[i]))
        else:
            even.append(int(nums[i]))

    if (sum(odd)*3 + sum(even)) % 10 == 0:
        print("#{} {}".format(test_case,sum(odd)+sum(even)))
    else:
        print("#{} {}".format(test_case,0))
