
#Q1 AND Q2
moth_in_house_input = (input('Is there moths in the house?'))
if moth_in_house_input == "True":
    # print('Get the moths.')
    moth_in_house = True
elif moth_in_house_input == "False":
    moth_in_house = False
    # print('No Threats Detected')
else:
    print("Did not use correct input")


mitch_in_house_input = (input('Is Mitch in the house?'))
if mitch_in_house_input == "True":
    mitch_in_house = True
elif mitch_in_house_input == "False":
    mitch_in_house = False
else:
    print("Did not use correct input")


if mitch_in_house and moth_in_house:
    print("Hoooman! Help me get the moths!")
elif not mitch_in_house and not moth_in_house:
    print("No threats detected.")
elif not mitch_in_house and moth_in_house:
    print("Meooooooooow! Hisssssss!")
elif mitch_in_house and not moth_in_house:
    print("Climb on Mitch")


#Q3


#Q1 AND Q2
light_colour = (input('What is the light colour'))
car_detected = (input('Is there a car'))

if light_colour == "Red" and car_detected == "False":
    print("Do nothing.")
elif light_colour == "Red" and car_detected == "True":
    print("FLASH!!!")
elif light_colour == "Green" and car_detected == "False":
    print("Do nothing")
elif light_colour == "Green" and car_detected == "True":
    print("Do nothing")
elif light_colour == "Amber" and car_detected == "True":
    print("Do nothing")
elif light_colour == "Amber" and car_detected == "False":
    print("Do nothing")
else:
    print("wrong inputs")


roller_coaster_height = float(input('What is your height'))
if roller_coaster_height < 120:
    print("Sorry, not today :( ")
else:
     print("Hop on!")






