field1 = 800
field2 = 700
field3 = 900
field4 = 500
field5 = 1000

total = field1 + field2 + field3 + field4 + field5
avg = total / 5

print("Total harvest: ", total, "kg")
print("Avg every field: ", avg, "kg")

price_kg = 100
earning = total * price_kg
print("Total earning: Rupees", earning)

bags = total // 25
left = total % 25

print("Full bags packed:", bags)
print("Left grain:", left, "kg")

last_year = 1000
print("Better than last year?:", total > last_year)
print("Same as last year?      :", total == last_year)
print("At least as good as last year?       :", total >= last_year)

total += 60
print("After bonus crop:", total, "kg")

total -= 15
print("After the reserved seeds:", total, "kg")

bags = total // 25
print("The final bags packed: ", bags)