# Calculator

num1str = input("Please input first number ")
num2str = input("Please input second number ")
num1 = int(num1str)
num2 = int(num2str)
oper = input("Please select operations ")

if (oper == "*"):
    print(num1 * num2)
elif (oper == "/"):
    print(num1 / num2)
elif (oper == "*"):
    print(num1 + num2)
elif (oper == "-"):
    print(num1 - num2)
else:
    print("Not a valid operation")
 


