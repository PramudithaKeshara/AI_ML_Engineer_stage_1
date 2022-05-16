# assumed marks to be integer values

marks = []
no_of_subs = 5

for i in range(no_of_subs):
  marks.append(int(input("Enter marks for the subject no. {no}: ". format(no=i+1))))
print("")
for sub_no, mark in enumerate(marks, start=1):
  if mark >= 75:
    grade = "A"
  elif mark >= 65:
    grade = "B"
  elif mark >= 55:
    grade = "C"
  elif mark >= 45:
    grade = "S"
  else:
    grade = "F"
  print("Your grade for subject no. {sub_no} is {grade}". format(sub_no = sub_no, grade = grade))