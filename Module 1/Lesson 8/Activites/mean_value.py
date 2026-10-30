print("This program finds the correct average of 40 numbers\n")

numbers = 4
misread = int(input("What is the wrong number: "))
mean = int(input("What is the wrong average that you got: "))
number = int(input("What is the correct number: "))
print()

sum = numbers * mean
print("The value currently", sum)

sum2 = sum-((misread)-(number))
print("The intermediate value: ",sum2)
print()

mean2 = sum2 / numbers
print("The final correct mean: ", mean2)