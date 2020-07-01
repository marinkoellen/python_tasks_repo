#Q1
foods = [
"orange",
"apple",
"banana",
"strawberry",
"grape",
"blueberry",
["carrot", "cauliflower", "pumpkin"],
"passionfruit",
"mango",
"kiwifruit"
]


print(f"{foods[0]} first item in the list")
print(f"{foods[2]} third item in the list")
print(f"{foods[-1]} last item in the list")
print(f"{foods[0:3]} last three items in the list")
print(f"{foods[-3:]} last three items in the list")
print(f"{foods[6][-1]} last item in the sub list")

#Q2
mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

mailing_list = [':'.join(x) for x in mailing_list]
print(mailing_list)


#Q3
names_list = []
Name_1 = input("Please enter name 1")
names_list.append(Name_1)
Name_2 = input("Please enter name 2")
names_list.append(Name_2)
Name_3 = input("Please enter name 3")
names_list.append(Name_3)
print(names_list)


#Q4
user_string = input('please enter a sentance')
user_string_list = list(user_string)

user_string_ouput= [len(user_string.split(sep=" ")),user_string.split(sep=" ")]
user_string_ouput2= [len(user_string_list),user_string_list]

print(user_string_ouput)
print(user_string_ouput2)