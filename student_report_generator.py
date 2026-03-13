name=input("Enter the name of student: ") #name of the student
math=int(input("Enter marks in math: ")) #marks in math
science=int(input("Enter marks in science: ")) #marks in science
english=int(input("Enter marks in english: ")) #marks in english
total= math+science+english #total marks
percentage =total/3 #percentage conversion
if percentage >= 90: #grading
    grade="Grade A"
elif percentage >= 75:
    grade="Grade B"
elif percentage >= 60:
    grade="Grade C"
elif percentage >= 40:
    grade="Grade D"
else:
    grade="Fail"
# Report card printing
print("-----REPORT CARD ----")
print("Name", name)
print("Math", math)
print("Science" ,science)
print("English" ,english)
print("Total Marks" ,total)
print("Percentage" ,round(percentage, 2))
print("Grade" ,grade)
#Pass and fail
if math < 40 or science < 40 or english < 40:
    result="Fail"
else:
    result="Pass"
print(result)
#highest marks subject
if math>=science and math >= english:
    top_sub="Math"
    top_marks=math
elif science>=math and science >= english:
    top_sub="Science"
    top_marks=science
else:
    top_sub="English"
    top_marks=english
print("Highest scoring subject", top_sub)
print("Marks", top_marks)
#lowest marks subject
if math<=science and math <= english:
    lowest_sub="Math"
    lowest_marks=math
elif science<=math and science <= english:
    lowest_sub="Science"
    lowest_marks=science
else:
    lowest_sub="English"
    lowest_marks=english
print("Lowest scoring subject" ,lowest_sub)
print("Marks" ,lowest_marks)