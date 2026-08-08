name = input("What is your name? ")
club = input("What is your school club? ")

# Different data types
member_number = 25
points = 89.5
events = 6
hours = 10.5
active = True

# Changing data types
points = int(points)
events = float(events)
member_number = str(member_number)
active = str(active)

# Show data types
print(type(points))
print(type(events))
print(type(member_number))
print(type(active))

# Badge code
badge_code = name[0:3] + name[-1]

# Reverse club name
secret_code = club[::-1]

# Print badge
print("Name: " + name)
print("Club: " + club)
print("Member Number: " + member_number)
print("Points: " + str(points))
print("Events: " + str(events))
print("Active: " + active)
print("Badge Code: " + badge_code)
print("Secret Club Code: " + secret_code)