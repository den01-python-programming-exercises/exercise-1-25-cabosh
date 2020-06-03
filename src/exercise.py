def main():
    #write your code below this line
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    if num1 > num2:
        print(f"The greater number is: {num1}")
    elif num2 > num1:
        print(f"The greater number is: {num2}")
    elif num1 == num2:
        print("The numbers are equal!")

if __name__ == '__main__':
    main()
