'''
problem #5
In your college Python is taught in 3 different departments by the same professor.
For each dept, get the no of students studying Python and their marks in the final exam
Get the input as comma seperated string

Find the top 3 marks in each class
Find the top 3 marks in all classes are combined.
Find the avg mark of students with passing mark in each class and the classes combined.
Find which class has the best average mark and least number of failed students.
'''
numberOfDepartment= 3 #int(input('Enter the number of department : '))
numberOfStudentInEachClasses = []
topThreeMarkInEachClasses = []
topThreeMarkInAllClasses = []
marksInEachClasses = []
marksOfClass1 = []
marksOfClass2 = []
marksOfClass3 = []
passMarksInClass1 = []
passMarksInClass2 = []
passMarksInClass3 = []
passMarksInEachClasses = []
passMarksInAllClasses = []
studentMarks={}
for classs in range(1,numberOfDepartment+1):
    numberOfStudentInClass = int(input(f'Enter the number of student in the class {classs} : '))
    numberOfStudentInEachClasses.append(numberOfStudentInClass)
    for student in range(1,numberOfStudentInClass+1):
        pythonMark = int(input(f'Enter the python Mark of student {student} in class {classs} :'))
        if classs == 1:
            marksOfClass1.append(pythonMark)
        elif classs == 2:
            marksOfClass2.append(pythonMark)
        else:
            marksOfClass3.append(pythonMark)
    marksOfClass1 = sorted(marksOfClass1,reverse = True)
    marksOfClass2 = sorted(marksOfClass2,reverse = True)
    marksOfClass3 = sorted(marksOfClass3,reverse = True)
marksInEachClasses.append(marksOfClass1)
marksInEachClasses.append(marksOfClass2)
marksInEachClasses.append(marksOfClass3)
marksOfAllClasses = sorted(marksOfClass1+marksOfClass2+marksOfClass3,reverse = True)
for mark in marksOfClass1:
    if mark >= 50:
        passMarksInClass1.append(mark)
for mark in marksOfClass2:
    if mark >= 50:
        passMarksInClass2.append(mark)
for mark in marksOfClass3:
    if mark >= 50:
        passMarksInClass3.append(mark)
passMarksInEachClasses.append(passMarksInClass1)
passMarksInEachClasses.append(passMarksInClass2)
passMarksInEachClasses.append(passMarksInClass3)
passMarksInAllClasses = passMarksInClass1+passMarksInClass2+passMarksInClass3
averageOfPassMarkInClass1 = sum(passMarksInClass1)//len(passMarksInClass1)
averageOfPassMarkInClass2 = sum(passMarksInClass2)//len(passMarksInClass2)
averageOfPassMarkInClass3 = sum(passMarksInClass3)//len(passMarksInClass3)
averageOfPassMarkInAllClasses = sum(passMarksInAllClasses)//len(passMarksInAllClasses)
if averageOfPassMarkInClass1>averageOfPassMarkInClass2 and averageOfPassMarkInClass1>averageOfPassMarkInClass3:
    bestAverageMark = averageOfPassMarkInClass1
    bestAverageMarkClass = 'Class1'
elif averageOfPassMarkInClass2>(averageOfPassMarkInClass3 and averageOfPassMarkInClass1):
    bestAverageMark = averageOfPassMarkInClass2
    bestAverageMarkClass = 'Class2'
else:
    bestAverageMark = averageOfPassMarkInClass3
    bestAverageMarkClass = 'Class3'
print('Number of student in each classes ',numberOfStudentInEachClasses)
print('Student mark in each classes ',marksInEachClasses)
print('Student mark in all classes ',marksOfAllClasses)
print('Top 3 marks in class 1 ',marksOfClass1[:3])
print('Top 3 marks in class 2 ',marksOfClass2[:3])
print('Top 3 marks in class 3 ',marksOfClass3[:3])
print('Top three marks in all classes are combined ',marksOfAllClasses[:3])
print('Student pass mark in each classes ',passMarksInEachClasses)
print('Student pass mark in all classes ',passMarksInAllClasses)
print('Average of pass mark in class 1 ',averageOfPassMarkInClass1)
print('Average of pass mark in class 2 ',averageOfPassMarkInClass2)
print('Average of pass mark in class 3 ',averageOfPassMarkInClass3)
print('Average of pass mark in all classes {:.2f}'.format(averageOfPassMarkInAllClasses))
print(f'Best average mark is {bestAverageMark} and the class is {bestAverageMarkClass}')
studentMarks={
    'Number of student in each classes ':numberOfStudentInEachClasses,
    'Student mark in each classes ':marksInEachClasses,
    'Student mark in all classes ':marksOfAllClasses,
    'Top 3 marks in class 1 ':marksOfClass1[:3],
    'Top 3 marks in class 2 ':marksOfClass2[:3],
    'Top 3 marks in class 3 ':marksOfClass3[:3],
    'Top three marks in all classes are combined ':marksOfAllClasses[:3],
    'Student pass mark in each classes ':passMarksInEachClasses,
    'Student pass mark in all classes ':passMarksInAllClasses,
    'Average of pass mark in class 1 ':averageOfPassMarkInClass1,
    'Average of pass mark in class 2 ':averageOfPassMarkInClass2,
    'Average of pass mark in class 3 ':averageOfPassMarkInClass3,
    'Average of pass mark in all classes ':averageOfPassMarkInAllClasses,
    'Best average mark ':bestAverageMark,
    'Best class average mark':bestAverageMarkClass
}
print(studentMarks)