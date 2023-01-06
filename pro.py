import numpy as np
import matplotlib.pyplot as plt
num=np.fromfile("c:/capstone/numbers.txt",dtype=int,sep=",")
n=np.genfromtxt("c:/capstone/chrs.txt",dtype='str',delimiter=",")
print(n)
x=np.arange(len(n))
plt.bar(x,num)
plt.xticks(x,n)
plt.ylabel("num")
plt.xlabel("n")
plt.show()
