# name_person = "ELLEN"
# print(f"{(name_person)} LISTS YAY")


tea_collection = ["Earl Grey","Peppermint","Lemon and ginger","Strawberry Cream"]


# print(tea_collection[3])
# print(tea_collection[0:2])
tea_collection[-1] = "Melbourne Breakfast"
# print(tea_collection[2:])


tea_collection.append("Chai")
# print(tea_collection)
# print(len(tea_collection))
tea_collection.extend(["New York Breakfast","Berry"])
# print(tea_collection.pop(4)) #remove item 5 from list
tea_collection


tea_collection.remove("Peppermint") # looks for string to remove
print(tea_collection)


#del removves lots

del tea_collection[1:3]


tea_collection.clear()


tea_collection = [
    ["Earl Grey","Breakfast","Chai"],
    ["Peppermint","Lemon and ginger","Strawberry cream"],
]

print(tea_collection[0][0])

tea_collection.append(["Chamonile","green","dandelion"])


if len(tea_collection) > 3:
    print("greater than 3")
else:
    print("less than 3")


black_teas = tea_collection[0]
print(black_teas)

if "Chai" in black_teas:
    print("Yay we have chai!")
