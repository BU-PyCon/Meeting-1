import numpy as np
from matplotlib.pyplot import *
from itertools import accumulate
import time


def getPrimes(upto):
    """
    Extremely fast method for generating prime numbers up to a
    specific value.

    Args:
        upto - Highest prime value to generate up to.

    Return:
        A numpy array of primes from 2 to upto parameter.
    """

    start = time.time()             #Get time at start of calculation
    
    #Start off by creating an array of odd integers. These are the
    #prime number candidates
    primes = np.arange(3,upto+1,2)

    #Create an array True boolean values which determine if the
    #numbers in primes are prime or not.
    isprime = np.ones((upto-1)/2,dtype=bool)

    #The tricky part of the code. Let's walk through this one step
    #at a time. Firstly, we loop over the array
    #
    # primes[:int(np.sqrt(upto))]
    #
    #This array goes from the first element of prime, up to the integer
    #which is the sqrt of the maximum value. Essentially, if any number
    #in primes has a divisor, it will be one of these numbers. So we
    #loop over all these factors.
    #
    #Inside the loop we check to see if the current number in our prime
    #array is still considered a prime. If it is, we then set all values
    #in the isprime array which are a multiple of this value equal to zero.
    #This is accomplished by using the isprime[(factor*3-2)/2::factor] = 0
    #command rather than another for loop. Essentially this starts from
    #the first multiple of factor, given by (factor*3-2)/2, and skips by
    #the quantity factor to the end of the array, setting all values to
    #zero along the way. Note that (factor*3-2)/2 is really the array
    #position, not the actual multiple value.
    #
    #This task utilizes a special property of numpy arrays wherein if the
    #the index is a decimal, numpy index based on floor of that value. I.e.,
    #array[1.5] actually evaluates as array[1].
    for factor in primes[:int(np.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor] = 0

    end = time.time()               #Get time at end of calculation
    
    print('Finding primes process took', round(end-start,5) , 'seconds. Onto the getPos function!')
    
    #Returns the values of primes where isprimes is still true and prepends
    #the values of one and two to the front of the array.
    return np.insert(primes[isprime],0,[1,2])

def getPos(val):
    """
    Get an array of x and y positions in the Ulam spiral for the array
    of input values in the val array. We define the Ulam spiral to start
    with the value 1 at position x = 0 and y = 0. It then moves to the right
    and circles around in a square, counter-clockwise pattern.

    Args:
        val - An array of values for which this method calculates the x and
              y positions in the Ulam spiral.

    Return:
        Returns two arrays of x and y positions which 
    """

    #This is really bad programming. The following lines do what we want
    #but they are completely obfuscated by dense and unintelligble code.
    #Essentially though, we use some math properties to figure out the
    #change in x and y as we move through the spiral.
    temp1 = np.sqrt(np.arange(1,val[-1]+1))
    temp2 = np.round(temp1)
    x = np.append(np.zeros(1),(temp1/temp2 <= 1) * (2*(temp2 % 2)-1))
    y = np.append(np.zeros(1),(temp1/temp2 >  1) * (2*(temp2 % 2)-1))

    #Now we need to sum up the values in the x and y arrays. This is by
    #far the slowest process in this function.
    #The following procedure is equivalent to
    #for i in range(1,len(x)):
    #    x[i] += x[i-1]
    #    y[i] += y[i-1]
    #However, it is always best to use native python functions which will
    #always be faster. As it turns out though, this function is barely
    #faster than the above loop.
    x = np.asarray(list(accumulate(x)))
    y = np.asarray(list(accumulate(y)))
    
    return x[val-1], y[val-1]

def plotUlam(upto):
    """
    Plot all the primes in an Ulam spiral on a plot.

    Args:
        upto - The number in the spiral to plot up to.
    """
    
    #Closes all previously opened plots
    close('all')

    start = time.time()             #Get time at start of calculation
    x, y = getPos(getPrimes(upto))  #Do the calculation
    end = time.time()               #Get time at end of calculation
    
    print('Calculational process took', round(end-start,5) , 'seconds. Onto the plotting!')

    figure(1)
    plot(x, y, ',k ', mec = 'None')
    xlim(-max(x)-1, max(x)+1)   #We want a square range for x and y
    ylim(-max(y)-1, max(y)+1)
    gca().xaxis.set_ticks([])   #Let's remove those pesky tick labels
    gca().yaxis.set_ticks([])
    gca().set_aspect(1)         #We also want a square plot for x and y
    show(block = False)
