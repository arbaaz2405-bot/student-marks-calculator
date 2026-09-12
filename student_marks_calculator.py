print("===== Student Marks Calculator =====")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
dbms = float(input("Enter DBMS marks: "))
java = float(input("Enter Java marks: "))
computer = float(input("Enter Computer marks: "))

total = maths + python + dbms + java + computer
percentage = total / 5

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")