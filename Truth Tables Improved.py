

def truth_table (statement):
    print ("A B C D || Y ")
    print ("-------------")
    aFlip = 1
    bFlip = 1
    cFlip = 1
    dFlip = 1
    A = True
    B = True
    C = True
    D = True
    for i in range(16):
        a = "F"
        b = "F"
        c = "F"
        d = "F"
        if aFlip == 9:
            A = False
        if 4 > bFlip:
            B = True
        if bFlip > 4:
            B = False
        if cFlip > 2:
            C = False
        if cFlip < 3:
            C = True
        if dFlip % 2 == 0:
            D = False
        if dFlip % 2 != 0:
            D = True
        if A == True:
            a = "T"
        if B == True:
            b = "T"
        if C == True:
            c = "T"
        if D == True:
            d = "T"
        if eval(statement) == True:
            Y = "T"
        if eval(statement) == False:
            Y = "F"
        print (a, b, c, d, "||", Y)
        aFlip += 1
        bFlip += 1
        cFlip += 1
        dFlip += 1
        if bFlip == 9:
            bFlip == 1
        if cFlip == 5:
            cFlip = 1
        i+=1
        