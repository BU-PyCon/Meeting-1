print("""
Short Tutorial on Dictionaries
------------------------------
Dictionaries are a poor man's object, akin to structs in other
languages. Think of them like arrays (or lists), except instead
of each element having an index that defines its position in the
array, each element is defined and accessed by a keyword. Thus
Dictionaries are defined by specifying a set of keys and values.
Dicts are mutable and implemented as hash tables under the hood.
This means they are very fast at accessing and storing elements.
""")

#Creating dicts
print("""
Creating Dictionaries
---------------------
""")
print('Create dictionary by a = dict(one=1, two=2, three=3)')
print("Create dictionary by a = {'one': 1, 'two': 2, 'three': 3}")
print("Create dictionary by a = dict(zip(['one', 'two', 'three'], [1, 2, 3]))")
print("Create dictionary by a = dict([('two', 2), ('one', 1), ('three', 3)])")
print("Create dictionary by a = dict({'three': 3, 'one': 1, 'two': 2})")
print('Create empty dictionaries by a = {} or a = dict()')

#Accessing elements
print("""
Accessing Elements
------------------
""")
a = dict(a=1,b=2,c=3)
print('All of dict:', a)
print("Second element.\tCmd: a['b']\tReturns:", a['b'])
print("Get third element.\tCmd: a.get('c')\tReturns:", a.get('c'))
print("Check if key exists.\tCmd: 'a' in a\tReturns:", 'a' in a)

#Adding to dict
print("""
Adding to List
--------------
""")
print('Current state of list. a =', a)
a['d'] = 4
print("Add new key/elem pair.\tCmd: a['d'] = 4\tResult:", a)

#Deleting from dict
print("""
Deleting from List
------------------
""")
print('Current state of list. a =', a)
del a['d']
print("Delete 'd' element.\t\tCmd: del a['d']\tResult:", a)
print("Delete and return 'c' element.\tCmd: a.pop('c')\tReturns:", a.pop('c'))
print("Clear all elements.\t\tCmd: a.clear()\tReturns:", a.clear())

#Performing operations on a dict
print("""
Various Operations
------------------
""")
a = dict(one=1, two=2, three=3, four=4)
print('Current state of dictionary. a =', a)
print('Length of dict.\t\t\tCmd: len(a)\tReturns:', len(a))
print("Get all keys.\t\t\tCmd: a.keys()\tReturns:", a.keys())
print("Get all values.\t\t\tCmd: a.values()\tReturns:", a.values())
print("Get all key, values pairs.\tCmd: a.items()\tReturns:", a.items())



#Notes on dict properties
print("""
Notes on dict properties
------------------------
- All key names must be "hashable". Essentially any name which is valid for a
  variable name is hashable.
- Values can be any python object or datatype.
""")
