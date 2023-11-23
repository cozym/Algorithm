# SW Expert Academy 1244. 최대 상금

T = int(input())

res = 0

def switch(arr,i,j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    return arr

def recursion(arr,n,count):
    if count==n:
        global res
        tmp = int(''.join(map(str,arr)))
        if res < tmp:
            res = tmp
        return
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            recursion(switch(arr,i,j),n,count+1)
            # arr = switch(arr,i,j)
            # recursion(arr,n,count+1)
            # arr = switch(arr,i,j)

for test_case in range(1, T + 1):
    info,n = map(str,input().split())
    arr = []
    for i in info:
        arr.append(int(i))
    n = int(n)

    recursion(arr,n,0)

    print("#{} {}".format(test_case,res))