#William Frazier
#CS200
#Hw10

def color(graph):
    """
    Takes a graph in the style of [{"a","b"}, {"b","c"}] (can be any length, any
    variable name) and prints out the color to paint each vertex in the graph 
    (colors are given as a number).
    """
    #stores graph's vertex pairs as a list, rather than a set
    vertices = []
    #stores the degree of each point in a dict. associated with the vertex
    degrees = {}
    #stores all connections in a dict, not super efficient but it works
    connections = {}
    #integer representing a color
    colors = 1
    #list to contain vertices in order of degree (highest to lowest)
    paint = []
    #final dict to return
    final = {}
    
    #moves vertices from sets to lists
    for i in graph:
        vertices.append(list(i))
        
    for j in vertices:
        for k in range(0,2):
            #stores all connections in graph (in both directions)
            if j[k] in connections:
                connections[j[k]] += j[(k+1)%2]
            else:
                connections[j[k]] = j[(k+1)%2]
            #updates the degree of each vertex
            if j[k] in degrees:
                degrees[j[k]] += 1
            else:
                degrees[j[k]] = 1
                
    #had lots of trouble here
    #this serves to organize the vertices in "degrees" and order them...
    #high to low based on the degree of each vertex, stores in list "paint"
    while len(degrees) > 0:
        #degree will always be > 0
        max = 0
        for r in degrees:
            if degrees[r] > max:
                #find the highest degree
                max = degrees[r]
        for s in degrees:
            #if the key was associated highest value, append it to "paint"
            if degrees[s] == max:
                paint.append(s)
                #remove the maximum key:value
                del degrees[s]
                #break from the loop to avoid errors
                break
            
    #this applies the color to each vertex
    while len(paint) > 0:
        #temporary list useful for avoiding a certain bug I was having
        temp = []
        #store current color to the key, a vertex in "paint"
        final[paint[0]] = colors
        for vertex in paint:
                #if vertex is not connected to paint[0], they can be same color
                if vertex not in connections[paint[0]]:
                    #paints the vertex
                    final[vertex] = colors
                    #update temp to reflect all painted vertices
                    temp.append(vertex)
        #remove everything that was painted
        for i in temp:
            paint.remove(i)
        #change to a new color
        colors += 1
    #this could easily be return, wasn't sure what I should use
    print(final)      
    
    
#Output:
#    >>> color([{"a","b"}, {"a","c"}, {"c", "b"}, {"b", "d"}])
#{'b': 1, 'c': 2, 'd': 2, 'a': 3}

#>>> color([{"a","b"},{"b","c"}])
#{'b': 1, 'c': 2, 'a': 2}
        