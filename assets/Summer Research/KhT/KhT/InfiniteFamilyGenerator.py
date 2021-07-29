import find_minimal_framing
import KhT
import os
import sys
def main(starting_tangle_path, iterating_str, inserting_index, family_name, num_iterations=5):
	f = open("../examples/" + family_name + "/" + starting_tangle_path + ".txt", "r")
	starting_tangle_str = f.read()
	starting_tangle_arr = starting_tangle_str.split('.')

	for i in range(1,1 + num_iterations):
		new_tangle_arr = list(starting_tangle_arr)
		filename = family_name + "_" + str(i)
		filepath = "../examples/" + family_name + "/" + filename + ".txt"
		for j in range(1, i):
			new_tangle_arr[inserting_index:inserting_index] = iterating_str.split('.')
		# new_tangle_str = new_tangle_arr.join('.')
		new_tangle_str = ".".join(new_tangle_arr)
		# print(new_tangle_arr)
		# print(new_tangle_str)
		# print(filepath)
		f = open(filepath, "w+")
		f.write(new_tangle_str)
		f.close()
		KhT.asdf(filename, tangle_path=family_name, resultingdirectory=filename)
		find_minimal_framing.main(filename, tangle_path=family_name, resultingdirectory=filename)

if __name__ == "__main__":
	# main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	# main("rational_experiment_1", "neg0", 5, "rational_experiment")

	# main("3_1-family_1", "pos0", 5, "3_1-family")
 
	# main("4_1-A-family_1", "neg3.neg2.neg2.neg3", 3, "4_1-A-family",num_iterations=5)

	# main("4_1-B-family_1", "neg0", 13, "4_1-B-family",num_iterations=5)

	# main("5_2-A-family_1", "neg3.neg2.neg2.neg3", 3, "5_2-A-family",num_iterations=5)

	# main("even_twist-family_1", "neg3.neg2.neg2.neg3.neg3.neg2.neg2.neg3", 3, "even_twist-family",num_iterations=3)

	# main("odd_twist-family_1", "neg3.neg2.neg2.neg3.neg3.neg2.neg2.neg3", 3, "even_twist-family",num_iterations=3)

	# main("orwell_1", "neg4", 7, "orwell",num_iterations=5)
	
	# main("copernicus_1", "pos0", 12, "copernicus",num_iterations=5)

	# main("5_2-B_1", "pos1", 10, "5_2-B",num_iterations=5)

	# main("6_2-A-family_1", "neg3.neg2.neg2.neg3", 3, "6_2-A-family")

	main("6_3-A-family_1", "pos0.pos1.pos1.pos0", 5, "6_3-A-family")

	# main("galois_1", "pos0", 12, "galois",num_iterations=5)


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
