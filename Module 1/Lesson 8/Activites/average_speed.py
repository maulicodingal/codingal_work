cyclist1 = int(input("What is the first cyclist speed?"))
cyclist2 = int(input("What is the second cyclist speed?"))
cyclist3 = int(input("What is the third cyclist speed?"))

avg = (cyclist1 + cyclist2 + cyclist3)/3
print("The average is", avg)

if avg > cyclist1 and avg > cyclist2 and avg > cyclist3:
    print("This average is banned!")
elif avg < cyclist1 or avg < cyclist2 or avg < cyclist3:
    print("You should not be in this race!")
elif avg != cyclist1:
    print("The average is not equal to the other cyclists")
elif avg > cyclist1:
    print("cyclist1 should increase their speed")
elif avg > cyclist2:
    print("cyclist2 should increase their speed")
elif avg > cyclist3:
    print("cyclist3 should increase their speed")
else:
    print("The race is postponed until the cyclists fix their speed!")