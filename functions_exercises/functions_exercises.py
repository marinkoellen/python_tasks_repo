# #Q1
# def convert_temp(fahrenheit):
#     celcius_temp = (float(fahrenheit) - 32)*(5/9)
#     return(celcius_temp)


# farenheight_user = input("What temperature is it in fahrenheight today")
# cel = convert_temp(farenheight_user)
# cel = round(cel,2)
# print(f"It is {cel} degrees")




# #Q2
# def calculate_mean(total_sum, num_items):
#     mean_items = float(total_sum)/float(num_items)
#     return(mean_items)


# user_number = input("Please enter a number")
# total_sum = 0
# num_items = 0
# while len(user_number) > 0:
#     num_items = num_items + 1
#     total_sum = total_sum + int(user_number)
#     user_number = input("Please enter a number")
# print(f"{total_sum} is sum of all inputs")

# mean_of_items = calculate_mean(total_sum,num_items)
# mean_of_items = round(mean_of_items,2)
# print(f"The mean of all numbers entered is:{mean_of_items}")


# #Q3
# import csv

# def read_csv_file(filepath):
#     file_store_list = []
#     with open(filepath) as csv_file:
#         reader = csv.reader(csv_file,delimiter=",")
#         for line in reader:
#             file_store_list.append(line)
#     return(file_store_list) 


# def format_colour_line(colour_data):
#     for colour_line in colour_data:
#         print(f"{colour_line[1]:<20} {colour_line[2]:<20} {colour_line[4]:<20}")  


# colours_file = input("Please enter file name")
# colours_list = read_csv_file(colours_file)
# format_colour_line(colours_list)


#Q4
def calculate_cost(unit_price, number_purchase):
    item_total = (unit_price)*(number_purchase)
    return(item_total)

def calculate_receipt(groceries_list,quantities):
    print("===Izzy's Food Emporium===")
    running_total = 0
    for index, item in enumerate(groceries_list):
        item_amount = calculate_cost(item[1],int(quantities[index]))
        print(f"{item[0]:<20} ${item_amount:.2f}")
        running_total = running_total + item_amount
    running_total = round(running_total,2)
    print("==========================")
    print(f"${running_total:>27}")


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
groceries_quanitities = []
for item in groceries:
    item_amount = input(f"What quantity of {item[0]} would you like? ")
    groceries_quanitities.append(item_amount)


calculate_receipt(groceries,groceries_quanitities)