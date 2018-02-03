#example functions
#---------------------------------------------
def fib2(n):  # return Fibonacci series up to n
    """ This is a comment
    Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
#---------------------------------------------
#argument examples
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
#---------------------------------------------
#lambda functions
def make_incrementor(n):
     return lambda x: x + n
#---------------------------------------------
f100 = fib2(100)    # call it
print f100                # write the result

parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOOOM')
parrot('a million', 'bereft of life', 'jump')
#---------------------------------------------
f = make_incrementor(42)
print f(0)
print f(1)
