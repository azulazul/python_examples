#the library numpy must be installed
#loading numpy
import numpy as np

#functional programming
def f(x): return x % 3 == 0 or x % 5 == 0
def cube(x): return x*x*x
def add(x, y): return x+y

#filter(function, sequence) returns a sequence consisting of those items from
#the sequence for which function(item) is true
myfilter=filter(f, range(2, 25))
print myfilter

#non aschi characters are nor allowed even in the comments :(
#map(function, sequence) calls function(item) for each of the sequences items
#and returns a list of the return values.
#cube of each element of the vector
mymap1=map(cube, range(1, 11))
print 'mymap1', mymap1

#sum of vectors
seq = range(8)
mymap2=map(add, seq, seq)
print 'mymap2', mymap2
#---------------------------------------------
#using the library numpy
a = np.arange(15).reshape(3, 5)
print 'numpy', a
a = np.matrix([[1, 0], [0, 1]])
b = np.matrix([[4, 1], [2, 2]])
#point wise multiplication
myout= np.multiply(a, b)
print 'myout', myout
#sum of two matrices
myout= a+b
print 'myout', myout
#matrix multiplication
myout= a*b
print 'myout', myout
a = np.zeros( (3,4) )
b = np.zeros( (3,4) )
#---------------------------------------------
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
print 'matrix', matrix
#transpose a matrix
tmatrix=zip(*matrix)
print 'tmatrix', tmatrix
#remove a complete slice of the matrix
del matrix[0]
print 'matrix', matrix
a = [-1, 1, 66.25, 333, 333, 1234.5]
print 'a', a
del a[0]
#---------------------------------------------
#set
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print 'fruit',fruit
#---------------------------------------------
#dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print 'tel', tel
print 'jack', tel['jack']
