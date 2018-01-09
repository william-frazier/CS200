#William Frazier
#hw09
#CS200
#Brendan provided a fair amount of tutoring help on the hanoi problem, I was very stuck

def BSWNRZ(length):
    """
    Returns a list of all possible bit sequences of a given length with
    no repeating zeroes (00).
    """
    
    #no bit sequences possible
    if length == 0:
        return [] 
    #hard coding the base case
    elif length == 1:
        return ['1', '0']
    else:
        #use a set so as to only return unique results
        final = set()
        #recursive call to build strings
        for i in BSWNRZ(length-1):
            #can add a 0 to the end only if string ends in a 1
            if i[-1] == "1":
                j = i + '0'
                final.add(j)
            #can always add a 1 to the end
            i += '1'
            final.add(i)
        #return in list format
        return list(final)
        
        
def hanoi(numDisks, start="A", end="B", spare="C", alt=1):
    """
    Plays out the game Tower of Hanoi by printing the correct moves.
    Merely enter "hanoi(n)" to play a game with n disks.
    """
    
    #the base case
    if numDisks == 1:
        print("Move disk", numDisks, "from peg", start, "to peg", end)
    #necessary check in order to move the larger disk
    elif alt == 0:
        print("Move disk", numDisks, "from peg", start, "to peg", end)
    else:
        #plays the game with one less disk, swapping the destination peg and the extra peg
        hanoi(numDisks-1, start, spare, end)
        #moves the largest disk to the correct position
        hanoi(numDisks, start, end, alt=0)
        #moves stack built on the spare peg to the destination peg
        hanoi(numDisks-1, spare, end, start)
    
    #I was really confused on this, could not have even gotten started (let alone finished)
    #without lots of help from Brendan at tutoring. He was very helpful.
 
        
        