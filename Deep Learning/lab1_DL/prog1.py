import numpy as np
rows = int(input("Enter rows of both matrices : "))
columns = int(input("Enter columns of both matrices : "))
m1=[]
m2=[]
for i in range(rows):
  a=[]
  for j in range(columns):
    a.append(int(input()))
  m1.append(a)

for i in range(rows):
  a=[]
  for j in range(columns):
    a.append(int(input()))
  m2.append(a)

m1=np.array(m1)
m2=np.array(m2)
print(m1+m2)