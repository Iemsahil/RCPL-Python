subject1 = float(input("Enter the marks of subject 1: "))
subject2 = float(input("Enter the marks of subject 2: "))
subject3 = float(input("Enter the marks of subject 3: "))
subject4 = float(input("Enter the marks of subject 4: "))
subject5 = float(input("Enter the marks of subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5

average_marks = total_marks / 5

percentage_marks = (total_marks / 500) * 100

print("Total marks: ", total_marks)
print("Average marks: ", average_marks)
print("Percentage marks: ", percentage_marks, "%")
