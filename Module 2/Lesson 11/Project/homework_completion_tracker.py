print("Welcome to your Homework Completion Tracker")

total_homework = 4
original_count = total_homework 
print(f"You have {original_count} homework tasks to finish today!\n")
 
completed_count = 0
task_num = 1
 
while task_num <= total_homework:
    if task_num == 1:
        next_task = "Economics Quiz"
    elif task_num == 2:
        next_task = "Math Quiz"
    elif task_num == 3:
        next_task = "English writing"
    else:
        next_task = "Coding practice"
 
    result = input(f"Have you finished: {next_task}? (yes or no): ")
 
    if result == "yes":
        completed_count += 1
        task_num += 1
        print("Great job! Your first Quiz has been completed.")
    else:
        print("Your task is still unfinished, finish it then check again!")
 
    print("Homework tasks remaining:", total_homework - completed_count)
    print()
 
print(" **** ALL HOMEWORK COMPLETE! **** ")
print("Good work you finished all your homework for today!\n")

print("Now let's create a safe infinite loop.")
safety_counter = 0
test_value = 0
 
while test_value <= 0:
    print("This condition never changes, so this condition would run forever!")
    safety_counter += 1
 
    if safety_counter == 3:
        print("(Stopping here on purpose, a real infinite loop never stops on its own!)")
        break

print("\n **** HOMEWORK COMPLETION TRACKER SUMMARY **** ")
print("Homework Assigned Today:", original_count)
print("Homework Completed:", completed_count)
print("Homework Remaining:", total_homework - completed_count)