number1 = int(input("First Number is :"))
number2 = int(input("Second Number is :"))
number3 = int(input("Third Number is :"))

if number1<number2:
    tempNum=number2
else:
    tempNum=number1
if tempNum<number3:
    print("Largest No is:"+str(number3))
else:
    print("Largest No is:"+str(tempNum))