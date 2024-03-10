# Define mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "You can't divide by zero."
    else:
        return x / y

# Function to display calculation history
def display_history(history):
    if history:
        print("Calculation History:")
        for entry in history:
            print(entry)
    else:
        print("No calculations recorded yet.")

# Main calculator function
def calculator():
    history = []   # Initialize calculation history list
    while True:
        print("\nWelcome to Abhi's Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Show History")
        print("6. Exit")

        choice = input("Please select an option: ")

        if choice == '6':
            print("Thank you")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                operation = f"{num1} / {num2} = {result}"

            print("Result:", result)
            history.append(operation)

        elif choice == '5':
            display_history(history)

        else:
            print("Invalid choice")

if __name__ == "__main__":
    calculator()
