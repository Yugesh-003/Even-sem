#Create a series by using object
#attributes(shape,size,dimension,type,values,index,bytes,empty,hasnans)
import pandas as pd

x=pd.Series([1,2,3],index=['a','b','c'])

#Returns a tuple representing the number of rows and columns in a DataFrame.
print("Shape:",x.shape)

#Returns the total number of elements (cells) in the DataFrame.
print("Size:",x.size)

#Returns the number of axes (1 for Series, 2 for DataFrame)
print("Index:",x.index)

#Returns the data type of each column
print("Dimension:",x.ndim)

#Returns the underlying NumPy array representation of the DataFrame.
print("Values:",x.values)

# Returns the index (row labels) of the DataFrame.
print("Data Type:",x.dtype)

#Returns the total memory usage in bytes.
print("Bytes:",x.nbytes)

#Returns True if the DataFrame is empty (has no rows or columns).
print("is empty:",x.empty)

#Returns True if the DataFrame contains any NaN (missing) values.
print("is empty:",x.hasnans)