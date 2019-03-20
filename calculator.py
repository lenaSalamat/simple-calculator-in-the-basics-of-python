# #return the sum of num1 and num2
# def add(num1 ,num2):
# 	return num1 + num2

# #return the result of subtracting num1 - num2
# def sub(num1 ,num2):
# 	return num1 - num2

# #return the result of multiplying num1 - num2
# def mul(num1 ,num2):
# 	return num1 * num2

# #return the result of dividing num1 - num2
# def div(num1 ,num2):
# 	return num1 / num2

# def main():
# 	operation = input("what do you want to do (+,-,*,/) :")
# 	if(operation != '+' and operation != '-' and operation != '*' and operation != '/'):
# 		#invalid operation
# 		print("you must enter a valid operation")
# 	else:
# 	    var1 = int(input("Enter num1 : "))	
# 	    var2 = int(input("Enter num2 : "))
# 	    if(operation == '+'):
# 	    	print(add(var1 ,var2))
# 	    elif(operation == '-'):
# 	        print(sub(var1 ,var2))
# 	    elif(operation == '*'):    	
# 	        print(mul(var1 ,var2))
# 	    else:
# 	        print(div(var1 ,var2))

# main()    

def add(num1, num2):
    """Returns num1 plus num2."""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2."""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 times num2."""
    return num1 * num2


def div(num1, num2):
    """Returns num1 divided by num2."""
    return num1 / num2


def main():
    """Allows user to run basic calculator operations with two numbers."""
    validInput = False
    while not validInput:
        # Get user input
        try:
            num1 = int(input("What is number 1?"))
            num2 = int(input("What is number 2?"))
            operation = int(input("What do you want to do? 1. add, 2. subtract, 3. multiply, or 4. divide. Enter  number: "))
            validInput = True
        except:
            print("Invalid input. Try again.")
    # Determine operation
    if (operation == 1):
        print("Adding...")
        print(add(num1, num2))
    elif (operation == 2):
        print("Subtracting...")
        print(sub(num1, num2))
    elif (operation == 3):
        print("Multiplying...")
        print(mul(num1, num2))
    elif (operation == 4):
        print("Dividing...")
        print(div(num1, num2))
    else:
        print("I don't understand")


main()

