# name = input("What is your name: ")
# color = input("What is your favorite color: ")
# print("hi " + name + " your favorite color is " + color)

# birth_year = input("birth year: ")
# age = 2019 - int(birth_year)
# print(age)

# weight = input("what is your weight: ")
# kilo = int(weight) * 0.453592
# print(kilo)

# string operators
# course = "Python for beginners"
# print(len(course))
# print(course.upper())
# print(course.find("o"))
# print(course.replace("P", "J"))

# x = 2.9
# print(round(x))

# good_credit = True
# house_price = 1000000

# if good_credit:
#     print(house_price * .1)
# else:
#     print(house_price * .2)

# input excercise
# weight = input("What is your weight")
# lb_or_k = input("(L)lbs or (k)kilos")
# if lb_or_k.lower() == "l":
#     lb_to_k = int(weight) * .45
#     print(f"You are {lb_to_k} kilos")
# else:
#     k_to_lb = int(weight) / .45
#     print(f"You are {k_to_lb} lbs")

# While loop excercise
# start = False
# stop = True
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if start:
#             print("car already started")
#         else:
#             print("started car")
#             start = True
#     elif command == "stop":
#         if stop:
#             print("car already stopped")
#         else:
#             print("car stopped")
#             stop = True
#     elif command == "help":
#         print("""
#       start - start car
#       stop - stop car
#       quit - quit
#       """)
#     elif command == "quit":
#         break
#     else:
#         print("sorry i dont udnerstand")

# for loop
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price

# print(total)

# nested loop
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")


# numbers = [5, 2, 5, 2, 2]
# for times in numbers:
#     output = ""
#     for occurance in range(times):
#         output += "x"
#     print(output)

# list = [9, 10, 30, 8, 7, 45, 8]
# max = 0
# for num in list:
#     if num > max:
#         max = num

# print(max)


# uniques excercise
# numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# numbers2: list = []

# for num in numbers:
#     if num not in numbers2:
#         numbers2.append(num)
# print(numbers2)
# print(numbers)


# tuple
# coordinates = (1, 2, 3)
# x, y, z = coordinates

# print(x, y, z)


# dicitonaries
# customer = {
#     "bill": "happpy",
#     "jancie": "sad"
# }
# print(customer["bill"])

# nums_hash = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
# }
# number = input("What is your phone number ")
# res = ""
# for num in number:
#     res += nums_hash.get(num, "!") + " "
# print(res)

# emojii dictionary
# emojii ctr + cmd + space
# message = input("> ")
# words = message.split(" ")
# emojiis = {
#     ":)": "😁",
#     ":(": "😞"
# }
# output = ""
# for word in words:
#     output += emojiis.get(word, word) + " "
# print(output)


# functions
# def greet_user(first_name, last_name):
#     print(f"hi {first_name} {last_name}")


# # keyword arguments
# greet_user(last_name="Smith", first_name="John")
# # positional arguments
# greet_user("John", "Smith")


# emojii dictionary
# emojii ctr + cmd + space


# def to_emojii(sentence):
#     words = sentence.split(" ")
#     emojiis = {
#         ":)": "😁",
#         ":(": "😞"
#     }
#     output = ""
#     for word in words:
#         output += emojiis.get(word, word) + " "
#     return output


# message = input("> ")
# print(to_emojii(message))


# handle errors
# try:
#     age = int(input("Age: "))
#     print(age)
# except ValueError:
#     print("invalid value")


# classes
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("moving")

#     def yell(self):
#         print("yo selfie")


# obj1 = Point(30, 20)
# print(obj1.x)

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"hello {self.name} how are you?")


# kevin = Person("Kevin")
# kevin.talk()


# inheritance
# class Mammal:
#     def walk(self):
#         print("walking")


# class Dog(Mammal):
#     pass


# class Cat(Mammal):
#     pass


# dog = Dog()
# dog.walk()

# cat = Cat()
# cat.walk()


# modules - to better organize code
# import converters
# from converters import kg_to_lbs
# print(kg_to_lbs(100))


# 3:30 packages
