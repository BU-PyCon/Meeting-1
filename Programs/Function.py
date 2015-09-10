print("""
Short Tutorial on Functions - part I
------------------------------------
Functions offer a way of containing a small bit of repeatable code which can
be called from within a program. They have the ability to have parameters
passed into them and can return new parameters. Unlike other languages, Python
uses duck typing which means input and output types are not specified. Rather
Python checks what it acts like and then treats it like that type (if it looks
like an int and acts like an int, it must be an int - hence duck typing).

The following is a layout of the general form of a function:

def function_name( parameters ):
    "function_docstring"
    function_suite
    return [expression]

Note the colon after the list of parameters and the indentation of the sequential
lines. Just like all other blocks, this is how Python knows which lines are a
part of the function.

Python is a very "fly by the seat of your pants" programming language. Unlike
other languages which try to restrict the user to doing only those things which
they should be able to do, Python takes the approach of "better to ask for
forgiveness than permission". In other words, Python does not make any attempt
to restrict the user from passing whatever it wants into a function. It is
up to the user to be self-conscious of what they should be passing and the
creator of the function to try and anticipate what the user may try to do.
Python plays no intermediate roll in facilitating that creators and users play
nice with each other.
""")

print("""
Parameter Input
---------------
Functions can take in parameters as input. These parameters can be of any type.
Shown below are three simple functions which take various parameter types.

def func1():
    return "Hello World!"

def func2(x):
    return x*x

def func3(m, x, b = 3):
    return m*x + b

Call the docstrings on these functions to get more info. This can be acheived by
help( func_name ).
""")

def func1():
    """
    Super basic function.
    
    Args:
        None
        
    Returns:
        A string containing "Hello World!"
    """
    return "Hello World!"

def func2(x):
    """
    More complicated function which accepts an input variable of name x.
    
    Args:
        x - This should be a number!
        
    Returns:
        The square of the input value.
    """
    return x*x

def func3(m, x, b = 3):
    """
    Even more complicated function which accepts three parameters and
    automatically assigns a value to the last one of three. This means
    one could call this function with func3(10,3) or func3(10,3,10).
    The first case automatically assumes b = 3 since no input was given
    for it.
    
    Args:
        m - The slope, a number
        x - The x value, another number
        b - The y intercept, a third number. This is optional and 3 by default
        
    Returns:
        The y value for the input line.
    """
    return m*x + b


print("""
Parameter Returns
-----------------
Functions offer a powerful way to return parameters. Firstly, unlike some older
languages, the returns are never input. That is, if a parameter is passed into
the function, the value it attains in that function is only known to the function
and not to the caller. Secondly, unlike some newer languages, Python functions
can return multiple values. Again, with duck typing, their type does not need
to be specified to the user. Below are two examples of returning in functions.

def isEven(x):
    if (type(x) == int):
        if (x%2 == 0): return True
        if (x%2 == 1): return False
    return

def getFirstTwoElems(x):
    if (type(x) == list and len(x) >= 2):
        return x[0], x[1]
    return
""")

def isEven(x):
    """
    Checks if the input parameter is an even number. Nothing is returned if the
    input is not an integer.
    
    Args:
        x - This should be an int!
        
    Returns:
        True if even, False if odd, Nothing otherwise
    """
    if (type(x) == int):
        if (x%2 == 0): return True
        if (x%2 == 1): return False
    return

def getFirstTwoElems(x):
    """
    Gets the first two elements of a list.
    
    Args:
        x - This should be a list! Should also be of length 2 or larger.
        
    Returns:
        The first two elements of the list as separate components.
    """
    if (type(x) == list and len(x) >= 2):
        return x[0], x[1]
    return

print("""
Scope within Functions
----------------------
All defined variables in any python code have scope. Scope is the region
of the code where the program knows about the existence of that variable.
A variable defined within a function has a scope only within that function,
i.e., you cannot access it outside the function because it has been
garbage collected once the function returns and the variable is no longer
accessible.

The following is an example code that creates a variable funcParam within
a function which is then returned.

def scopeEx():
    funcParam = 5
    return funcParam1

Run this function and then try to print out funcParam. You'll find that
Python does not know how to access it because it does not exist.

Unlike some other languages, you generally cannot create static variables
inside a function and should simply make them global if that is required.
""")
def scopeEx():
    """
    Allows you to see the scope of variables within a function. This function
    creates a variable called funcParam, sets it equal to 5, and returns it.
    Try to print funcParam after calling this function to see if you can.
    
    Args:
        None.
        
    Returns:
        Value of funcParam
    """
    funcParam = 5
    return funcParam

print("""
Hiding the Field
----------------
Python allows you to "Hide the field". This is a process where you create
a variable in a function with the same name as a global variable. This
means the variable in the function "Hides" the existence of the global
variable and any references to that variable within the function do
not affect the global variable.

Try this out by first printing the variable "var", then running the method
below which creates a variable called "var" as well and seeing what it
prints out.

var = "Hello World!"
def hidingField():
    var = 5
    print("Created variable called var with value: ", var)

""")
var = "Hello World!"
def hidingField():
    """
    Simple function which creates a variable called var and prints it out.
    Note that var has already been defined globally (you can see this your-
    self by just printing var and you should get "Hello World!").
    
    Args:
        None.
        
    Returns:
        None.
    """
    var = 5
    print("Created variable called var with value: ", var)

print("""
Passing by Reference vs. Values
-------------------------------
Python is a pass-by-reference language. All variables in python are nothing more
than references (or pointers as other languages might call them) to the memory
space where the value of the variable is stored. When you send a variable as
input to a function, you are passing not the value, but the reference to the
memory space. This means that any variables in the function that get this
reference have the ability to change the same memory space as the input variable.
This could potentially have drastic consequences since it could mean unknowingly
altering a global variable unintentionally. The following functions illustrate
this potentiality.

globalListVar = list(range(10))
def changeGlobalVar(listVar):
    listVar.append(10) #Changes globalListVar as well!
    print(listVar)

def doesntChangeGlobalVar(listVar):
    listVar = list(range(9,-1,-1)) #Doesn't change globalListVar
    print(listVar)
""")
globalListVar = list(range(10))
def changesGlobalVar(listVar):
    """
    This method takes in a list and appends the int 10 to the end of it. However
    the param listVar is given only the reference to the input list. This means
    that changing listVar changes anything pointing to the same memory space,
    which is necessarily going to be the input variable. Print out globalListVar,
    run this program inputting globalListVar, then print out globalListVar again.
    
    Args:
        listVar - A list
        
    Returns:
        None.
    """
    listVar.append(10) #Changes globalListVar as well!
    print('listVar =', listVar)

def doesntChangeGlobalVar(listVar):
    """
    Another example which does not change the input parameter. This is due to the
    fact that the equals sign is inherently reassigning the reference of the
    listVar variable. Rather than resetting what is in the memory space listVar
    was originally pointing to, reassignment simply creates a new memory space for
    the new data and points listVar to this new memory space. Now listVar has no
    association with the old globalListVar which was input. Print out globalListVar,
    run this program inputting globalListVar, then print out globalListVar again.

    Args:
        listVar - A list
        
    Returns:
        None.
    """
    listVar = list(range(9,-1,-1)) #Doesn't change globalListVar
    print('listVar =', listVar)

print("""
Recursion
---------
Python supports recursion which is simply the ability for a function to call on
itself. Recursive functions can be very useful for certain practices such as
searching and performing tasks which rely on themselves. One of the important
features of a recursive function is that it needs to have some way of breaking
the recursion. Generally this is done when a certain condition is met based
on the input parameters.

When a function calls itself, the current data remains on the stack (one of
the memory banks given to each program) and a new instance of the function is
created. This implies that recursion cannot proceed indefinitely and there is
a maximum "recursion depth" before you run out of memory. If necessary, higher
depths can be acheived by

sys.setrecursionlimit( higher_depth )

Note that python is not particularly efficient as a tail-call language. This
means that you should generally use recursion sparingly, and not if the task
can  be done in some other manner. Below is a simple, and quintessential recusion
function which calculates the n^th fibonacci number.

def fib_recursive(n):
    if (n == 1): return n
    return fib(n-1) + fib(n-2)

As mentioned above, recursion, while useful, is not always the best way to go
about things. Below is a function which uses other features of python to do
the same thing, and isn't recursive.

def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
""")
def fib_recursive(n):
    """
    Recursive method which calls itself to calculate the n^th fibonacci number.
    
    Args:
        n - The n^th fibonacci number to calculate.
        
    Returns:
        The n^th fibonacci number (how many times do I have to tell you this?)
    """
    if (n == 1 or n == 2): return n
    return fib(n-1) + fib(n-2)

def fib_iter(n):
    """
    Non-recursive method which uses lists and looping to calculate the n^th
    fibonacci number.
    
    Args:
        n - The n^th fibonacci number to calculate.
        
    Returns:
        The n^th fibonacci number (how many times do I have to tell you this?)
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print("""
Lambda Functions
----------------
Also known as anonymous functions, these are functions which can be created on
the fly and have no association with a particular program, class, or object.
Lambda functions are meant to be short and simple and can only have a single
expression which is returned to the user. No assignment or any other process
is allowed. The syntax is as follows

lambda [arg1 [,arg2,.....argn]]:expression

One could create a simple lambda function which squares the input.

f = lambda x: x*x

The lambda function has been stored into the variable f, making f a function
now. One can call it by f(2). Another example

g = lambda a, b: a + b

An important feature of functions has been shown here, that they can be assigned
to variables just like any other data type. This means functions can be copied
and passed around to other functions.
""")
f = lambda x: x*x
g = lambda a, b: a + b
