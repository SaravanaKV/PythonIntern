'''
3. you have a list of student names. you have one list each for their marks in CS, Math and English.
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.
'''

studentName=['Saro','Kumar','Uva','Raj','Deeran']
csMark=[90,88,83,98,94]
mathMark=[92,43,67,94,79]
engliseMark=[98,87,83,81,71]
studentname=[]
for i in range(0,len(studentName)):
    if mathMark[i]>=90:
        gradeM='A'
    elif mathMark[i]>=80:
        gradeM='B'
    elif mathMark[i]>=70:
        gradeM='C'
    elif mathMark[i]>=60:
        gradeM='D'
    elif mathMark[i]>=50:
        gradeM='E'
    else:
        gradeM='Fail'
    if engliseMark[i]>=90:
        gradeE='A'
    elif engliseMark[i]>=80:
        gradeE='B'
    elif engliseMark[i]>=70:
        gradeE='C'
    elif engliseMark[i]>=60:
        gradeE='D'
    elif engliseMark[i]>=50:
        gradeE='E'
    else:
        gradeE='Fail'
    if csMark[i]>=90:
        gradeC='A'
    elif csMark[i]>=80:
        gradeC='B'
    elif csMark[i]>=70:
        gradeC='C'
    elif csMark[i]>=60:
        gradeC='D'
    elif csMark[i]>=50:
        gradeC='E'
    else:
        gradeC='Fail'
    print(studentName[i],gradeM,gradeE,gradeC)
    if ((gradeM=='A' and gradeE=='B' and gradeC=='B') or (gradeM=='B'and gradeE=='A' and gradeC=='B')or
            (gradeM=='B'and gradeE=='B' and gradeC=='A') or (gradeM=='A'and gradeE=='A' and gradeC=='B') or
            (gradeM=='B'and gradeE=='A' and gradeC=='A')or (gradeM=='A'and gradeE=='B' and gradeC=='A') or
            (gradeM=='A'and gradeE=='A' and gradeC=='A')):
        studentname.append(studentName[i])
print(studentname)
