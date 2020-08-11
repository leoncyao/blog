import sys
import os
from BNComplexes import *
from CobComplexes import *
from Drawing import *
from CrossingTangle import *

import KhT
import ConcatWebpages

def num_gens(tangle_str):
    cx = BNbracket(tangle_str,0,0,1) # compute Bar-Natan's bracket
    BNr = cx.ToBNAlgebra(2) # convert the Bar-Natan's bracket into a complex over BNAlgebra
    BNr.eliminateAll() # cancel all identity components of the differential
    BNr.clean_up() # try to find the immersed curve invariant BNr through a sequence of random isotopies
    multicurve = BNr.to_multicurve()

    # assuming chain complex is in first index

    if len(multicurve.comps) == 1:
        return len(multicurve.comps[0].gens)    
    else:
        for comp in multicurve.comps:
            incident_to_0 = 0
            for i in range(len(comp.gens)):
                if comp.diff[0][i] != 0:
                    incident_to_0 += 1
            for j in range(len(comp.gens)):
                if comp.diff[j][0] != 0:
                    incident_to_0 += 1
            if incident_to_0 != 2:
                return len(comp.gens)
        # for comp in multicurve.comps:
        # print("new comp")
        # print(comp.is_looptype())
        # print(comp)
            # if not comp.diff[0][-1] == 0:
                # should not be a cycle
                # return len (comp.gens)


def main(name, tangle_path=None, resultingdirectory=None):
    print("------------------------------------------------------")
    print("STARTING SMALL ARC CALCULATION")
    print("------------------------------------------------------")
    tangle_path_str = "../examples/"
    if tangle_path:
        tangle_path_str += tangle_path
    else:
        tangle_path_str += "miscellaneous"
    tangle_path_str += "/"
    f = open(tangle_path_str + name + ".txt", "r")
    # print(tangle_path_str + name + ".txt")
    tangle_str = f.read()
    # print("tangle_str: " + tangle_str)
    


    # compute adding 1 pos twist and 1 neg twist seperately, to see which direction i should twist in to
    # find the 'small' arc invariant
    
    original_gens = num_gens(tangle_str)
    pos_gens = num_gens(tangle_str + ".pos0")
    neg_gens = num_gens(tangle_str + ".neg0")

    if pos_gens < original_gens or neg_gens < original_gens:

        # i don't think its possible for them to be equal
        if pos_gens < neg_gens:
            twist_str = ".pos0"
        else:
            twist_str = ".neg0"

        print("twist_str is " + twist_str)
    
        KhT.asdf(name, tangle_path=tangle_path, resultingdirectory=name)

        cur_tangle_str = tangle_str
        next_tangle_str = tangle_str + twist_str

        cur_num_gens = num_gens(cur_tangle_str)
        next_num_gens = num_gens(next_tangle_str)

        while True:
            cur_num_gens = next_num_gens
            cur_tangle_str = next_tangle_str

            next_tangle_str = cur_tangle_str + twist_str
            next_num_gens = num_gens(cur_tangle_str)

            if cur_num_gens <= next_num_gens:
                break
    else:
        # already minimal 
        next_tangle_str = tangle_str
        
    print("FOUND SMALL with tangle_str: " + next_tangle_str)
    
    # want to start are on a white dot
    new_name = name + "_small" 
    f = open(tangle_path_str + new_name + ".txt", "w")
    f.write(next_tangle_str)
    f.close()
    KhT.asdf(new_name, tangle_path=tangle_path, resultingdirectory=name)

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
    #         new_name = name + "_small"
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
        

