#
# print("Ahoj, jak se jmenuješ?")
# meno = input()
# print("Jaký jsi?")
# vlastnost = input()
# print(f"{meno}, je, {vlastnost}")
# from fractions import Fraction
# from decimal import Decimal
# a = Fraction(3, 4)
# b = Fraction(1, 3)
# result = float(a + b) # addition of fractions 3/4 + 1/3
# print(round(Decimal(result),21))
# smiley = input("Enter smiley:")
# if smiley == ":-)" or smiley == ":)":
#     print("Your smiley is happy")
# elif smiley == ":-(" or smiley == ":(":
#     print("Your smiley is sad")
# elif smiley == ":-*" or smiley == ":*":
#     print("Your smiley is in love")
# elif smiley == ":-P" or smiley == ":P":
#     print("Your smiley is sticking out its tongue")
# else:
#     print("Your smiley is unknown")

#
# print("Welcome to calculator!")
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# print("Choose one of the following operations: ")
# print("1 - addition")
# print("2 - subtraction")
# print("3 - multiplication")
# print("4 - division")
# option = int(input())
#
# if (option == 1):
#     result = a + b
# elif (option == 2):
#     result = a - b
# elif (option == 3):
#     result = a * b
# elif (option == 4):
#     if b != 0:
#         result = a / b
#     else:
#         print("Division by zero is not allowed!")
#         result = "N/A"
# if option > 0 and option < 5:
#     print(f"Result: {result}")
# else:
#     print("Invalid option")
# print("Thank you for using calculator.")
# print("Welcome to calculator!")
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# print("Choose one of the following operations: ")
# print("1 - addition")
# print("2 - subtraction")
# print("3 - multiplication")
# print("4 - division")
# option = int(input())
# match option:
#     case 1:
#         result = a + b
#     case 2:
#         result = a - b
#     case 3:
#         result = a * b
#     case 4:
#         if b != 0:
#             result = a / b
#         else:
#             print("Division by zero is not allowed!")
#             result = "N/A"
#
# if option > 0 and option < 5:
#     print(f"Result: {result}")
# else:
#     print("Invalid option")
# print("Thank you for using calculator.")
# m = 15
# n = 10
# x = range(m-n)
# print(x)
# for i in range(1, 11):
#     print(i, end = ' ')
# print("Exponent calculator")
# print("==========")
# a = int(input("Enter the base: "))
# n = int(input("Enter the exponent: "))
# result = a
# for i in range(n - 1):
#     result = result * a
#
# print(f"Result: {result}")
# print("Thank you for using our exponent calculator")
# fish_count = int(input("How many fish do you want for dinner?\n"))
# ryba = "<° )))-<"
# x = 0
# while x < fish_count:
#     print(ryba)
#     x += 1
# fish_count = int(input("How many fish do you want for dinner?\n"))
# for x in range(fish_count):
#     print("<° )))-<")
# input()

# count = int(10)
# while (count <= 10 and count > 1):
#     print(f"{count} green bottles hanging on the wall and one green bottle should accidentally fall")
#     count -= 1
# print(f"{count} green bottle hanging on the wall and one green bottle should accidentally fall")

# print("Combination of rolls with two six-sided dice:")
# for i in range(1,7):
#     for j in range(1,7):
#         print(f"({i},{j})", end=" ")