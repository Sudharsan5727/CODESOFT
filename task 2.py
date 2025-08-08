def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    choice = input("Enter your choice (1/2/3/4): ")

    # Perform calculation
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
        operation = '/'
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        return


    print(f"{num1} {operation} {num2} = {result}")

calculator()

