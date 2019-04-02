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
