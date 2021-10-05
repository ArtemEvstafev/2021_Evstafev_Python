
import numpy as np
import matplotlib.pyplot as plt

#f2 = np.array(list(map(float, input().split())))#берет вводимые значения и делает из них вектор
U = np.array([26.67, 26.8, 27.1, 27.5, 28.3, 29.3, 31.8, 32.1])
I = np.array([5.72, 4, 3.44, 2.84, 2.4, 2.08, 1.44, 0.4])
file = open('PLAYERS.txt', 'w')
for i in range(0,7):
    print(f"{I[i]} {U[i]}", file=file)
file.close()
plt.plot(I, U)
plt.show()


#f1 = np.array([1501, 2354, 2573, 2786])
#print(f1-655)