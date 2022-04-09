# layout--> arithmetic,binary,temp-deg/fah, power(cube,cuberoot,sqr,sqroot)


# displaying the options
print("\n\nA. Arithmetic")
print("B. Logical")
print("C. Temperature interconversion")
print("D. Exponent")

# taking user input
choice = str(input("\nEnter your choice: "))


def multiplication(x, y):
    return(x*y)


def division(x, y):
    return(x/y)


# if(choice==('A'or'B'or'C'or'D')):
if(choice == 'A'):

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice2 = int(input("\nEnter your choice "))
    num1 = int(input("Enter the first number "))
    num2 = int(input("Enter the second number "))

    if(choice2 == 1):
        ans = num1+num2
        print(num1, "+", num2, "=", ans)
    if(choice2 == 2):
        ans = num1-num2
        print(num1, "-", num2, "=", ans)
    if(choice2 == 3):
        print(num1, "*", num2, "=", multiplication(num1, num2))
    if(choice2 == 4):
        print(num1, "/", num2, "=", division(num1, num2))

if(choice == 'B'):

    print("\n1. Decimal to others")
    print("2. Binary to others")
    print("3. Hexadecimal to others")
    print("4. Octal yo others")

    choice3 = int(input("\nEnter your choice "))

    if(choice3 == 1):
        num = int(input("\nEnter a number "))
        print("The decimal value of", num, "is:")
        print(bin(num), "in binary.")
        print(oct(num), "in octal.")
        print(hex(num), "in hexadecimal.")

    if(choice3 == 2):
        decimal = int(input("Enter a binary number :"))
        binary = bin(int(decimal)).replace("0b", "")
        print("The decimal number is :", binary)
        print(oct(decimal), "in octal.")
        print(hex(decimal), "in hexadecimal.")

if(choice == 'C'):
    val = float(input("Enter the value of temperature in degree celsius "))
    kelvin = val+273
    print("\nThe value of temperature", val, "in kelvin is ", kelvin, "K")
    fahrenheit = (val*(9/5))+32
    print("\nThe value of temperature", val,
          "in fahrenheit is", fahrenheit, 'F')

if(choice == 'D'):
    num = int(input("Enter a number "))
    n = int(input("Enter the power "))
    print(num**n)
