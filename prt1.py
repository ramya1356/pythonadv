import numpy as np
import matplotlib.pyplot as plt
y1=np.fromfile("c:/advp/year1.txt",dtype=int,sep=",")
y2=np.fromfile("c:/advp/year2.txt",dtype=int,sep=",")
s1=np.fromfile("c:/advp/sales1.txt",dtype=int,sep=",")
s2=np.fromfile("c:/advp/sales2.txt",dtype=int,sep=",")
plt.plot(y1,s1,label="first sales")
plt.plot(y2,s2,label="second sales")
plt.legend(loc="upper right")
plt.ylabel("sale")
plt.xlabel("years")
plt.show()
