# SWIMMING POOL ENTRY CHECKER

print(" **** Swimming Pool Entry Checker **** ")
print(Answer these 3 questions to detemine if you can enter\n.)

age = int(input("How old are you?"))
can_swim = input("Can you swim 25 meters?: (yes/no)").lower()
adult_here = input("Is an adult with you?: (yes/no)\n ").lower()

print(" Entry Decision ")

if age < 3:
    print("Age group : Toddler - splash pool only, adult required.")
elif age < 12:
    print("Age group : Child - main pool with an adult.")
elif age < 18:
    print("Age group : Teen - main pool alone if you can swim.")
else:
    print("Age group : Adult - all pools are open to you.\n]")

if can_swim != "yes" and can_swim != "no":
    print("Input error: Please answer the can you swim question with yes or no only.")
    swim_known = False
else:
    swim_known = True

if adult_here != "yes" and adult_here != "no":
    print("Input error : Please answer the adult with you question with yes or no only.")
    adult_known = False
else:
    adult_known = True

if can_swim == "yes" and adult_here == "yes":
    print("Deep pool : Allowed - you are able to swim and an adult is with you.")

if age < 12 or can_swim == "no":
    print("Shallow pool only: Stay in the shallow side today.")

if adult_known == True and not (adult_here == "yes"):
    print("Reminder : No adult with you - please do inform the lifeguard.")

if swim_known == False or adult_known == False:
    print("Verdict : Cannot decide until both questions are answered properly.\n")

elif age >= 18 and can_swim == "yes":
    print("Verdict : Full access to all pools. Enjoy your day.")
elif age >= 12 and can_swim == "yes" and adult_here == "yes":
    print("Verdict : Main pool access with an adult nearby.")
elif can_swim == "no" and not (adult_here == "yes"):
    print("Verdict : Shallow end only, and please find an adult or inform the lifeguard first.")
else:
    print("Verdict: Shallow end for today - come back with an adult for more.")

print()
print("Have a safe and amazing swim!")