import numpy as np
rows = int(input("Enter rows of both matrix 1 : "))
columns = int(input("Enter columns of both matrix 2 : "))
m1=[]
m2=[]
for i in range(rows):
  a=[]
  for j in range(columns):
    a.append(int(input()))
  m1.append(a)

rows2 = int(input("Enter rows of both matrix 1 : "))
columns2 = int(input("Enter columns of both matrix 2 : "))
if(rows2 == rows and columns2 == columns):
  for i in range(rows2):
    a=[]
    for j in range(columns2):
      a.append(int(input()))
    m2.append(a)

  m1 = np.array(m1)
  m2 = np.array(m2)
  print(np.dot(m1,m2))
else:
  print("Dimensions do not match to do a mult operation")