from matplotlib import pyplot as plt
x=["Jithu","Kanna","Charu"]
y=[100,50,65]
plt.title("Bar Graph")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.grid(True)
plt.bar(x,y,color="magenta")
plt.show()
