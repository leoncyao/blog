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

def asdf(tangle_name,tangle_path=None, resultingdirectory=None):
    verbose = False
    if not verbose:
        blockPrint()
    filename=tangle_name
    if resultingdirectory:
        filepath="../examples/" + resultingdirectory
    else:
        filepath="../examples/"+filename
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
    if tangle_path:
        tangle_str_path += tangle_path
    else:
        tangle_str_path += "miscellaneous"
    f = open(tangle_str_path + "/" + filename + ".txt", "r")
    tangle = f.read()

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
    html_content += multicurve.html(name,"_BNr7","hdelta",Tangle)
    # print(BNr)
    # html_content += "<h4>Figure-8 invariant over \(\mathbb{F}_7\)</h4>"

    # Khr = BNr.cone(1)
    # Khr.clean_up()
    # multicurveKh = Khr.to_multicurve()
    # # html_content += multicurveKh.html(name,"_Khr7","hdelta",Tangle)

    # # html_content += "<h4>Arc invariant over \(\mathbb{F}_2\)</h4>"
    # cx = BNbracket(tangle,0,0,1) # compute Bar-Natan's bracket
    # BNr = cx.ToBNAlgebra() # convert the Bar-Natan's bracket into a complex over BNAlgebra
    # BNr.eliminateAll() # cancel all identity components of the differential
    # BNr.clean_up() # try to find the immersed curve invariant BNr through a sequence of random isotopies

    # # Jones_poly = BNr.Jones()
    # # print("JONES POLY: " + Jones_poly)

    # # with open("examples/"+filename+"/"+filename+"_jones.txt", "w") as text_file:
    # #     print(Jones_poly, file=text_file)
    # # f = open("Jones.txt", "a")
    # # f.write(Jones_poly)
    # # f.close()

    # #BNr.draw(name)

    # multicurve = BNr.to_multicurve()
    # multicurve.save(name)

    if figured_out_tangle:
        with open("../examples/"+filename+".html", "w") as text_file:
            # print(header+html_content, file=text_file)
            print(html_content, file=text_file)
    if not verbose:
        enablePrint()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        asdf(sys.argv[1])
    if len(sys.argv) == 3:
        asdf(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 4:
        asdf(sys.argv[1], sys.argv[2], sys.argv[3])
    