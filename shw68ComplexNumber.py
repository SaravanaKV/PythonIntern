import cmath
def Complex(num1,num2):
    complexNumber=complex(num1,num2)
    return complexNumber
num1=int(input("Enter then number 1 : "))
num2=int(input("Enter the number 2 : "))
complexNumber=Complex(num1,num2)
print('The complex number is complex',complexNumber)
print("The real part of complex number is:", complexNumber.real)
print("The imaginary part of complex number is:", complexNumber.imag)
print("The phase of complex number is:", cmath.phase(complexNumber))
print("The polar of complex number is:", cmath.polar(complexNumber))