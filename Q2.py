distance_km = float(input("Enter the distance between two cities in kilometers: "))


km_to_ft = 3280.839895
km_to_in = 39370.07874
km_to_cm = 100000

# distance in feet
distance_ft = distance_km * km_to_ft

# distance in inches
distance_in = distance_km * km_to_in

# distance in centimeters
distance_cm = distance_km * km_to_cm

# Print the results
print("Distance in feet: ", distance_ft)
print("Distance in inches: ", distance_in)
print("Distance in centimeters: ", distance_cm)
