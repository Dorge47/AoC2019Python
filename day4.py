inputRange = [256310, 732736]
pwdList = []


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


for i in range(inputRange[0], (inputRange[1]+1)):
    if verifyNum(i):
        pwdList.append(i)
print(len(pwdList))
