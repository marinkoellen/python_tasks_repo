#Q1

#Function
def calculate_receipt(groceries_list):
    print("===Izzy's Food Emporium===")
    running_total = 0
    for food_item, cost_overall in groceries_list.items():
        print(f"{food_item:<20} ${cost_overall:<7.2f}")
        running_total = running_total + cost_overall
    running_total = round(running_total,2)
    print("==========================")
    print(f"${running_total:>27}")


#Data
groceries = {
"Baby Spinach": 2.78,
"Hot Chocolate": 3.70,
"Crackers": 2.10,
"Bacon": 9.00,
"Carrots": 0.56,
"Oranges": 3.08
}


# calculate amounts
for item, cost in groceries.items():
        item_amount = input(f"What quantity of {item} would you like? ")
        cost_updated = cost*int(item_amount)
        groceries[item] = cost_updated

#' Calculate reciept
calculate_receipt(groceries)


#Q2
names = [
"Maddy", "Bel", "Elnaz", "Gia", "Izzy",
"Joy", "Katie", "Maddie", "Tash", "Nic",
"Rachael", "Bec", "Bec", "Tabitha", "Teagen",
"Viv", "Anna", "Catherine", "Catherine", "Debby",
"Gab", "Megan", "Michelle", "Nic", "Roxy",
"Samara", "Sasha", "Sophie", "Teagen", "Viv"
]
print(names)
names_unique = set(names) 
print(names_unique)

name_dict = {}
for name in names_unique:
    name_count = names.count(name)
    name_dict[name] = name_count


for name, count in name_dict.items():
    print(f"{name} {count}")


#Q3
import csv

colours = []
with open("colours_20.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    a = list(reader)
    colours.append(a)

print(colours)
