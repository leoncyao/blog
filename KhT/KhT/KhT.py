import sys
import os
from BNComplexes import *
from CobComplexes import *
from Drawing import *
# from CrossingTangle import *
import CrossingTangle



def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def asdf(tangle_name,tangle_path="miscellaneous", resultingdirectory=None):
    verbose = True
    if not verbose:
        blockPrint()

    filename=tangle_name
    print(tangle_path)


    filepath = "../examples/" + tangle_path + "/"
    if resultingdirectory:
        filepath += resultingdirectory
    else:
        filepath += filename
    # filename = name of example file called by kht
    # filepath = examples/<filename>/

    # print(filepath)
    # print(filename)

    # try:# assuming KhT calls file without including the '.py'-ending
    #     with open("examples/"+filename+".py", "r") as text_file:
    #         data = text_file.read()
    # except: # assuming KhT calls file with the '.py'-ending or the file does not have an ending
    #     with open("examples/"+filename, "r") as text_file:
    #         data = text_file.read()
    #         filename=filename[:-3]
        
    paths=["","/PSTricks","/BNComplexes","/CobComplexes"]
    for path in paths:
        if not os.path.exists(filepath+path):
            os.makedirs(filepath+path)
    filepath+="/"

    print("----------------")
    print("KhT, version ???")
    print("----------------")
    BNComplexes.filename = filename
    BNComplexes.filepath = filepath
    Drawing.filename = filename
    Drawing.filepath = filepath
    name = filename
    
    tangle_str_path = "../examples/"
    tangle_str_path += tangle_path
    f = open(tangle_str_path + "/" + filename + ".txt", "r")
    # f = open("../examples/asimov/asimov_1_small.txt", "r")
    tangle = f.read()
    # print(f)
    # print("TANGLE IS " + tangle)
    Tangle = CrossingTangle.Tangle(tangle)

    figured_out_tangle = True

    html_content=""

    html_content += "<h4>Arc invariant over \(\mathbb{F}_2\)</h4>"
    cx = BNbracket(tangle,0,0,1) # compute Bar-Natan's bracket
    BNr = cx.ToBNAlgebra(2) # convert the Bar-Natan's bracket into a complex over BNAlgebra
    BNr.eliminateAll() # cancel all identity components of the differential
    BNr.clean_up() # try to find the immersed curve invariant BNr through a sequence of random isotopies
    multicurve = BNr.to_multicurve()
    multicurve.save(name)
    print("name is " + name)
    test = []
    print(multicurve.comps)
    for comp in multicurve.comps:
        # print("new comp")
        # print(comp.is_looptype())
        # print(comp)
            if not comp.diff[0][-1] == 0:
                # should not be a cycle
                test.append(comp)
    multicurve.comps = test
    print(multicurve.comps)
    html_content += multicurve.html(name,"_BNr7","hdelta",Tangle)



        # for gen in comp.gens:
        #     # print(gen)
        #     # print(repr(gen))
        #     print(gen.is_looptype())
    # print(BNr)

    # html_content += "<h4>Figure-8 invariant over \(\mathbb{F}_7\)</h4>"

    # Khr = BNr.cone(1)
    # Khr.clean_up()
    # multicurveKh = Khr.to_multicurve()
    # # html_content += multicurveKh.html(name,"_Khr7","hdelta",Tangle)

    # html_content += "<h4>Arc invariant over \(\mathbb{F}_2\)</h4>"
    # cx = BNbracket(tangle,0,0,1) # compute Bar-Natan's bracket
    # BNr = cx.ToBNAlgebra() # convert the Bar-Natan's bracket into a complex over BNAlgebra
    # BNr.eliminateAll() # cancel all identity components of the differential
    # BNr.clean_up() # try to find the immersed curve invariant BNr through a sequence of random isotopies
    # multicurve = BNr.to_multicurve()
    # multicurve.save(name)

    # html_content += "<h4>Figure-8 invariant over \(\mathbb{F}_2\)</h4>"

    # Khr = BNr.cone(1)
    # Khr.clean_up()
    # multicurveKh = Khr.to_multicurve()
    # html_content += multicurveKh.html(name,"_Khr2","hdelta",Tangle)

    # html_content += multicurve.html(name,"_BNr7","hdelta",Tangle)
    # # Jones_poly = BNr.Jones()
    # # print("JONES POLY: " + Jones_poly)

    # #BNr.draw(name)

    # multicurve = BNr.to_multicurve()
    # multicurve.save(name)

    # # with open("examples/"+filename+"/"+filename+"_jones.txt", "w") as text_file:
    # #     print(Jones_poly, file=text_file)
    # # f = open("Jones.txt", "a")
    # # f.write(Jones_poly)
    # # f.close()

    if figured_out_tangle:
        # path = "../examples/" + filename + "/" + filename+".html"
        # path = "../examples/" + resultingdirectory + "/" + filename+".html"
        path = "../../_includes/" + name + ".html"
        print("saving html in " + path)
        with open(path, "w") as text_file:
            print(html_content, file=text_file)
    if not verbose:
        enablePrint()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        asdf(sys.argv[1])
    if len(sys.argv) == 3:
        asdf(sys.argv[1], tangle_path=sys.argv[2])
    if len(sys.argv) == 4:
        asdf(sys.argv[1], tangle_path=sys.argv[2], resultingdirectory=sys.argv[3])