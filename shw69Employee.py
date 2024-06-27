class Employee:
    def __init__(self,Id ,Name,Designation,Salary,Email,PhoneNumber,Manager):
        self.Id=Id
        self.Name=Name
        self.Designation=Designation
        self.Salary=Salary
        self.Email=Email
        self.PhoneNumber=PhoneNumber
        self.Manager=Manager
    def printEmp(self):
        print(f'Id : {self.Id}')
        print(f'Name : {self.Name}')
        print(f'Designation : {self.Designation}')
        print(f'Salary : {self.Salary}')
        print(f'Email : {self.Email}')
        print(f'Phone Number : {self.PhoneNumber}')
        print(f'Manager : {self.Manager}')


emp1=Employee(1,'Saro','Software Developer',45000,'saro9341748@gamil.com',8667745859,'Ram')
emp2=Employee(2,'Ram','Senior Developer',65000,'skv93008@gamil.com',8098966317,'Raj')
emp3=Employee(3,'Uva','Software Developer',30000,'uva444@gamil.com',7646879254,'Ram')
emp4=Employee(4,'Raj','Team lead',75000,'rajkumar@gamil.com',8093465817,'Kumar')
emp5=Employee(5,'Saravana','CEO',185000,'saro9341748@gamil.com',8667745859,None)
emp6=Employee(6,'Kumar','Project Manager',90000,'skv93008@gamil.com',8098966317,'Saravana')
emp7=Employee(7,'Uva','Software Developer',37000,'uva444@gamil.com',9864779254,'Deeran')
emp8=Employee(8,'Rajan','Team lead',77000,'rajkumar@gamil.com',7458955817,'Kumar')
emp9=Employee(9,'Deeran','Senior Developer',68000,'deera93008@gamil.com',954966317,'Rajan')
emp10=Employee(10,'Sri','Software Developer',30000,'sri444@gamil.com',7646879254,'Deeran')
emp=[emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8,emp9,emp10]
for i in emp:
    i.printEmp()
    print('-'*35)

