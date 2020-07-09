import sys
if __name__ == "__main__":
    filename = sys.argv[1]
    new_filename = filename + "_together"
    with open("examples/"+new_filename+".html", "w+") as new_text_file:
        with open("examples/"+filename+".html", "r") as text_file1:
            print(text_file1.read(), file=new_text_file)
        with open("examples/"+filename+"_minimal.html", "r") as text_file2:
            print(text_file2.read(), file=new_text_file)

