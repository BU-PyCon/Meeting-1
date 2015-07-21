# Exception Handling and debugging

import pdb

# First, create a list with some values inside it:
list1  = [1,2,'wow', 34.1]

# Now, we will iterate over the list, where var is the value in the list.
for var in list1:
    # Let's try to add 3 to the value of var:
    try:
	    var2 = var + 3
    # If we cannot add 3 because it's the wrong type, it will raise
    # a TypeError. This will catch that exception if raised:
    except TypeError:
	    print('This variable is not a number!')
    # This else code will execute if no exceptions are raised:
    else:
        print(var2)
    # The finally statement will execute no matter what else happens:
    finally:
        print('\nMoving on...')

#pdb.set_trace()

for index, num in enumerate(range(10)):
    try:
        value = num / (index - 4)
    except ZeroDivisionError:
        raise ValueError('Dude, do you not know how to do math?')
    finally:
        print(value,'\n')

