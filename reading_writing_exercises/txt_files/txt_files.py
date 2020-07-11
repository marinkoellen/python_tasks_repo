names = []
# reads in spaces around the textfile so there is new line characters if not specified

with open ("names.txt") as txt_file:
    for line in txt_file:
        line = line.strip()
        print(line)
        names.append(line)
print(names)


# Including a mode argument is optional because a default value of ‘r’ will be assumed if it is omitted. The ‘r’ value stands for read mode, which is just one of many.

# The modes are:

# ‘r’ – Read mode which is used when the file is only being read
# ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
# ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
# ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file


with open("names_output.txt", "w") as txt_file:
    for name in names:
        txt_file.write(name + "\n")
