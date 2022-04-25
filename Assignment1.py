# Q.1
a = int(input("enter first number:"))
b = int(input("enter first number:"))
c = int(input("enter first number:"))

avg = (a+b+c)/3

print("avg",avg)


# Q.2

gross_income = float(input("Enter your gross income"))
number_of_dependents = float(input("Enter number of dependents"))
std_deduction = 10000
tax_income = gross_income - std_deduction -(number_of_dependents * 3000)
tax = (tax_income * 20)/100
if(tax<0):
    print("Invalid input")
else:
    print("Tax:", tax)

# Q.3
SID = input("Enter your SID : ")
Name = input("Enter your Name : ")
Gender = input("Enter your Gender : ")
Coursename = input("Enter your Coursename : ")
CGPA = input("Enter your CGPA : ")
student = [SID, Name, Gender, Coursename, CGPA]
print(student)

# Q.4
m1 = int(input("Marks of 1st student: "))
m2 = int(input("Marks of 2nd student: "))
m3 = int(input("Marks of 3rd student: "))
m4 = int(input("Marks of 4th student: "))
m5 = int(input("Marks of 5th student: "))
SortedMarks = [m1, m2, m3, m4, m5]
SortedMarks.sort()
print(SortedMarks)

#Q5(a)

List_of_colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'yellow']
print("List of colors before removing: ", List_of_colors)
List_of_colors.pop(3)
print("your list after removing 4th element: ",List_of_colors)

#Q5(b)

List_of_colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("List of colors before replacing:",List_of_colors)
List_of_colors[3:5]= ['Purple']
print("your list after replacing black and pink with purple:", List_of_colors)

