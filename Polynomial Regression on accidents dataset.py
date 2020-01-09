import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
data = pd.read_csv("final.csv")
y=data.Survival
#x is a matrix which stores all the input values
x=[]
for i in range(len(data['Vehicle_Reference'])):
    #z is a column in the matrix of input values
    z=[]
    z.append(data['Vehicle_Reference'][i])
    z.append(data['Vehicle_Reference'][i]**2)
    z.append(data['Vehicle_Reference'][i]*data['Age_of_Driver'][i])
    z.append(data['Vehicle_Type'][i])
    z.append(data['Vehicle_Type'][i]*data['Skidding_and_Overturning'][i]) 
    z.append(data['Junction_Location'][i])
    z.append(data['Skidding_and_Overturning'][i])
    z.append(data['Age_of_Driver'][i])
    z.append(data['Age_of_Driver'][i]**2)
    x.append(z)

linearreg = LinearRegression()
linearreg.fit(x,y)
y_predict = linearreg.predict(x)
#e is a variable to store of error with regularisation
e=0
e=np.sqrt(metrics.mean_squared_error(y,y_predict))
y_predict = linearreg.predict(x)
for i in range(len(linearreg.coef_)):
    e=e+linearreg.coef_[i]**2
e=e+linearreg.intercept_**2
#printing the value of mean squared error
print(np.sqrt(metrics.mean_squared_error(y,y_predict)))
#printing the value of mean squared error with the regularisation term(in this case we have taken lambda as 1)
print(e)

x1=int(input("Enter the Vehicle Reference"))
x2=int(input("Enter the Vehicle Type"))
x3=int(input("Enter the Juntion Location"))
x4=int(input("Enter the degree of skidding and overturning"))
x5=int(input("Enter the age of the driver"))

print("The probability of death is ",linearreg.coef_[0]*x1+linearreg.coef_[1]*x1*x1+linearreg.coef_[2]*x1*x5+linearreg.coef_[3]*x2+linearreg.coef_[4]*x2*x4+linearreg.coef_[5]*x3+linearreg.coef_[6]*x4+linearreg.coef_[7]*x5+linearreg.coef_[8]*x5*x5+linearreg.intercept_)
