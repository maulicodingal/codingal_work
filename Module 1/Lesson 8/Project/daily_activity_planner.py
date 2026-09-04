temperature = int(input("What is today's temperature in Celsius?: "))
 
# PART 2: Decide between outdoor and indoor activity
if temperature < 20:
    hobby = "indoor reading"
    print("It is cooler today."\n "Do", hobby)

else:
    hobby = "outdoor play"
    print("It is nice and cozy today."\n "Do", hobby)
 
is_it_raining = input("Is it raining today? (yes/no): ")
 
if is_it_raining == "yes":
    print("Pick an indoor activity or go and play in the rain!")
 
homework_time = int(input("What is the homework time in minutes?: "))
 
if homework_time > 100:
    break_needed = "yes"
    print("You have a long homework session today."\n "Take a break in between", hobby)

else:
    break_needed = "no"
    print("Homework time is short today."\n "No long break needed in between", hobby)
 
have_free_time = input("Do you have free time today? (yes/no): ")
 
if have_free_time == "yes":
    my_final_task = "hobby time"
    print("You have free time today."\n "Enjoy your", my_final_task)

else:
    my_final_task = "planning time"
    print("You don't have enough free time today.")
    print("Use your time for", my_final_task)
 
print("")
print(" ***** Daily activity check complete! ***** ")
 
print(" ===== DAILY ACTIVITY PLANNER ===== ")
print("Temperature:", temperature)
print("Chosen hobby:", hobby)
print("Raining:", is_it_raining)
print("Study Break Needed:", break_needed)
print("My Final Task:", my_final_task)
print("***********************************")
