number1 = int(input("First No"))
number2 = int(input("Second No"))

if number1<number2:
    print("Largest No is :"+str(number2))
else:
    print("Largest No is :"+str(number1))


print("Largest No is :"+str(number1)) if number1>number2 else print("Largest No is :"+str(number2))