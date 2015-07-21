import numpy as np

print("""
Short Tutorial on Arrays
------------------------
Arrays are part of the numpy package and not native to Python. They function
very much like standard arrays from any other language and are very powerful
for performing fast and computationally expensive tasks. They have many
features and greater versatility which make them easier and more convenient
to use than Python's built in sequences.

Numpy arrays are so chocked full of features, this tutorial can not hope to
cover it all. For more information, go here: http://wiki.scipy.org/Tentative_NumPy_Tutorial

Note: To use arrays, import from numpy. For the purposes of this program all
functions of numpy are imported and used as np, i.e., import numpy as np was
used.
""")

#Creating arrayss
print("""
Creating Arrays
---------------
""")
print('Create array by a = np.array([1,2,3,4,5,6,7,8,9])')
print('Create multidimensional array by a = np.array([ (1,2,3), (4,5,6) ])')
print('Common numpy methods to create arrays:')
print('Cmd: np.zeros(5)\t\tResult:', np.zeros(5))
print('Cmd: np.ones(5)\t\t\tResult:', np.ones(5))
print('Cmd: np.arange(5)\t\tResult:', np.arange(5))
print('Cmd: np.arange(-2,2.5,0.5)\tResult:', np.arange(-2,2.5,0.5))
print('Cmd: arange(15).reshape(3, 5)\tResult:\n', np.arange(15).reshape(3, 5))
print('Cmd: np.logspace(1,2,5)\tResult:\n', np.logspace(1,2,10))
print('Cmd: np.linspace(1,2,5)\tResult:\n', np.linspace(1,2,10))
print('Create empty arrays by np.arange(0) or np.array([])')

#Accessing elements
print("""
Accessing Elements
------------------
""")
a = np.array([1,2,3,4,5,6,7,8,9])
print('All of array:', a)
print('Second element of array.\t\tCmd: a[1]\t\t\tReturns:', a[1])
print('1st through 4th elements.\tCmd: a[0:4]\t\t\tReturns:', a[0:4])
print('5th to last elment.\t\tCmd: a[4:]\t\t\tReturns:', a[4:])
print('Every other element.\t\tCmd: a[::2]\t\t\tReturns:', a[::2])
print('Last element.\t\t\tCmd: a[-1]\t\t\tReturns:', a[-1])
print('Conditional check of elements.\tCmd: a[a == 4]\t\t\tReturns:', a[a == 4])
print('Using array of indices.\t\tCmd: a[np.arange(0,5,2)]\tReturns:', a[np.arange(0,5,2)])

#Basic operations
print("""
Basic Operations
----------------
""")
print('Current state of array. a =', a)
print('Appending.\t\t\tCmd: np.append(a, 10)\t\t\tResult:', a)
print('Insering.\t\t\tCmd: np.insert(a, 1, 0)\t\t\tResult:', a)
print('Convert sequence to array.\tCmd: np.asarray(list(range(10)))\tResult:', np.asarray(list(range(10))))
print('Operating on each value.\tCmd: a*10\tResult:', a*10)
print('Getting single column from 2D array.\t Cmd: (np.arange(4).reshape(2,2))[0]\tResult:', (np.arange(4).reshape(2,2))[0])
print('There are lots of other things you can do that can be looked up!')
