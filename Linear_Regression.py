import matplotlib.pyplot as plt
from sympy import *
import pandas as pd
data = pd.read_csv("ex1data1.txt")
x=Symbol('x')
o1=Symbol('o1')
o0=Symbol('o0')
O1=0
O0=0
h=o1*x+o0
alpha=0.01
J=0
for i in range(len(data['Population'])):
    x=data['Population'][i]
    y=data['RevenueData'][i]
    J=J+(x*o1+o0-y)**2
z=J.diff(o1)
z1=J.diff(o0)
for i in range(1500):
    O1=O1-alpha*(z.subs([(o1,O1),(o0,O0)]))/len(data['Population'])
    O0=O0-alpha*(z1.subs([(o1,O1),(o0,O0)]))/len(data['Population'])
line=[O1*x+O0 for x in data['Population']]
print(O1)
print(O0)
plt.xlabel('Population')
plt.ylabel('RevenueData')
plt.scatter(data['Population'],data['RevenueData'],color="red")
plt.plot(data['Population'],line)
plt.show()

