print("Welcome to your chore checklist!!!\n\n")

chores = 5

current = 0

loop_v = 0

#Its declaring what the first chore is
next = "Wake up from the bed!!!\n"

#this is the loop that makes the chore request and keeps moving ahead
while loop_v <= chores :
    # it just fixes that what will be the next chore wrt the current chore
    if loop_v == 1:
        next = "Go eat Breakfast"
    elif loop_v == 2:
        next = "Get on the school bus to go to school"
    elif loop_v == 3:
        next = "play dodgeball with friends"
    elif loop_v == 4:
        next = "lets enjoy an evening snack"
    else:
        next = "Scroll a little and sleep"

print(f"This is the chore to be done - {next}")

#I am asking here that if the current chore is done or not
track = input(f"Did you finish chore {loop_v} (reply as yes/no)?:")

#Based on the value of track I am handling how next logic will be

if track == "yes":
    #increamenting the loop variable
    loop_v += 1
    current = loop_v
else:
    print("Finish your chore, its still not completed")

print(f"The user has {current}/{chores} finished.")
print("\n ***********  Well Done!!! You have finished all your chores for today   ************ ")