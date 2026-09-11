# My Personal Goals Display

# import the keyword module
import keyword

# Creating variables using valid Python identifier names
user_name = input("Enter your Name: ")
personal_goal = input("Enter your personal goal: ")
target_month = input("Enter your target month: ")
daily_minutes = 60

# Printing Multiple Values together
print("\nName:", user_name)
print("Personal Goal:", personal_goal)
print("Target Month:", target_month)
print("Daily Practice:", daily_minutes)

# Use \n to start a new line
print("\nMy Personal Goals Display\n")

# Change how the print statement ends
print("My Goal Status:", end=" ")
print("Not Started")

print("Progress Reminder:", end=" - ")
print("Practice Every Day!")

# My Full Goal Summary
print(
    "\n",
      user_name,
      "plans to work on",
      personal_goal,
      "for",
      daily_minutes,
      "minutes every day."
)

# Print Python's keywords
print("\nPython keywords are...\n")
print(keyword.kwlist)