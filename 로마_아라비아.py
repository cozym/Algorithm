romanDict2 = { 1:'I', 4:'IX', 5:'V', 9:'IX', 10:'X',40:'XL', 50:'L', 90:'XC', 100:'C',400:'CD', 500:'D', 900:'CM', 1000:'M'}
keyValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
length = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def toRomanNumber(n):
    str = ""
    for i in range(len(keyValues)):
        while n >= keyValues[i] :
            str += romanDict2[keyValues[i]]
            n -= keyValues[i]
    return str

for i in range(1,5000) :
    ll = len(toRomanNumber(i))
    length[ll] += 1
		
#N = int(input(""))
print(length)
