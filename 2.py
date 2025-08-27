# numbers = list(range(1,11))
#
# for number in numbers:
#     print(number)
# simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
#
# for i, item in enumerate(simpsons):
#     print(f"{i}: {item}")
#
# for i in range(1,5):
#     print(f"{i}")
# numbers = range(10)
# print(numbers)
# print(list(numbers))
# print(list(numbers[:5]))
# print(list(numbers[2:8]))
# print(list(numbers[1:7:2]))
# print(list(numbers[2:9:2]))
# print(list(numbers[6:]))
#
# numbers = [2, 3, 16, 21]
# a = numbers.index(2)
# print(a)
# print(numbers[a])
# numbers.clear()
# print(numbers)
# numbers = [2, 3, 16, 21]
# numbers.remove(3)
# print(numbers)

# simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"
# simpsons.sort()
# print(simpsons)
# for s in simpsons:
#     print(s, end = " ")
#
# zoznam = list(range(10,0,-1))
# zoznam.reverse()
# for number in zoznam:
#     print(number)
# Vegetable: cabbage, cucumber, tomato, pepper, radish, carrot, broccoli.
# Fruit: apple, pear, orange, strawberry, banana, kiwi, raspberry.
# Vegetable = ["cabbage", "cucumber", "tomato", "pepper", "radish", "carrot", "broccoli"]
# Fruit = ["apple", "pear", "orange", "strawberry", "banana", "kiwi", "Raspberry"]
# repeater = "yes"
# zoznam = list("")
# while (repeater == "yes"):
#     volba = str(input("Enter the name of any fruit or vegetable:\n"))
#     zoznam.append(volba)
#     if volba in Vegetable:
#         print("You entered a vegetable")
#         repeater = "no"
#     elif volba in Fruit:
#         print("You entered a fruit")
#         repeater = "no"
#     else:
#         print("I don't recognize this word.")
#         repeater = "no"
#     repeater = str(input("Would you like to enter another word? (yes/no)"))
# print(f"You entered a total of", len(zoznam),"words")


numbers = []
print("Enter the numbers, to stop entering numbers just hit ENTER")
number = 1
while number != "":
    number = (input("Enter a number:"))
    numbers.append(number)
numbers.pop(-1)
numbers_int = list(map(int, numbers))
sorted = sorted(numbers_int)
middle = int(len(sorted) / 2)
median = (sorted[middle])
x =len(numbers_int)
while x > 0:
    print(f"{numbers_int[len(numbers_int)-x]} deviates from the median by {numbers_int[len(numbers_int)-x]-median}")
    x = x -1












