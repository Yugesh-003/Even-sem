import matplotlib.pyplot as plt
plt.title("Line Graph")
plt.plot([1,4,5],[5,3,2],'r',linewidth=5,
label="Line1")
plt.plot([1,5,3],[6,4,9],'k',linewidth=5,
label="Line2")
plt.legend()
plt.grid(True)
plt.show()