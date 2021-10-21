#create a calculator

operand_1 = int(input("Enter operand_1"))
operand_2 = int(input("Enter operand_1"))

operator = input("Enter any operator i.e. '+'/'-'/'*'/'/'")

if(operator == "+"):
    result = operand_1 + operand_2
elif(operator == "-"):
    result = operand_1 - operand_2
elif(operator == "*"):
    result = operand_1 * operand_2
elif(operator == "/"):
    result = operand_1 / operand_2
else:
    result = 0
print(result)
print("Thank You")

