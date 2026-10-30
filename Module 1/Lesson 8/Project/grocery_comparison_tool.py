print("*** Welcome TO YOUR GROCERY COST COMPARISON TOOL ***\n\n")

chocolate_price = 8
donut_price = 3
watermelon_price = 14
baskets = 6
family_size = 5

cost_per_person = (chocolate_price + donut_price + watermelon_price) * baskets / family_size

print("Cost per person: ", cost_per_person)
print()

total_groceries = int(input("Enter the total number of groceries: "))
family_members = int(input("Enter the number of family members sharing the groceries: "))

if family_members == 0:
    print("You cannot share with 0 family mebers")
else:
    if total_groceries % family_members == 0:
        print(total_groceries, "divide groceries equally amongst ", family_members, " family members ", total_groceries // family_members, "each.")
    else:
        print(total_groceries, "groceries cannot be divided equally among", family_members, " family members", total_groceries % family_members, "left over.")


recorded_average = 65
total_weeks = 4
incorrect_week_cost = 50
correct_week_cost = 80

recorded_total = recorded_average * total_weeks
corrected_total = recorded_total - incorrect_week_cost + correct_week_cost
corrected_average = corrected_total / total_weeks

print("Recorded total is:", recorded_total)
print("Corrected total is:", corrected_total)
print("Corrected weekly average:", corrected_average)

store_a_average = 70
store_b_average = 75
store_c_average = 80

print("Store A: ", store_a_average, "Store B: ", store_b_average, "Store C: ", store_c_average)

if corrected_average < store_a_average and corrected_average < store_b_average and corrected_average < store_c_average:
    conclusion = "cheaper than all the three stores"
elif corrected_average > store_a_average and corrected_average > store_b_average and corrected_average > store_c_average:
    conclusion = "more expensive than all three stores"
else:
    conclusion = "somewhere in between are the three stores"

print("Your average is", conclusion)

print("\n *** SUMMARY *** \n")
print("Cost per person in this family:", cost_per_person)
print("Corrected total average       :", corrected_average)
print("The concluion                 :", conclusion)