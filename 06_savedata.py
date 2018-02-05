import numpy as np
#saving two vectors
# saving:
x = np.random.randn(10)
y = np.random.randn(10)
f = open("data.txt", "w")
#f.write("# x y\n")        # column names
#create a matrix and transpose it
#np.array([x, y]).T
#Vector columna por vector columna
ans1=np.array([x]).T*np.array([y]).T
#Vector columna por vector renglon, resultado matriz
ans2=np.array([x]).T*np.array([y])
print 'x', x
print 'y', y
#np.savetxt('data.txt', np.array([x, y]).T, fmt="%.3f", header="x   y")
np.savetxt('data.txt', np.array([x, y]).T, header="x   y")
# loading:
x = np.zeros(10)
y = np.zeros(10)
x, y = np.loadtxt("data.txt", unpack=True)
print 'x', x
print 'y', y
