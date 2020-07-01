# tea_collection = [
#     "Earl Grey",
#     "Melbourne Breakfast",
#     "Chai",
#     "Peppermint",
#     "Lemon and Ginger",
#     "Strawberry Cream",
#     "Chamomile",
#     "Green",
#     "Dandelion"
# ]

# for tea in tea_collection:
#     print(tea)
#     print(f"I have {tea} flavoured tea")

# print("ended loop")


# for index in range(0,10):
#     print(index)

# for index in range(0,10,2):
#     print(index)

# for index, tea in enumerate(tea_collection):
#     print(index,tea)




tea_collection = [
    ["Black", "Earl Grey", "Melbourne Breakfast", "Chai"],
    ["Flavoured", "Peppermint", "Lemon and Ginger", "Strawberry Cream"],
    ["Health", "Chamomile", "Green", "Dandelion"]
]

for tea_category in tea_collection:
    print(f"{tea_category[0]} Teas:")
    for tea in tea_category[1:]:
        print(f"    {tea} Teas:")



groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

#{item[0]:<20} saying put 20 spaces after this item
#:.2f round to 2 decimal places
for item in groceries:
    print(f"{item[0]:<20} ${item[1]:.2f}")




