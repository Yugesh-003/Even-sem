from matplotlib import pyplot as plt
x=[5,7,10]
y=[18,10,6]
x2=[6,9,11]
y2=[7,14,17]
plt.scatter(x,y)
plt.scatter(x2,y2,color='g')
plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.grid(True)
plt.show()