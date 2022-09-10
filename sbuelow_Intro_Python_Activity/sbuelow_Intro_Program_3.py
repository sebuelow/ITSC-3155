def sumDictionary(aDict, bDict):
    sumDict = {**aDict, **bDict}

    for key, value in sumDict.items():
        if key in aDict and key in bDict:
            sumDict[key] = value + aDict[key]
    return sumDict

aDict = eval(input("Enter 1st dictionary: "))
bDict = eval(input("Enter 2nd dictionary: "))
cDict = sumDictionary(aDict, bDict)
print(cDict)