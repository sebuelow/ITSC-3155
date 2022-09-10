numItems = int(input("Enter number of items in invoice: "))

itemDict = dict(input("Enter name of item and price, seperated by a space: ").split(" ") for x in range(numItems))

for key in itemDict:
    itemDict[key] = (int)(itemDict[key])

sortItemDict = dict(sorted(itemDict.items(), key = lambda item:item[1]))

for key, item in sortItemDict.items():
    print(key, item)