#CS200
#William Frazier
#HW05

def expand(number, base):
    """
    Represents a number in a given base.
    For example expand(13,2) would return a string showing 13 in binary
    Use numbers 1 or larger.
    """
    
    if number <= 0:
        return ""
    else:
        return expand(number//base, base) + str(number % base)
        
def sieve(number):
    """
    Returns a list containing all primes lower than the entered number.
    Works by utilizing the Sieve of Eratosthenes.
    """
    
    fullList = []
    finalList = []
    for i in range(number-1):
        fullList.append(i+2)
    while len(fullList) != 0:
        finalList.append(fullList[0])
        j = 2
        while j * fullList[0] <= fullList[-1]:
            if j * fullList[0] in fullList:
                fullList.remove(j * fullList[0])
            j += 1
        fullList.pop(0)
    return finalList
    
def factor(number):
    """
    Returns a list containing the prime factors of a number.
    """
    
    primes = sieve(number)
    factors = []
    i = 0
    while number > 1:
        currentPrime = primes[i]
        if number % currentPrime == 0:
            factors = factors + [currentPrime]
            number = number / currentPrime
        else:
            i += 1
    return factors
    
 