import sys
import os
from BNComplexes import *
from CobComplexes import *
from Drawing import *
from CrossingTangle import *
# goal, find the number integer describing number of twists to do to tangle, such that the tail of 
# the arc invariant chain complex dissapears

# first calculate chain complex with no twists, see how many black dots "n" at the end of the complex
# (this is mainly to check my work)
# for i in range(-10, 10):
#   calculate chain complex for tangle with i twists at bottom
#   check that the number of blacks dots becomes 0 
if __name__ == "__main__":
    name = sys.argv[1]
    f = open(name + ".txt", "r")
    tangle_str = f.read()
    tries = [0] + [(-1)**(i) * int((i)/2) for i in range(2, 50)]
    for i in tries:
        if i > 0:
            new_tangle_str = tangle_str + ".pos0" * i
        else:
            new_tangle_str = tangle_str + ".neg0" * abs(i)

        # Tangle = Tangle(new_tangle)
        cx = BNbracket(new_tangle_str,0,0,1) # compute Bar-Natan's bracket
        BNr = cx.ToBNAlgebra(2) # convert the Bar-Natan's bracket into a complex over BNAlgebra
        BNr.eliminateAll() # cancel all identity components of the differential
        # print(BNr)
        BNr.clean_up() # try to find the immersed curve invariant BNr through a sequence of random isotopies
        #BNr.draw(name)
        multicurve = BNr.to_multicurve()

        # assuming has one comp
        order = multicurve.comps[0].gens
 
        if order[0].h <= order[1].h:    
            new_name = name + "_minimal"
            f = open(new_name + ".txt", "w+")
            # print("truncated str is " + new_tangle_str[:-5])
            # print(f)
            f.write(new_tangle_str[:-5])
            
            break
            # filename = new_name
            # filepath="examples/"+filename+"/"
            # BNComplexes.filename = filename
            # BNComplexes.filepath = filepath
            # Drawing.filename = filename
            # Drawing.filepath = filepath
            # exec("__main__.py ")
        

