
name = filename
f = open(name + ".txt", "r")
tangle = f.read()
Tangle = Tangle(tangle)

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
    with open("examples/"+filename+".html", "w") as text_file:
        # print(header+html_content, file=text_file)
        print(html_content, file=text_file)
