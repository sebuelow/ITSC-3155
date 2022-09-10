def Divides_by_7(start, end):
    numbers = []
    for x in range(start, end):
        if x % 7 == 0 and x % 5 != 0:
            numbers.append(str(x))
    return numbers

start = int (input("Enter starting number:"))
end = int (input("Enter ending number:"))
divides7 = Divides_by_7(start, end)
print (divides7)
