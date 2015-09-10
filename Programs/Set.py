print("""
Short Tutorial on Sets
----------------------
Sets are mutable unorderd arrays of values. Sets are used for
comparisons, much like in boolean algebra. Importantly, sets
cannot contain duplicates! If duplicate values are passed into
a set creation, any duplicates are dropped.
""")

#Creating sets
print("""
Creating Sets
--------------
""")
print('Create set by a = set([1,2,3,4,5,6,7,8,9])')
print("Create set by a = set('abcdefg')")
print('Create set by a = {1,2,3,4,5,6,7,8,9}')
print('Create empty set by a = set(), cannot do a = {}')

#Changing elements in set
print("""
Changing Sets
-------------
""")
a = set('abcdefg')
print('Current state of set. a =', a)
print("Adding to set.\t\t\tCmd: a.add('h')\t\tResult:", a.add('h'))
print("Remove from set.\t\tCmd: a.remove('h')\tResult:", a.remove('h'), '- Returns error is element does not exist in set')
print("Remove from set if present.\tCmd: a.discard('h')\tResult:", a.discard('g'), '-tReturns no errors')
print("Remove and return last element.\tCmd: a.pop()\t\tReturns:", a.pop())
print("Remove all elements.\t\tCmd: a.clear()\t\tReturns:", a.clear())

#Set comparison
print("""
Set Comparison
--------------
""")
a = set('abracadabra')
b = set('alakazam')
print("Creating two new sets:\nCmd: a = set('abracadabra')\tResult: a = ", a, "\nCmd: b = set('alakazam')\tResult: b = ", b)
print('Letters in a but not in b.\tCmd: a-b\tResult:', a-b)
print('Letters in a or b.\t\tCmd: a|b\tResult:', a|b)
print('Letters in a and b.\t\tCmd: a&b\tResult:', a&b)
print('Letters in a xor b.\t\tCmd: a^b\tResult:', a^b)
print('Is a super set of b.\t\tCmd: a>b\tResult:', a^b)
print('Is a sub set of b.\t\tCmd: a<b\tResult:', a^b)

#Performing operations on a set
print("""
Various Operations
------------------
""")
a = set('abcdefg')
print('Note: Most operations require all elements of list be the same type.')
print('Convert other sequence types to a set by using set(var) command.')
print('Current state of set. a =', a)
print('Length of set.\t\tCmd: len(a)\t\tReturns:', len(a))
print('Max of set.\t\tCmd: max(a)\t\tReturns:', max(a))
print('Min of set.\t\tCmd: min(a)\t\tReturns:', min(a))
print("Test for element.\tCmd: 'a' in a\t\tReturns:", 'a' in a)

#Notes on list properties
print("""
Notes on set properties
-----------------------
- There was an older module called sets (as opposed to set) which functioned
  similarly, but has since been depreciated. Do not use sets.
- All set elements are necessarily hashable.
- Checking for existence of elements within a set is much faster than checking
  for existence in a tuple or list due to elements being hashed.
- There exists a frozenset sequence with many of the same properties, the only
  difference being that frozensets are immutable.
""")
