dictF={}
for i in range(10):
    fruit=input('Enter the fruit name: ')
    if fruit in dictF:
        dictF[fruit]+=1
    else:
        dictF[fruit]=1
print(dictF)

'''
apple
apple
banana
apple

dict={
'apple'=3
'banana'=1
}
'''