print("""
Short Tutorial on Lists
-----------------------
Lists are mutable arrays of values. They can contain a collection of a
of any variable type and be of any size. One can delete elements from,
append or concatenate elements to, and iterate over them. They offer
a powerful way to collect groups of data and manage them.
""")

#Creating lists
print("""
Creating Lists
--------------
""")
print('Create list by a = [1,2,3,4,5,6,7,8,9]')
print('Create list by a = list(range(10))')
print('Create empty lists by a = [] or a = list()')
print('Create list of duplicate values by a = [1]*10')

#Accessing elements
print("""
Accessing Elements
------------------
""")
a = [1,2,3,4,5,6,7,8,9]
print('All of list:', a)
print('Second element of list.\t\tCmd: a[1]\tReturns:', a[1])
print('1st through 4th elements.\tCmd: a[0:4]\tReturns:', a[0:4])
print('5th to last elment.\t\tCmd: a[4:]\tReturns:', a[4:])
print('Every other element.\t\tCmd: a[::2]\tReturns:', a[::2])
print('Last element.\t\t\tCmd: a[-1]\tReturns:', a[-1])

#Adding to list
print("""
Adding to List
--------------
""")
print('Current state of list. a =', a)
print('Appending 0 to list.\tCmd: a.append(0)\tResult:', a.append(0))
print('Concatenating to list.\tCMD: a + [0]\t\tResult:', a+[0])
print('Appending a list.\tCmd: a.append([1,2])\tResult: ', a.append([1,2]))
print('Appending a string.\tCmd: a.append("Hello")\tResult:', a.append("Hello"))
print('Inserting elements.\tCmd: a.insert(1,-1)\tResult:', a.insert(1,-1))

#Deleting from list
print("""
Deleting from List
------------------
""")
print('Current state of list. a =', a)
del a[len(a)//2]     #Deletes middle element
print('\nDelete middle element of list. \nCmd: del a[len(a)//2] \nResult: ', a)
a.remove("Hello")
print('\nDeleting first element of input. \nCMD: a.remove("Hello") \nResult:', a)
print('\nDelete and return last element. \nCmd: a.pop() \nReturns:', a.pop())

#Performing operations on a list
print("""
Various Operations
------------------
""")
print('Note: Most operations require all elements of list be the same type.')
print('Convert other sequence types to a list by using list(var) command.')
print('Current state of list. a =', a)
print('Sum of list.\t\tCmd: sum(a)\t\tReturns:', sum(a))
print('Length of list.\t\tCmd: len(a)\t\tReturns:', len(a))
print('Max of list.\t\tCmd: max(a)\t\tReturns:', max(a))
print('Min of list.\t\tCmd: min(a)\t\tReturns:', min(a))
print('Count occurences.\tCmd: a.count(0)\t\tReturns:', a.count(0))
a.reverse()
print('Order reversed.\t\tCmd: a.reverse()\tResults:', a)
a.sort()
print('Sort list.\t\tCmd: a.sort()\t\tResults:', a)
print('Test for element.\tCmd: 5 in a\t\tReturns:', 5 in a)
print('Find index of 5.\tCmd: a.index(5)\t\tReturns:', a.index(5))
a = list(range(10))
b = a       #Copy reference to a

c = a[:]    #Copy elements of a
print('\nCreated two new lists from a.\na: ', a, '\nCmd: b = a\tResult:', b, '\nCmd: c = a[:]\tResult:', c)
b[0] = -1
print('\nRedefining b. Cmd: b[0] = -1\na: ', a, '\nb: ', b)
a = list(range(10))
c[0] = -1
print('\nRedefining c, Cmd: c[0] = -1\na: ', a, '\nc: ', c)


#Notes on list properties
print("""
Notes on list properties
------------------------
- Lists are collections of references, not objects. Hence the following
    a = [1000]
    a[0] is 1000 #Returns false

- Time to get or set elements is O(1).
- Time to append elements is "amortized constant". List dynamically
  allocates when necessary.
- Insertion and deletion is O(n) and should be avoided if list is large.
- Faster to get elements from end (using pop()) rather than from beginning
  (using pop(0)).
- Due to the pop and append methods, lists make great stacks.
- Tip: Doing a[False] returns the first element of the list and a[True]
  returns the second element of the list. Any conditionals that return
  True or False can be used in this way as well.
""")
