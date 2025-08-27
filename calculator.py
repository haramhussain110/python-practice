num1 = int(input ("enter any number :"))
num2 = int(input ("enter any Second number :"))
choice = input("enter these symbol +,-,%,/,*  :  \" ")
if choice == "+":
    result = num1 + num2
    print(result)
elif choice == "-":
    result = num1 - num2
    print(result)
elif choice == "%":
    result = num1 % num2
    print(result)
elif choice == "/":
    result = num1 /num2    
    print(result)
elif choice == "*":
    result = num1*num2 
    print(result)
else:
    print("write correct ")
