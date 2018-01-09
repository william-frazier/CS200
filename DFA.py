#William Frazier
#CS200
#HW11

def states():
    """
    Simple function that returns a list comprised of user imput, separated by
    spaces. Used as the states in the DFA.
    """
    
    print("State names: ", end='')
    states = input().split()
    return states
    
def alphabet():
    """
    Simple function that returns a list comprised of user input, separated by
    spaces. Used as the alphabet in the DFA.
    """
    
    print("Alphabet: ", end='')
    alphabet = input().split()
    return alphabet
    
def transitions(states, alphabet):
    """
    Function that takes a list of states and a list of the alphabet and returns
    a dictionary in the form {(state, alphabet): 0} for all possible 
    combinations.
    """
    
    transitions = {}
    for i in states:
        for j in alphabet:
            combinations = (i, j)
            transitions[combinations] = 0
    return transitions
    
def combinations(states, alphabet, transitions):
    """
    Allows the user to set where the transitions go by requesting user input in
    a table. UI should be pretty self-explanitory. Returns these transitions in
    a dictionary in the form {(state, alphabet): end point of transition}.
    """
    
    currentState = []
    print("Enter transition table: \n     ", end='')
    for i in states:
        print(i, '', end='')
        currentState.append(i)
    print(' ')
    for j in alphabet:
        m = 0
        print('', j, ": ", end='' )
        endState = input().split()
        for k in endState:
            transitions[(currentState[m], j)] = k
            m +=1
    return transitions
    
def start():
    """
    Simple function that requests a start location from the user and returns
    it as a string.
    """
    
    print('Start state: ', end='')
    return input()

def ends():
    """
    Simple function that requests end locations from the user and returns them
    as a list, separated by spaces.
    """
    
    print('Final states: ', end='')
    return input().split()
    
def simulate():
    """
    Combination of all proceeding functions. Fully simulates a DFA and prompts
    the user for a string to test, returning either True or False.
    """
    
    stat = states()
    alph = alphabet()
    tran = transitions(stat, alph)
    combs = combinations(stat, alph, tran)
    location = start()
    end = ends()
    print("Enter a string to test: ", end='')
    string = input()
    for i in string:
        location = combs[(location, i)]
    if location in end:
        return True
    else:
        return False
    