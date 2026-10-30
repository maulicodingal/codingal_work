print("Welcome to your Custom Ride Builder\n\n\n")

print("To select Bike press 4,\n To select Car press 5")
choice = int(input("What Vehicle do you use?"))

if choice == 4:
    bike_type = str(input("What is your bike type?")).lower().strip()
    if bike_type == "scooty":
        print("You can drive even if you are under 12 years old in India!!!")
    elif bike_type == "flyingbike":
        print("You will fall")
    else:
        print("Buy a vehicle first")

elif choice == 5:
    print("If it is an important car press 2\n If it is a unimportant car press 1")
    car_type = int(input("What is your car type?")).lower().strip()
    if car_type == 1:
        print("Drive safe but it is ok if you crash it")
    elif car_type == 2:
        print("You must not crash it under any circumstances, and do not eat in the car!!!")
    else:
        print("The number entered is incorrect")

else:
    print("The number entered is incorrect.")

print("\n///////////////SUMMARY//////////////")
if choice == 4:
    print(f"You chose bike and your type was{bike_type}")
elif choice == 5:
    print(f"You chose car and your type was{car_type}")
else:
    print("your choice is invaid.")