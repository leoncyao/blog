import sys
import os
from BNComplexes import *
from CobComplexes import *
from Drawing import *
from CrossingTangle import *

import KhT

# goal, find the number integer describing number of twists to do to tangle, such that the tail of 
# the arc invariant chain complex dissapears

# first calculate chain complex with no twists, see how many black dots "n" at the end of the complex
# (this is mainly to check my work)
# for i in range(-10, 10):
#   calculate chain complex for tangle with i twists at bottom
#   check that the number of blacks dots becomes 0 
def main(name, tangle_path=None, resultingdirectory=None):
    name = sys.argv[1]
    tangle_path_str = "../examples/"
    if tangle_path:
        tangle_path_str += tangle_path
    else:
        tangle_path_str += "miscellaneous"
    tangle_path_str += "/"
    f = open(tangle_path_str + name + ".txt", "r")
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
            f = open(tangle_path_str + new_name + ".txt", "w+")
            # print("truncated str is " + new_tangle_str[:-5])
            # print(f)
            f.write(new_tangle_str[:-5])
            f.close()
            print("check" + sys.argv[1])
            if len(sys.argv) == 2:
                KhT.asdf(new_name)
            if len(sys.argv) == 3:
                KhT.asdf(new_name, resultingdirectory=resultingdirectory)
            if len(sys.argv) == 4:
                KhT.asdf(new_name, tanglepath=tangle_path, resultingdirectory=resultingdirectory)
            break
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
# if __name__ == "__main__":
    # name = sys.argv[1]
    # tangle_path = "../examples/"
    # if len(sys.argv) > 3:
    #     tangle_path += sys.argv[3]
    # else:
    #     tangle_path += "miscellaneous"
    # # f = open(name + ".txt", "r")
    # tangle_path += "/"
    # f = open(tangle_path + name + ".txt", "r")
    # tangle_str = f.read()
    # tries = [0] + [(-1)**(i) * int((i)/2) for i in range(2, 50)]
    # for i in tries:
    #     if i > 0:
    #         new_tangle_str = tangle_str + ".pos0" * i
    #     else:
    #         new_tangle_str = tangle_str + ".neg0" * abs(i)

    #     # Tangle = Tangle(new_tangle)
    #     cx = BNbracket(new_tangle_str,0,0,1) # compute Bar-Natan's bracket
    #     BNr = cx.ToBNAlgebra(2) # convert the Bar-Natan's bracket into a complex over BNAlgebra
    #     BNr.eliminateAll() # cancel all identity components of the differential
    #     # print(BNr)
    #     BNr.clean_up() # try to find the immersed curve invariant BNr through a sequence of random isotopies
    #     #BNr.draw(name)
    #     multicurve = BNr.to_multicurve()

    #     # assuming has one comp
    #     order = multicurve.comps[0].gens
    #     if order[0].h <= order[1].h:    
    #         new_name = name + "_minimal"
    #         f = open(tangle_path + new_name + ".txt", "w+")
    #         # print("truncated str is " + new_tangle_str[:-5])
    #         # print(f)
    #         f.write(new_tangle_str[:-5])
    #         f.close()
    #         print("check" + sys.argv[1])
    #         if len(sys.argv) == 2:
    #             KhT.asdf(new_name)
    #         if len(sys.argv) == 3:
    #             KhT.asdf(new_name, resultingdirectory=sys.argv[2])
    #         if len(sys.argv) == 4:
    #             KhT.asdf(new_name, tanglepath=sys.argv[2], resultingdirectory=sys.argv[3])
    #         break
        

