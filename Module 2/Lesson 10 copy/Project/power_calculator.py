print(" **** Power Calculator **** \n\n")

base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent: "))
print()

result = 1 # I selected 1 and not zero because adding zero changes nothing, and multiplying zero destroys the whole thing. If i use 1 it changes nothing in multiplication and doesn't ruin everything

for i in range(1, exponent + 1):
    result = result * base
    print("Step", i, ": result =", result)

print("\n answer:", base, "to the power", exponent, " = ", result)