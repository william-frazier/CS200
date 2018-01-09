#William Frazier
#CS200
#HW4
#I had some tutoring help on this program
        
def expressions(variables):
    #base case
    if len(variables) == 1:
        return [variables[0]]
    else:
        statement = []
        #for loop ensures all sections are strung together
        for i in expressions(variables[1:]):
            statement.append(str(variables[0]) + "+" + str(i))
            statement.append(str(variables[0]) + "-" + str(i)) 
            statement.append(str(variables[0]) + "*" + str(i))
        return statement
        
def unique(*arg):
    operationsList = []
    for j in (arg):
        operationsList.append(j)
    unique = set()
    fullOperations = expressions(operationsList)
    for i in fullOperations:
        print (str(i) + " = " + str(eval(i)))
        unique.add(eval(i))
    print ("Unique: " + str(len(unique)))