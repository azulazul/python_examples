#Example of data structures
#lists

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')
print a
#inserts int position 2
a.insert(2, -1)
print a
a.append(333)
print a
#get the index of the first 333
myindex=a.index(333)
print myindex
#remove the first 333
myremove=a.remove(333)
print a
a.reverse()
print a
a.sort()
print 'sort ascend', a
a.sort(reverse=True)
print 'sort descend', a
mypop=a.pop()
print 'mypop', mypop
