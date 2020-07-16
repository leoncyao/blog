import find_minimal_framing
import KhT
import os
if __name__ == "__main__":
	t="cap0.neg1.cap3.neg2.neg2.neg1.cup1"
	for i in range(1,1 + 5):
		new_t = t[:-5] + ".pos0" * i + ".cup1"
		print(new_t)
		filename = "asimov_" + str(i)
		# filename_copy = str(filename)
		filepath = "../examples/asimov/" + filename + ".txt"
		f = open(filepath, "w+")
		# print("WRITING " + new_t)
		f.write(new_t)
		f.close()

		# KhT.asdf(filename, "asimov")

		print("at this point filename is " + filename)
		find_minimal_framing.main(filename, tangle_path="asimov", resultingdirectory=filename)