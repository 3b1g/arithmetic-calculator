#Constant Variables
MINI_VALUE = 1

#defining arithmetic operations like addition, subtraction, multiplication and division using list
operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']

# Display the list of operations
for index, operation in enumerate(operations, start=1):
    print(f'{index}. {operation}')

while True:
    try:
        choice = int(input('Enter the Corresponding number to The Opretion: '))
        if MINI_VALUE<=choice <=len(operations):
            break
        else:
            print('Invalid Choice. Please Select a valid Opretion Number')
    except ValueError:
        print('Invalid Input. Please select a valid Number')

# Get user input for operands
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the selected operation using Nested Conditional Statements

if choice == 1:
    result = num1+num2
    operation_name = 'Addition'

elif choice ==2:
    result = num1-num2
    operation_name = 'Subtraction'

elif choice ==3:
    result = num1*num2
    operation_name = 'Multiplication'

elif choice ==4:
    if num2 ==0:
        result = 'Math Error!'
    else: 
        result = num1/num2
        operation_name = 'Division'

#Result 
if isinstance(result, str):
    print(result)

else:
    print(f'{operation_name} {result}')