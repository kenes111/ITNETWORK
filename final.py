from selectors import SelectSelector

# for i in range(8):
#     for j in range(8):
#         if (i+j)%2:
#             print(" ", end = "")
#         else:
#             print("█", end = "")
#     print()



# print("A number in decimal: ")
# number = int(input())
# print("Number system (2-16): ")
# system = int(input())
# def prevod():
#     prepocet = 1
#     while prepocet > 0:
#         if prepocet > 0:
#             prepocet = number/system
#             result = number % system
#             print(result, end="")
#     print()


import time
from functools import lru_cache

def print_decorator(func):
    def wrapper():
        print("START")
        func()
        print("END")
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Time elapsed: {:f}'.format(end - start))
        return result
    return wrapper
print_decorator(timer)