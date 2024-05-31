'''
(Problem) #1
You have a list of numbers in ascending order, but with duplicates.
Remove the duplicated, append _ at the end for each duplicate removed
eg input = [1,2,3,3,3,4,4,7,7,9]
output = [1,2,3,4,7,9,_,_,_,_]
'''
def update(inputList):
    uniqueList=[]
    numberOfDuplicate=0
    for i in range(len(inputList)):
        if inputList[i]!=inputList[i-1]:
            uniqueList.append(inputList[i])
        else:
            numberOfDuplicate+=1
    uniqueList.extend('_'*numberOfDuplicate)
    return uniqueList
inputList=[1,2,3,3,3,4,4,7,7,9]
updatedList=update(inputList)
print(updatedList)