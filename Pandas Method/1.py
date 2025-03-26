
#series is like a list in python 
# The data is represented in rows and columns instead of arrays of comma seperated values. 
#
# it prints the index values by default when printing the series



#Create series by using array or dictionary
import pandas as pd
import numpy as np

li = ['R','a','y','s','T','e','c','h']


info = np.array(li)
a= pd.Series(info)#printing this would give an array of the elements in the list with index

print(a)
