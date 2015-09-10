print("""
Short Tutorial on Tuples
------------------------
Tuples are immutable arrays of values. Similarly to lists, they can
contain a collection of objects and variable types of any type and
be of any size, but once made, a tuple cannot be changed. Elements
cannot be added to, removed from, or otherwise changed in any way.
Tuples are good for passing parameters around which do not change,
or which you do not wish to be changed.
""")

#Creating tuples
print("""
Creating Tuples
---------------
""")
print('Create tuple by a = (1,2,3,4,5,6,7,8,9)')
print('Create tuple by a = 1,2,3,4,5,6,7,8,9')
print('Create empty tuple by a = () or a = tuple()')
print('Create single element tuple by a = 1, or a = (1,)')
print('Create tuple of duplicate values by a = (1)*10')

#Accessing elements
print("""
Accessing Elements
------------------
""")
a = (1,2,3,4,5,6,7,8,9)
print('All of tuple:', a)
print('Second element of tuple.\t\tCmd: a[1]\t\tReturns:', a[1])
print('1st through 4th elements.\tCmd: a[0:4]\t\tReturns:', a[0:4])
print('5th to last elment.\t\tCmd: a[4:]\t\tReturns:', a[4:])
print('Every other element.\t\tCmd: a[::2]\t\tReturns:', a[::2])
print('Last element.\t\t\tCmd: a[-1]\t\tReturns:', a[-1])
x, y = a[0:2]
print('Unpacking a tuple.\t\tCmd: x, y = a[0:2]\tResults: x =', x, ', y = ', y)

#Performing operations on a tuple
print("""
Various Operations
------------------
""")
print('Note: Most operations require all elements of list be the same type.')
print('Convert other sequence types to a tuple by using tuple(var) command.')
print('Current state of tuple. a =', a)
print('Sum of tuple.\t\tCmd: sum(a)\t\tReturns:', sum(a))
print('Length of tuple.\t\tCmd: len(a)\t\tReturns:', len(a))
print('Max of tuple.\t\tCmd: max(a)\t\tReturns:', max(a))
print('Min of tuple.\t\tCmd: min(a)\t\tReturns:', min(a))
print('Count occurences.\tCmd: a.count(0)\t\tReturns:', a.count(0))
print('Test for element.\tCmd: 5 in a\t\tReturns:', 5 in a)
print('Find index of 5.\tCmd: a.index(5)\t\tReturns:', a.index(5))

#Notes on tuple properties
print("""
Notes on tuple properties
--------------_----------
- Tuples are collections of references, not objects. Hence the following
    a = (1000,)
    a[0] is 1000 #Returns false

- Tuples are faster to access and use than lists. If you have a set of variables
  that do not change, use a tuple over a list to be faster and more efficient.
""")
