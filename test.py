import numpy as np

x = open('Concentrations.csv','r')

data = np.loadtxt(x, delimiter=',')
print(data)

print(data[1][1])
