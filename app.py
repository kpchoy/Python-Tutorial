# integrated terminal ctrl + `` (ctrl and backtick)
#  problems shift cmnd M
# shift cmnd p
# ctrl alt n     to run python code

# course_name = """
# Multiple
# Python
# Lines
# """

# interpolation
# first = "Kevin"
# last = "Choy"
# full = f"{first} {last}"
# print(full)

# uppercase letters for constants
# PI = 3.14
# print(round(PI))
# print(math.floor(PI))

# print(int(x))
# print(float(x))
# print(bool(x))

# Falsey
# ""
# 0
# []
# none

# conditional statements
# age = 15
# if age >= 18:
#     print("Adult")
#     print("Adult")
# elif age >= 13:
#     print("teenager")
# else:
#     print("Child")

# name = "  "
# if not name.strip():
#     print("name is empty")

# age = 22
# if 18 <= age < 65:
#     print("you are elligiable")

# age = 22
# message = "elligible" if age >= 18 else "not of age"
# print(message)


# LOOPS
# for x in "kevin":
#     print(x)
# for x in range(0, 10, 2):
#     print(x)

# names = ["AJohn", "Mary"]
# for name in names:
#     if name.startswith("J"):
#         print("found")
#         break
# else:
#     print("not found")

# guess = 0
# answer = 5
# while guess != answer:
#     guess = int(input("Guess: "))

# def increment(inc, by):
#     return inc + by


# print(increment(2, 3))

# def multiply(*list):
#     total = 1
#     for i in list:
#         total *= i
#     return total


# print(multiply(2, 3, 4, 5))


# def save_user(**user):
#     print(user)


# save_user(id=3, name="Kevin")

# DEBUG
# add break statement fn&f9 keys
# open up debugger and press fn&f5 keys to start debugger

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("start")
# print(multiply(1, 2, 3))
# print("finish")

def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "fizzbuzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"
    else:
        return input


print(fizz_buzz(15))
