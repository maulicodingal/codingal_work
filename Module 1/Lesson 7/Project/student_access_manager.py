# |\/|\/|\/|\/|\/|\/|\/|\/| Student App Access Manager |/\|/\|/\|/\|/\|/\|/\|/\|
CAMERA = 2       # the binary value of 2 is 0010
MICROPHONE = 4   # the binary value of 4 is 0100
STORAGE = 8      # the binary value of 8 is 1000
LOCATION = 16    # the binary value of 16 is 1100

approved_student_apps = [
    "E-books",
    "ILS",
    "Chrome",
    "Play store"
]

restricted_student_apps = [
    "Roblox",
    "Instagram",
    "Youtube",
    "Shein"
]

student_name = str(input("Enter your name: "))
requested_app = input("Enter the app you want: ").lower()
 
# Identity Operators
 
if type(student_name) is str:
    print("The student's name is stored as a string.")
 
if type(requested_app) is not int:
    print("The requested app is not stored as a number.")
 
# Membership Operators
 
if requested_app in approved_student_apps:
    print(requested_app, "is an approved student app.")
if requested_app not in approved_student_apps:
    print(requested_app, "is not an approved student app.")
 
# Combine Permission Bits

student_permissions = CAMERA | MICROPHONE | STORAGE
 
print("Permission value:", student_permissions)
print("Permission bits:", bin(student_permissions))
 
if student_permissions & CAMERA:
    print("Camera permission is Enabled")
 
if student_permissions & MICROPHONE:
    print("Microphone permission is Enabled")
 
if student_permissions & STORAGE:
    print("Storage permission is Enabled")
 
if student_permissions & LOCATION:
    print("Location permission is Enabled")
 
# Bit Shifts 

left_shift_permission = CAMERA << 1

print("Camera bit:", bin(CAMERA))
print("After left shift:", bin(left_shift_permission))
 
right_shift_permission = STORAGE >> 1
 
print("Storage bit:", bin(STORAGE))
print("After right shift:", bin(right_shift_permission))

print("\n **** Final Access Result **** ")
 
# Final check

if requested_app in approved_student_apps and requested_app not in restricted_student_apps:
    print("Access is granted to", requested_app)
else:
    print("Access is denied to", requested_app)