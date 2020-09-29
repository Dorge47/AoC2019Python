inputRange = [256310, 732736]
pwdList = []
pwdList2 = []


def verifyNum(numToVerify):
    repeats = False
    n = str(numToVerify)
    if not len(n) == 6:
        return False
    for i in range(0, len(n)):
        if i == 0:
            continue
        else:
            if n[i] < n[i-1]:
                return False
            if n[i] == n[i-1]:
                repeats = True
    return repeats


def verifyNum2(numToVerify):
    repeats = False
    n = str(numToVerify)
    if not len(n) == 6:
        return False
    for i in range(0, len(n)):
        if i == 0:
            continue
        else:
            if n[i] < n[i-1]:
                return False
        compareNum = int(n[i])
        occurences = 1
        for j in range(0, len(n)):
            if i == j:
                continue
            else:
                if int(n[j]) == compareNum:
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
