print("Welcome to your Smart School Day Planner!\n\n\n")

day = str(input("What is the day?(Friday, Monday, e.t.c)"))lowercase().
weather = str(input("What is the Weather today?(snowing, sunny, raining, e.t.c)"))lowercase().
homework = str(input("Do you have homework?(Yes, No)"))lowercase().

if day in("Friday", "Saturday", "Sunday"):
    print(The day : Weekend - enjoy your day off from school!\n)
elif day == "Monday": 
    print("The day : The first day of another school week. Pack your bag and weekly planner.\n")
elif day in("Tuesday", "Thursday"):
    print("The day : Just a few school days till weekend. Finish everything!\n")
elif day == "Wednesday":
    print("The day : The only day you don't have after school, which means more time to playyyyyyy!\n")
else:
    print("The day : There is no such day, please check your spelling.\n")

if weather == "sunny" and homework == "yes":
    print("After school: Do not go outside - its always hot, do homework at home instead!\n")

if weather == "rainy" or "snowing":
    print("Weather: Pack your umbrella and water-resistant jacket - it may get wet and cold outside.\n")

if not(homework == "yes"):
    print("Homework: Not finished yet. Finish it before going to sleep!\n")

if weather == "rainy" and not (homework == "yes"):
    print("Best idea : Stay inside, and finish your homework, then go play in the rainnnnn!")
elif weather == "sunny" and (homework == "yes") and not (day in ("Monday", "Tuesday", "Wednesday", "Thursday")):
    print("Best idea : Go out - its the weekend!")
elif day in ("Monday", "Tuesday", "Wednesday", "Thursday") and weather == "windy":
    print("Best idea : Its a school day - Try not to fall asleep in school!")
else:
    print("Best idea : Don't forget to rest - you can do this!\n")

print("Your Smart School Day Planner is complete! Have a nice day!")