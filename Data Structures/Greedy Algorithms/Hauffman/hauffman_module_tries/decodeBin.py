dict = {
    '00' : 'i',
    '01' : 's',
    '10' : 'e',
    '111' : 'a',
    '1101' : 'u',
    '11000':'t',
    '11001':'o'
}

input = input()

counter = ""
finalStr = ""
for i in input:
    counter = counter + i
    if(counter in dict):
        finalStr +=dict[counter]
        counter =""
        
print(finalStr)