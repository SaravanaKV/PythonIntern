'''
Problem #2
Same as above,but print the list in descending order
input = [1,2,3,3,3,4,4,7,7,9]
output = [9,7,4,3,2,1,_,_,_,_]
'''
def updated(inputList):
    uniqueList=[]
    numberOfDuplicate=0
    for i in range(len(inputList)):
        if inputList[i]!=inputList[i-1]:
            uniqueList.append(inputList[i])
        else:
            numberOfDuplicate+=1
    uniqueList.sort(reverse=True)
    uniqueList.extend('_'*numberOfDuplicate)
    return uniqueList
inputList=[1,2,3,3,3,4,4,7,7,9]
updatedList=updated(inputList)
print(updatedList)