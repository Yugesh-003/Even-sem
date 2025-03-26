#operations(filter,map,std,count)
import numpy as np
import pandas as pd

#Map
a=pd.Series(['Java','C','C++',np.nan])
print(a.map({'Java':'Core',"C":'Python'}))

#Standard Deviation (std)
print("Standard Deviation :",np.std([1,2,3,4,5]))

#Count
i=pd.Series([2,1,1, np.nan, 3,4,5,5])
print(i.count())


#Filter
arr=np.array(([20,30,40],[50,70,80]))
df=pd.DataFrame(arr,index=["Vijay","Jay"],columns=["Physics","Chemistry","Maths"])
print(df)
print(df.filter(items=["Physics"]))