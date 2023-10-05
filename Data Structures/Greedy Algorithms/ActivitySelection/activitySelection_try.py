def activitySelection(inputList):
    output=[]
    inputList.sort(key=lambda x:x[1])
    j=0
    output.append(inputList[j])
    for i in range(1,len(inputList)):
        if (inputList[i][0] >= inputList[j][1]):
            output.append(inputList[i])
            j=i
    return output



s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
inputList = []
for i in range(len(s)):
    inputList.append([s[i],f[i]])
n = len(inputList)
outputActivities = []
o=activitySelection(inputList)
print(o)