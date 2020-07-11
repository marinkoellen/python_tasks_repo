def addition(a, b):
    print(f"a: {a}, b: {b}")
    result = float(a) + float(b)
    # print(result)
    return result
a = 3
b = 5
addition(a, b)
addition_result = addition(b, a)
print(addition_result)
# addition(2, 3)
# addition(4, 5)
# addition(6, 8)
# first_number = input("Pick a number: ")
# second_number = input("Pick a number: ")
# addition(first_number, second_number)
# print(result)

def is_odd(number):
    if number%2 == 0: # has a remainder of 0 - even
        return False
    else:
        return True


# counter = 5
# while counter > 0:
#     if is_odd(counter): # has a remainder of 0 - even
#         print(f"{counter} is an odd number.")
#     else:
#         print(f"{counter} is an even number.")
#     counter -= 1

def format_grocery_item(item_name,item_cost):
        return(f"{item_name:<20} ${item_cost:.2f}")


groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]
for item in groceries:
    print(format_grocery_item(item[0],item[1]))