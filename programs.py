import numpy as np
# n1=np.random.rand(3)
# print(n1)
# n2=np.random.rand(3,2)
# print(n2)
# n3=np.random.randn(3,2)
# print(n3)
# n4=np.random.randint(2,4)
# print(n4)
# n4=np.random.randint(3,size=(2,4))
# print(n4)
# print(np.random.rand(3))
# print(np.random.sample(size=(3,2,3)))
import matplotlib.pyplot as plt
# snum=np.random.standard_normal(6000)
# print(snum)
# plt.hist(snum,bins=15)
# plt.show()
# score=np.array([90,60,65])
# print(score.mean())
# print(score.std())
# print(score.var())
x=np.linspace(0,2,20)
# print(x)
# y=np.sin(x)
# z=np.cos(x)
# plt.plot(x,y)
# plt.plot(x,z)
# plt.show()
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,label="sine")
plt.plot(x,z,label="cos")
plt.legend(loc="right")
plt.show()
