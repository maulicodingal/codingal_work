print("/////////// Welcome to your Holiday Activity Planner! ///////////\n\n")
 
print(" Select your holiday type")
print(" 1 - Beach Holiday")
print(" 2 - Mountain Holiday")
 
choice = int(input("Enter 1 or 2: "))
print()
 
if choice == 1:
    print(" Select your beach activity")
    print(" 1 - Swimming")
    print(" 2 - Sandcastle Building\n")
 
    beach_activity = int(input("Enter 1 or 2: \n"))
 
    if beach_activity == 1:
        print("You selected: Swimming")
        print("Best time   : Evening")
        print("Remember    : Carry goggles and slippers")
    else:
        print("You selected: Sandcastle Building")
        print("Best time   : Morning")
        print("Remember    : Carry a bucket and a shovel")
 
elif choice == 2:
    print(" Select your mountain activity")
    print(" 1 - Hiking")
    print(" 2 - Camping\n")
 
    mountain_activity = int(input("Enter 1 or 2: \n"))
 
    if mountain_activity == 1:
        print("You selected: Hiking")
        print("Best for    : Exploring Mountains")
        print("Remember    : Wear comfortable shoes")
    else:
        print("You selected: Camping")
        print("Best for    : Exploring nature")
        print("Remember    : Carry a tent and a flashlight")
 
else:
    print("That is not a valid choice.")
    print("Please enter one of the options provided.")
 
print()
print(" Your Holiday Activity plan is ready! ")
print(" ///////// Enjoy your trip! ////////// ")














