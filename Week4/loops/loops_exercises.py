#Q1) Continuously ask the user to enter a number until they provide a blank input. 
# Output the sum of all the numbers
user_number = input("Please enter a number")
user_number_store = 0
while len(user_number) > 0:
    user_number_store = user_number_store + int(user_number)
    user_number = input("Please enter a number")
print(f"{user_number_store} is sum of all inputs")

 
#Q2) Use a for loop to format and print the following list:

mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]


for user_details in mailing_list:
    print(f"{user_details[0]}: {user_details[1]}")



#Q3) Use a while loop to ask the user for three names and append them to a list, then use a for loop to print the list
names_list = []
while len(names_list) < 3:
    enter_name = input("Please enter a name")
    if len(enter_name)>0:
        names_list.append(enter_name)

print(f"{names_list[0]} {names_list[1]} {names_list[2]}")


# Q4) Below is a list of foods and their prices per unit:
groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]
# For the input below, assume that the input is provided in the same order as defined in the list above.
groceries_quanitities = [1,3,2,1,4,2]

running_total = 0
print("===Izzy's Food Emporium===")
for index, item in enumerate(groceries):
    item_amount = int(groceries_quanitities[index])
    item_total = item[1]*item_amount
    print(f"{item[0]:<20} ${item_total:.2f}")
    running_total = running_total + item_total
print("==========================")
print(f"${running_total:.2f}")