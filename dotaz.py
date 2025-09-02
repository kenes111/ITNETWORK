# message = input("Enter your message: ")
# message = message.lower()
# print(f"The original message: {message}")
# coded_message = ""
# alphabet_chars = "abcdefghijklmnopqrstuvwxyz "
# morse_chars = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
# "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
# "...-", ".--", "-..-", "-.--", "--..", "/"]
# for char in message:
#     morse_char = "?"
#     try:
#         index = alphabet_chars.index(char)
#         morse_char = morse_chars[index]
#         coded_message = coded_message + " " + morse_char
#     except ValueError:
#         print("Not a valid character") # b=3
# print(f"Your coded message: {coded_message}")
#=======================================================================================

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
========================================================================================================

# fruit_list = ["Apples", "Pears", "Plums", "Apricots", "Strawberries", "Cherries"]
# index = -1
#
# for fruit in fruit_list:
#     if len(fruit) > 6:
#         index = fruit_list.index(fruit)
#         break
#
# if index >= 0:
#     print(f"First word longer than 6 characters: {fruit_list[index]}")

# numbers_string = "10,50,abcd,30,9"
# numbers_list = numbers_string.split(',')
# total = 0
#
# for item in numbers_list:
#     if not item.isdigit():
#         continue
#
#     else:
#         number = int(item)
#         total += number
#
# print(f"The sum is: {total}")

# a = 0
# while a < 10:
#     a += 1
#     print(a)


# def factorial(number):
#     if number > 0:
#         return factorial(number - 1) * number
#     else:
#         return 1
# result = factorial(0)
# print(result)

# def generate_hello(name: str) -> str:      #  the return value of the function will be str
#     return "Hello, " + name + "!"
# generate_hello("John")
# print(generate_hello(name)
def get_number(prompt_text, error_text):
    invalid_input = True
    while invalid_input:
        try:
            number = float(input(prompt_text))
            invalid_input = False
        except ValueError:
            print(error_text)

    return number
get_number(2,5)