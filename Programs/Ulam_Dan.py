""" 
This solution was created by Dan, in collaboration with Connor, Taylor,
Eunkyu, Chris, Aurora, and Brandon. Though not as efficient as
Brandon's algorithm, I wanted to show other ways to approach this Ulam
spiral problem and some other Python tricks in practice. I didn't time
any of this so while some of the algorithms herein are slower than
Brandon's, some of them might not be.
"""

# We require three modules to import -- two should look familiar.
# The third, numpy.ma is an offshoot of numpy good for creating and
# manipulating "masked arrays" that have some values masked. This is
# ofthen used in arrays with bad pixels or data values in science.
import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma

def ulam_spiral(max_):
    """Create an Ulam spiral plot consisting of primes up to a maximum
    value.
    
    Arguments:
        max_ -- The maximum number utilized in the Ulam spiral.
    
    Outputs:
        primes -- A numpy array containing all prime numbers up to "max_"
        
        spiralArr -- A masked numpy array containing the spiral grid 
                     plotted in the image.
    """
    
    # This function creates an Ulam spiral, which is a spiral made up of
    # prime numbers. It is not an independent function, as it makes use
    # of a function defined later in the code, namely spiral_grid(). More
    # on that later...
    
    # First we have to build our array of prime numbers up the maximum
    # value given by the "max_" argument. For our algorithm to work,
    # we cannot put 1 in the array until the end, so we instead 
    # initialize it with a 2:
    primes = np.array([2])
    
    # We now want to build up this array with prime numbers. We will
    # start with 3, the next available number, and work our way up,
    # skipping all even numbers because we know they are not primes.
    # To work our way up, we will use a for loop; please note that 
    # for us to consider the number "max_", we have to end at max_+1:
    for num in range(3,max_+1,2):
        # To check if the number is prime, we have to compare it to all
        # prime numbers below the square root of the number in question:
        root        = np.floor(np.sqrt(num))
        primeArr    = num % primes[primes<=root]
        # primeArr now contains the number in question modulo all primes
        # lower than its root. In order for it to be prime, it must have
        # no zero values, i.e., all "True", checked by the .all() method:
        if primeArr.all():
            primes  = np.append(primes, num)

    # Now that the loop has finished, we have all of the primes, except
    # one, which you recall we couldn't add (because any number modulo
    # one is zero). So we'll now append 1 to the front of the array:
    primes = np.append(1, primes)
    
    # Armed with all the primes, we must create a spiral grid from which
    # we can create the Ulam spiral. To do this, we will once again need
    # the integer square root of the max_ argument, as it will be the
    # length of the spiral box needed for the grid:
    sideLength  = np.floor(np.sqrt(max_))
    
    # We now have to create the grid. This is done using the
    # spiral_grid() function. If you haven't yet, you should jump to that
    # function's code below, and then come back.
    
    # Ok, we will create a 2 x 2 spiral grid of length "sideLength" and
    # then flatten it (to a 1-D array) using the .flatten() method:
    spiralArr1d = spiral_grid(sideLength).flatten()
    
    # This next step has two things going on, so let me walk you through.
    # The numpy module has a function called in1d(), which will take
    # two 1-D arrays and return a comparison of which entries in the
    # first array are also found in the second. As such, the output
    # is a boolean array the size of the first array with True values
    # where they matched and False values where they didn't. We want to
    # compare the spiral 1-D array with the primes. However, we want the
    # primes themselves, so we use the "invert" keyword argument to put
    # a False value where the primes are, and a True where they aren't.
    # We then will use numpy.ma to mask all the values where we have
    # "True" values from the previous comparison, i.e., the non-primes.
    # Once that is done, we use the .reshape() method to return it to a
    # spiral grid. If you print this out, you will get a numerical
    # representation of the Ulam spiral:
    spiralArr1d[np.in1d(spiralArr1d,primes, invert=True)] = ma.masked
    spiralArr   = spiralArr1d.reshape(sideLength, sideLength)
    
    # Ok, now we just have to make the plot. Instead of figuring out an
    # x axis like Brandon does so he can use plt.plot(), I will use 
    # matplotlib's image plotting routine. The downside is it will
    # color code the points and weigh them to the outer points, since
    # they have higher values (I'm not reducing primes to ones).
    # So to plot an image, you use plt.imshow(). Don't worry too much
    # about these parameters, but if you're curious, it's documented on
    # the matplotlib website:
    plt.imshow(spiralArr, cmap='gray', interpolation='nearest')
    plt.savefig('ulam_spiral_dan.pdf', dpi=300)
    
    # And we're done! Once you close the plot, the function returns both
    # the array of prime numbers, and the spiral grid used in the plot.
    return primes, spiralArr

def spiral_grid(box_length):
    """Return a spiral grid of the inputted length. This box length
    can be either odd or even.
    
    Arguments:
        box_length -- the length of each side of the grid.
        
    Outputs:
        grid -- the square spiral grid.
    """
    
    # Part of why I put this function here is to illustrate that it
    # doesn't matter the order of the functions you create in a 
    # module, even if the above ones reference the below ones. It is
    # good practice to separate independent functions from dependent
    # ones, and to put the dependent ones on bottom...oops.
    
    # First, I test for the simplest case, and reject anyone annoying
    # enough to try to use this code to make a 1 x 1 spiral grid:
    if box_length == 1 or box_length == 1.0:
        raise ValueError('SPIRAL_GRID: Cannot make spiral grid of length 1.')
    
    # Now I create the skeleton of the grid, an array of zeros
    # of the correct length to be filled in later:
    grid      = np.zeros([box_length, box_length])
    
    # Now I find which index in the grid will hold the value 1:
    oneIndex  = int(box_length - 1) // 2
    grid[oneIndex, oneIndex] = 1
    
    # This algorithm is a bit dense to read on its own, so let me walk
    # you through it in words and then let you parse it with what it's
    # doing in mind. I'm first creating an array with all the numbers
    # from 1 to the max number in the grid which will fill into the grid
    # itself (e.g., in a 5 x 5 grid, a 25 integer array). I then have to
    # keep track of 3 things as I fill in the spiral grid: the length of
    # the side I'm filling in (Length), the position in the number array
    # of the values I'm about to fill in (startIndex), and my current
    # position I'm located in the spiral grid (position). I fill in the
    # values in up to down and then left to right when the length is odd,
    # and fill them in down to up and then right to left when the length
    # is even (checked by Length % 2). I continue this until Length is
    # equal to box length. At that point, I fill in the final piece of
    # the spiral, which depends on whether we have an even or odd grid.
    # Ok, let's dive in:
    
    # Some housekeeping initializations:
    num_array  = np.arange(box_length*box_length) + 1
    Length     = 1
    startIndex = 0
    position   = [oneIndex, oneIndex]
    # Using a while loop...could be a for loop but this seemed easier:
    while Length < box_length:
        # If we are filling in odd length:
        if Length % 2 is 1:
            grid[(position[0]+1):(position[0]+Length+1),(position[1])] = \
                num_array[startIndex+1:startIndex+Length+1]
            grid[(position[0]+Length),(position[1]+1):position[1]+Length+1] = \
                num_array[startIndex+Length+1:startIndex+Length+Length+1]
            position   = [position[0]+Length, position[1]+Length]
            startIndex = int(startIndex + (Length*2))
        # If we are filling in even length, do this instead. You'll see
        # in here the usage of np.flipud(), which flips an array in the
        # "up-down" direction. This is because when I fill in numbers
        # from down to up or right to left, I'm filling in backwards, so
        # I have to flip the array of numbers to be filled in:
        elif Length % 2 is 0:
            grid[(position[0]-Length):position[0], position[1]] = \
                np.flipud(num_array[startIndex+1:startIndex+Length+1])
            grid[position[0]-Length,position[1]-Length:position[1]] = \
                np.flipud(num_array[startIndex+Length+1:startIndex+ \
                                    (Length*2)+1])
            position   = [position[0]-Length, position[1]-Length]
            startIndex = int(startIndex + (Length*2))
        Length += 1
    # You'll notice I used backslashes to continue long lines rather than
    # using parenthetical continuations. This is because the code already
    # had a lot of parentheses and I didn't want to compound the density
    # of parentheses. Remember, readability > convention. I also have a
    # tendency to line up many of my nearby equal signs. This is not
    # convention but I find it to be much more readable--it's not a 
    # requirement for you to do, but I like it a lot.
    
    # Finish up the last section of grid, depending on even or odd grid:
    if box_length % 2 is 1:
        grid[1:box_length,0]    = num_array[int((box_length-1)*-1):]
    elif box_length % 2 is 0:
        grid[0:box_length-1,-1] = np.flipud(num_array[int((box_length-1)*-1):])
    
    # Done!
    return grid
