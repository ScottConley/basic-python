'''Make a python calculator'''

def addition(num1, num2):
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
    return result

def subtraction(num1, num2):
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
    return result
    
def multiplication(num1, num2):
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
    return result
    
def division(num1, num2):
    if num2 == 0:
        print("I can't divide by zero!")
    else:
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
        return result

def main():
    num1 = input('Please enter your first number.')
    num2 = input('Please enter your second number.')
    
    op = input("Please enter whether you would like addition (a), subtraction (s), multiplication (m), or division (d).")
    
    num1 = float(num1)
    num2 = float(num2)
        
    if op in ['a','addition']:
        addition(num1, num2)
        
    elif op in ['s', 'subtraction']:
        subtraction(num1, num2)
        
    elif op in ['m', 'multiplication']:
        multiplication(num1, num2)
        
    elif op in ['d', 'division']:
        division(num1, num2)

if __name__ == '__main__':
    main()