import find_minimal_framing
import KhT
if __name__ == "__main__":
	t="cap0.neg1.cap3.neg2.neg2.neg1.cup1"
	for i in range(1,10):
		new_t = t[:-5] + ".pos0" * i + ".cup1"
		filename = "asimov_" + str(i)
		filepath = "../examples/asimov/" + filename + ".txt"
		f = open(filepath, "w+")
		f.write(new_t)
		f.close()

		KhT.asdf(filename, "asimov")
		find_minimal_framing.main(filename, tangle_path="asimov", resultingdirectory="")