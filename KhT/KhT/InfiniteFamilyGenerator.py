import find_minimal_framing
import KhT
import os

def main(starting_tangle_str, iterating_str, inserting_position, family_name, num_iterations=5):
	starting_tangle_arr = starting_tangle_str.split('.')
	for i in range(1,1 + num_iterations):
		new_tangle_arr = list(starting_tangle_arr)
		new_tangle_arr[1:1] = iterating_str.split('.')
		# new_tangle_arr.insert()
		# new_tangle_str = t[:-5] + ".pos0" * i + ".cup1"
		new_tangle_str = new_tangle_arr.join('.')
		print(new_tangle_str)
		filename = family_name + "_" + str(i)
		filepath = "../examples/" + family_name" + /" + filename + ".txt"
		f = open(filepath, "w+")
		f.write(new_t)
		f.close()
		find_minimal_framing.main(filename, tangle_path=family_name, resultingdirectory=filename)

if __name__ == "__main__":
	# main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

	# figure 8 family
	f = open("../examples/cixin_liu/cixin_liu.txt", "w")
	starting_tangle_str = f.read()
	main(starting_tangle_str)


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