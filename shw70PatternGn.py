'''
Problem #1
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

look at the output and find the pattern. Hint - add next letter in the alphabet in each row
'''
#'Go until g' so we can direct input as n=7
def pattern():
    n=7    #int(input('Enter the input : '))
    previous=''
    for i in range(1,n+1):
        print()
        previous=str(previous)+chr(96+i)+str(previous)
        print(previous)
pattern()