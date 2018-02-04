#Data types and flow control instruction
#---------------------------------------------
#list of chars
a = ['aa', 'bb', 'cc']
#list of numbers
n = [1, 2, 3]
#concatenate lists
x = [a, n]
#print the fist list
print x[0]
#print the first element of the first list
print x[0][0]
#---------------------------------------------
#while example
a, b = 0, 1
#a=b and at the same time b=a+b
a, b = b, a+b
print "a=", a
print "b=", b
while b < 1000:
    print b,
    a, b = b, a+b
print "\nout of while without identation"
#---------------------------------------------
#for example
words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)

x = 1
for w in words[:]:  # Loop over a slice copy of the entire list.
    print x
    x = x+1
    if len(w) > 6:
        words.insert(0, w)
print words
#---------------------------------------------
#the range function
x=range(10)
print x
#---------------------------------------------
#iteration with range and length
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]
#---------------------------------------------
#break and continue examples
for num in range(2, 15):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num
    break;
#---------------------------------------------
#input values and if, elseif
x = int(raw_input("Please enter an integer: "))
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'
