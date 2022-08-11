inputRange = [256310, 732736]
pwdList = []
pwdList2 = []


def verifyNum(numToVerify):
    repeats = False
    n = str(numToVerify)
    if len(n) != 6:
        return False
    for index, num in enumerate(n):
        if index == 0:
            continue
        if num < n[index-1]:
            return False
        if num == n[index-1]:
            repeats = True
    return repeats


def verifyNum2(numToVerify):
    repeats = False
    n = str(numToVerify)
    if len(n) != 6:
        return False
    for index, num in enumerate(n):
        if index == 0:
            continue
        if num < n[index-1]:
            return False
        compareNum = int(num)
        occurences = 1
        for index2, num2 in enumerate(n):
            if index == index2:
                continue
            if int(num2) == compareNum:
                occurences += 1
        if occurences == 2:
            repeats = True
    return repeats


for i in range(inputRange[0], (inputRange[1]+1)):
    if verifyNum(i):
        pwdList.append(i)
print(len(pwdList))
for i in range(inputRange[0], (inputRange[1]+1)):
    if verifyNum2(i):
        pwdList2.append(i)
print(len(pwdList2))
