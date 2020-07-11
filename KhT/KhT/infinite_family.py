import KhT
if __name__ == "__main__":
	tangle_str="cap0.neg1.cap3.neg2.neg2.neg1.cup1"
	for i in range(1,3):
		new_tangle_str = tangle_str[:-5] + ".pos0" * i + ".cup1"
		filename = "../examples/asimov/asimov_" + str(i) + ".txt"
		f = open(filename, "w+")
		# print("truncated str is " + new_tangle_str[:-5])
		# print(f)
		f.write(new_tangle_str)
		test = "sh find_minimal_and_make_webpage.sh " + filename
		KhT.asdf("asimov_1", )

if __name__ == "__main__":
    if len(sys.argv) == 2:
        asdf(sys.argv[1])
    if len(sys.argv) == 3:
        asdf(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 4:
        asdf(sys.argv[1], sys.argv[2], sys.argv[3])