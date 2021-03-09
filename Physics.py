import numpy as np
import matplotlib.pyplot as plt
#P1 = 5.53, P2 = 5.5, T=33.8
# pressure = np.array(list(map(float, input().split())))#берет вводимые значения и делает из них вектор
P1 = np.array([3.82, 3.64, 3.58, 3.4, 3.16, 3.04, 2.88, 2.62, 2.55, 2.44, 2.21, 2.13, 2.04, 1.86])
T = np.array([33, 32, 31.2, 30.2, 29.2, 28.1, 27.3, 26.1, 25.2, 24.2, 23, 22, 21, 20.2])
P2 = np.array([3.84, 3.64, 3.51, 3.32, 2.95, 2.92, 2.8, 2.7, 2.55, 2.35, 2.23, 2.13, 2.02, 1.9])
P = ((P1 + P2) / 2) * 10 * 133.332
T+=273
#x = 1/T
#y = np.log(P)
x = T
print(x)
y = P
#file = open('PLAYERS.txt', 'w')
#for i in range(0,14):
#    print(x[i], file=file)
#file.close()

plt.plot(x, y)
plt.show()