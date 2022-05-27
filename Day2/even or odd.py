num=int(input("Given number is:"))

if num%2==0:
    print('EVEN Number')
else:
    print('ODD Number')

#Ternary operation
print('Even Number') if num % 2 == 0 else print('Odd Number')

DayNo = int(input("Given Day No is : "))
if DayNo==1:
    print("Sunday")
elif DayNo==2:
    print("Monday")
elif DayNo==3:
    print("Tuesday")
elif DayNo==4:
    print("Wednesday")
elif DayNo==5:
    print("Thursday")
elif DayNo==6:
    print("Friday")
elif DayNo==7:
    print("Saturday")
else:
    print("Invalid Day No")