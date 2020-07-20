import find_minimal_framing
import KhT
import os
import sys
def main(starting_tangle_path, iterating_str, inserting_index, family_name, num_iterations=5):
	f = open("../examples/" + family_name + "/" + starting_tangle_path + ".txt", "r")
	starting_tangle_str = f.read()
	starting_tangle_arr = starting_tangle_str.split('.')


	for i in range(0,0 + num_iterations):
		new_tangle_arr = list(starting_tangle_arr)
		new_tangle_arr[inserting_index:inserting_index] = iterating_str.split('.')
		# new_tangle_str = new_tangle_arr.join('.')
		new_tangle_str = ".".join(new_tangle_arr)
		print(new_tangle_str)
		filename = family_name + "_" + str(i)
		filepath = "../examples/" + family_name + "/" + filename + ".txt"
		print(filepath)
		f = open(filepath, "w+")
		f.write(new_tangle_str)
		f.close()
		find_minimal_framing.main(filename, tangle_path=family_name, resultingdirectory=filename)

if __name__ == "__main__":
	# main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	# main("asimov_1", "pos0", 5, "asimov")
	main("cixin_liu_0", "pos3.pos2.pos2.pos3", 3, "cixin_liu")
	# figure 8 family
	# f = open("../examples/cixin_liu/cixin_liu.txt", "w")
	# starting_tangle_str = f.read()
	# main(starting_tangle_str)


	# t="cap0.neg1.cap3.neg2.neg2.neg1.cup1"
	# for i in range(1,1 + 5):
	# 	new_t = t[:-5] + ".pos0" * i + ".cup1"
	# 	print(new_t)
	# 	filename = "asimov_" + str(i)
	# 	filepath = "../examples/asimov/" + filename + ".txt"
	# 	f = open(filepath, "w+")
	# 	f.write(new_t)
	# 	f.close()
	# 	find_minimal_framing.main(filename, tangle_path="asimov", resultingdirectory=filename)