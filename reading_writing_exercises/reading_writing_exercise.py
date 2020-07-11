
#Q1
names = []
with open ("names.txt") as txt_file:
    for line in txt_file:
        line = line.strip()
        print(line)
        names.append(line)
print(names)


with open("names_output.txt", "w") as txt_file:
    for index,name in enumerate(names):
        txt_file.write(f"{index+1}. {name}"+ "\n")



#Q2
colour_file_name = input("Please enter file name")

COLOURS = []
import csv
with open(colour_file_name) as csv_file:
    reader = csv.reader(csv_file,delimiter=",")
    for line in reader:
         COLOURS.append(line) 
# print(COLOURS)

for colour_line in COLOURS:
    print(f"{colour_line[1]:<20} {colour_line[2]:<20} {colour_line[4]:<20}")  

#Q3

colour_file_name = input(" Please enter file name")
colour_names = []
import csv
with open(colour_file_name) as csv_file:
    reader = csv.reader(csv_file,delimiter=",")
    for line in reader:
         colour_names.append(line[4]) 

counter_red_store= 0
counter_green_store = 0
counter_blue_store = 0
for line in colour_names:
    counter_red = line.count("red")
    counter_red_store = counter_red_store + counter_red
    counter_green = line.count("green")
    counter_green_store = counter_green_store + counter_green
    counter_blue = line.count("blue")
    counter_blue_store = counter_blue_store + counter_blue


print(f"Red: {counter_red_store}")
print(f"Green: {counter_green_store}")
print(f"Blue: {counter_blue_store}")



