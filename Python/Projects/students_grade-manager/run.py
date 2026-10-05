
# [expression for item in iterable if condition ]

squares = [x**2 for x in range(10)]
print(squares)


numbers = [1,2,3,4,5]
doubled = [x*2 for x in numbers]
print(doubled)

num = [1,2,3,4,5,6,7,8]

evens = [x for x in num if x%2==0]
print(evens)

names =["Ram","Shyam","Geta","Meta"]

uppercase_names = [name.upper() for name in names]
print(uppercase_names)













student_score = input("Enter student scores seperated by commas: ")
scores = [int(score) for score in student_score.split(",")]

grades =[
    "A" if score>=90 else
    "B" if score>=80 else
    "C" if score>=70 else
    "D" if score>=60 else
    "F"
    for score in scores
]

passing_students = [score for score in scores if score>=60]
failing_students = [score for score in scores if score<=60]

print('Student Scores :',scores)
print("Grades: ",grades)
print("Passing Students: ",passing_students)
print("failing Students",failing_students)

print("\n STUDENTS GRADES")
print("passing students ",passing_students)
print("Failing Students :",failing_students)
