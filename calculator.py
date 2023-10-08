num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print(
    "enter 1 for 'addition' \n enter 2 for 'subtraction' \n enter 3 for 'multiplication' \n enter 4 for 'division'"
    )
entered_number=int(input( "enter the number from 1 to 4:"))
if entered_number == 1:
     print("addition of first and second number is:" , num1+num2)
elif entered_number == 2:
     print("subtraction of first and second number is:" , num1-num2)
elif entered_number == 3:
     print("multiplication of first and second number is:" , num1*num2)
elif entered_number == 4:
     print("division of first and second number is:" , num1/num2)
else:
     print("invalid input")
