#this is the addfnction
def addFunction(var1: float, var2: float):
    """Function to Add"""
    return var1 + var2

#this is the subtraction fnction
def subFunction(var1: float, var2: float):
    """Function to Substract"""
    return var1 - var2

#this is the multiplication fnction
def mulFunction(var1: float, var2: float):
    """Function to Multiple"""
    return var1 * var2

#this is the division fnction
def divFunction(var1: float, var2: float):
    """Function to Divide"""
    if var2 == 0:
        raise ValueError('Cannot divide by zero')

    return var1 / var2

#this is the main fnction
if __name__ == '__main__':
    try:
        # menu driven program
        while True:
            print('1. Add')
            print('2. Subtract')
            print('3. Multiply')
            print('4. Divide')
            print('5. Exit')
            choice = int(input('Enter your choice: '))
            if choice == 5:
                break
            input1 = float(input('Enter first number: '))
            input2 = (input('Enter second number: '))
            if choice == 1:
                print(addFunction(input1, input2))
            elif choice == 2:
                print(subFunction(input1, input2))
            elif choice == 3:
                print(mulFunction(input1, input2))
            elif choice == 4:
                print(divFunction(input1, input2))
            else:
                print('Invalid choice')
            print()

    except ValueError as e:
        print(e)
        

