
'''
Problem #2
you have a list of student names and another list with their marks in CS.
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.
'''

studName=['Saro','Saravana','Uva','Raj','Sri','Kumar','Deeran','Dharani','Vetri','Anu']
studMark=[75,86,34,50,97,49,90,77,55,89]
noOfStudFailed=0
passedStudName=[]
for i in range(10):
    if studMark[i]>=50:
        temp=(studName[i],':',studMark[i])
        passedStudName.append(temp)
    else:
        noOfStudFailed+=1
print(passedStudName)
print(f'Number of failed student = {noOfStudFailed}')