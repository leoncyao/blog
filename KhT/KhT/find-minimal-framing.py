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
    filename=sys.argv[1]
    filepath="examples/"+filename+"/"
    f = open(filename + ".txt", "r")
    tangle_str = f.read()
    tries = [0] + [(-1)**(i) * int((i)/2) for i in range(2, 14)]
    # tries = [1]
    print(tries)
    results = []
    for i in tries:
        if i > 0:
            new_tangle_str = tangle_str + ".pos0" * i
        else:
            new_tangle_str = tangle_str + ".neg0" * abs(i)
        BNComplexes.filename = filename
        BNComplexes.filepath = filepath
        Drawing.filename = filename
        Drawing.filepath = filepath
        # Tangle = Tangle(new_tangle)
        cx = BNbracket(new_tangle_str,0,0,1) # compute Bar-Natan's bracket
        BNr = cx.ToBNAlgebra(2) # convert the Bar-Natan's bracket into a complex over BNAlgebra
        BNr.eliminateAll() # cancel all identity components of the differential
        # print(BNr)
        BNr.clean_up() # try to find the immersed curve invariant BNr through a sequence of random isotopies
        #BNr.draw(name)
        multicurve = BNr.to_multicurve()
        multicurve.save(filename)

        # assuming has one comp
        order = multicurve.comps[0].gens
        if order[0].h <= order[1].h:
            print("has no tail")
            results.append("Minimal")
        else:
            results.append("not Minimal")
        for gen in multicurve.comps[0].gens:
            print(gen)
        
        # print(BNr)
    print(tries)
    print(results)
    # with open("examples/template.py", "r") as text_file:
    #     data = text_file.read()

    # paths=["","/PSTricks","/BNComplexes","/CobComplexes"]
    # for path in paths:
    #     if not os.path.exists('examples/'+filename+path):
    #         os.makedirs('examples/'+filename+path)

