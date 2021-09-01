'''
import numpy as np
import matplotlib.pyplot as plt

#f2 = np.array(list(map(float, input().split())))#берет вводимые значения и делает из них вектор
f1 = np.array([827, 996, 1172, 1496, 2165, 2357])
f2 = np.array([838, 988, 1166, 1497, 2157, 2338])
k = np.array([1, 2, 3, 4,5 ,6 ])
f = ((f1-456)+(f2-453))/4
x = k
y = f
print(f)
#file = open('PLAYERS.txt', 'w')
#for i in range(0,14):
#print(x[i], file=file)
#file.close()
plt.plot(x, y)
plt.show()
'''
m = 0.044
L = 0.796
l = 0.001
B = 216
b = 1.7
R = 8.31
T = 273+24.9
t = 0.1
Y = m*(2*L*B)**2/(R*T)
y = Y*((t/T)**2 + (2*l/L)**2 + (2*b/B)**2)**0.5
print(Y, y, y/Y*100)
#f1 = np.array([1501, 2354, 2573, 2786])
#print(f1-655)