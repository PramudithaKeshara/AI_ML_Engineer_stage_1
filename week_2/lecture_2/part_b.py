# assumed marks to be integer values

marks = []
no_of_students = 10
for i in range(no_of_students):
  marks.append(int(input("Please enter the marks for the student no. {no}: ".format(no=i+1))))

print("maximum marks of students is", max(marks)) 
print("minimum marks of students is", min(marks))
print("average marks of students is", str(sum(marks)/no_of_students))