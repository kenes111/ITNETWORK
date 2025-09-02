def get_number(prompt_text, error_text):
    invalid_input = True
    while invalid_input:
        try:
            number = float(input(prompt_text))
            invalid_input = False
        except ValueError:
            print(error_text)

    return number
def another_example():
    invalid_response = True
    while invalid_response:
        answer = input("Would you like to make another calculation? [yes/no]: ").lower()
        if answer in ["yes", "no"]:
            invalid_response = False
        else:
            print("Please answer 'yes' or 'no'.")
    return answer == "yes"  #  The function returns True when the string "yes" is stored in the answer variable, otherwise it returns False.
def perform_operation(a, b):
    operation = 0
    while operation not in [1, 2, 3, 4]:
        print("1 - addition")
        print("2 - subtraction")
        print("3 - multiplication")
        print("4 - division")

        #  To avoid handling user input again when selecting an operation, we'll use our already created function here
        #  We'll cast its output (of type float) to int
        operation = int(get_number("Choose one of the following operations:  ", "Invalid input. Please enter a number..."))

        if operation == 4 and b == 0:
            print("Division by zero is not allowed!")
            operation = 0  #  Reset operation due to division by zero

        elif operation < 1 or operation > 4:
            print("Invalid choice. Please enter a number corresponding to the selected operation.") #  Invalid input handling

    match operation:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case 4:
            return a / b
print("Calculator\n")
go_on = True

while go_on:
    first_number = get_number("Enter first number: ", "Invalid number!\n")
    second_number = get_number("Enter second number: ", "Invalid number!\n")
    calculation_result = perform_operation(first_number, second_number)
    print(f"Result: {calculation_result}")
    go_on = another_example()

print("Thank you for using our calculator.")
input()