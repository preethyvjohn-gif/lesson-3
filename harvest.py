feild1 = 120
feild2 = 88
feild3 = 166
feild4 = 22
feild5 = 192

total = feild1 + feild2 + feild3 + feild4 + feild5
average = total / 5

print("Total hervest        :", total,  "kg")
print("Average per feild  :" , average, "kg")

price_per_kg = 15
earnings = total * price_per_kg
print("Toatal earnings      : Rs.", earnings)


bags     = total // 25
leftover = total % 25

print("Full bags packed :", bags)
print("Leftover grain    :", leftover, "kg")

last_year = 500
print("Better than last year?  :", total > last_year)
print("same as last year?      :", total == last_year)
print("At least as good?       :", total >= last_year)

total += 30
print("after seed reserve :", total, "kg")

bags = total // 25
print("Final bags packed :", bags)

