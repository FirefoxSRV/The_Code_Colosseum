import numpy as np
rows = int(input("Enter rows of both matrix 1 : "))
columns = int(input("Enter columns of both matrix 2 : "))
m1=[]
for i in range(rows):
  a=[]
  for j in range(columns):
    a.append(int(input()))
  m1.append(a)

m1 = np.array(m1)
print(m1)
print(np.transpose(m1))