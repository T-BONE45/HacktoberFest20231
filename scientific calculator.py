import math

def main():
    print("Basic Scientific Calculator")
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Square Root (√)")
        print("6. Exponentiation (^)")
        print("7. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("Enter first number: "))
            if choice != '5':
                num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        elif choice == '5':
            if num1 < 0:
                print("Error: Cannot calculate square root of a negative number.")
                continue
            result = math.sqrt(num1)
        elif choice == '6':
            result = num1 ** num2
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        print("Result: ", result)

if __name__ == "__main__":
    main()
