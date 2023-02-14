total_seconds = int(input("Enter the number of seconds: "))

hours = total_seconds // 3600

minutes = (total_seconds % 3600) // 60

seconds = (total_seconds % 3600) % 60

print("Hours: ", hours, "\nMin: ", minutes, "\nSec: ", seconds)
