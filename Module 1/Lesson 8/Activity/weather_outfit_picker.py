temp = int(input("What is the temperature?"))

if temp>30:
    beach_outfit = "swimming goggles"
    print("Take your beach_outfit and head to to the Beach!")
    print("Have fun!")

else:
    print("Stay inside with heaters!")

rain = str(input("Is it Raining?(Yes or No)"))

if rain=="Yes":
    rain_reflect = "umbrella"
    print("Take an rain_reflect! \n And Don't forget to enjoy the rain!\n")

wind_speed = int(input("What is the wind speed in km/h? "))

if wind_speed > 40:
    print("You are gonna need a windbreaker! ")

else:
    print("Atleast there is wind!\n Its usually only heat daily.\n")

muddy_puddles = str(input("Are there puddles outside? (Yes or No): "))

if muddy_puddles == "Yes":
    foot_wear = "Rain Boots"
    print("Have fun and take your foot_wear!")

else:
    foot_wear = "sneakers"
    print = ("Your shoes are safe to wear outdoor!")

print("Now we have completed the weather check.")

print("  **** OUR WEATHER COLLECTION SELECTER ****  ")
print("Temperature:", beach_outfit)
print("Raining:", rain_reflect)
print("shoes chosen:", foot_wear)
print(" *********************************** ")