#William Frazier
#CS200
#HW07
 
def anagrams(string):
    """
    Returns all unique anagrams possible from a given string.
    """
    
    #if size 1 or 0, return only the string in a list
    if len(string) <= 1:
        return [string]
    else:    
        # a temporary set to ensure uniqueness of anagrams
        temp = set()
        #for loop cycles through all letters in the string
        for i in range(len(string)):
            character = string[i]
            #update the string, removing the letter at index i
            updated_string = string[:i] + string[i+1:]
            #recursion call on remaining letters
            for j in anagrams(updated_string):
                temp.add(character + j)
    final_list = [] 
    #put everything in the set into a list          
    for k in temp:
        final_list.append(k)
    return final_list
        