# Write a program to calculate CGPA/Average of a students mark in a semester and print the grade.

sub1=int(input('Enter the mark of subject 1: '))
sub2=int(input('Enter the mark of subject 2: '))
sub3=int(input('Enter the mark of subject 3: '))
sub4=int(input('Enter the mark of subject 4: '))
sub5=int(input('Enter the mark of subject 5: '))
sub6=int(input('Enter the mark of subject 6: '))

average=(((sub1+sub2+sub3+sub4+sub5+sub6)/600)*100)

print('Average: ',average)
if average>=50:
    print('Pass')
    if average>90:
        print('Grade: O')
    elif average>80:
        print('Grade: A')
    elif average>70:
        print('Grade: A+')
    elif average>60:
        print('Grade: B')
    elif average>50:
        print('Grade: B+')
    elif average==50:
        print('Grade: C')
else:
    print('Fail')


