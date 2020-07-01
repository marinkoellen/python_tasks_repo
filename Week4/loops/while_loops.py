# counter = 10

# while counter > 0:
#     print(counter)
#     if counter%2 == 0:
#         print(f"{counter} is an even number.")
#     else:
#         print(f"{counter} is an odd number.")
#     counter = counter -1


# counter = 0
# while counter < 3:
#     name = input("What is your name?")
#     counter = counter + 1


name = input("What is your name?")
while len(name) > 1:
    if name == "Ellen":
        print("You are awesome!")
    else:
        print(f"Hi {name}")
    name = input("what is your name? ")


