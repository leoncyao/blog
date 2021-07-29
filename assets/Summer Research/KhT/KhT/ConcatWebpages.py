import sys
import os

def write():
    with open("../examples/header.html", "r") as text_file1:
            print(text_file1.read(), file=new_text_file)

def main(filename):
    new_filename = filename + "_together"
    source_path = "../examples/" + filename + "/"
    target_path = "../../../final_project/public/Capped-Trivial-Tangles"
    with open(source_path + new_filename+".html", "w") as new_text_file:



        with open(source_path + filename + ".html", "r") as text_file2:
            print(text_file2.read(), file=new_text_file)

        # tries = [(-1)**(i) * int((i)/2) for i in range(2, 6)]
        # for num_twists in tries:
        #     with open("../examples/html_files/"+filename + "_" + str(num_twists) + "_minimal.html", "r") as text_file_temp:
        #         print(text_file_temp.read(), file=new_text_file)
        #     text_file_temp.close()
        # if os.source_path.is
        with open("../examples/" + filename + "/" + filename+"_minimal.html", "r") as text_file3:
            print(text_file3.read(), file=new_text_file)

        
if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
    # new_filename = filename + "_together"
    # with open("examples/"+new_filename+".html", "w+") as new_text_file:
    #     with open("examples/header.html", "r") as text_file1:
    #         print(text_file1.read(), file=new_text_file)
    #     with open("examples/"+filename+".html", "r") as text_file2:
    #         print(text_file2.read(), file=new_text_file)
    #     with open("examples/"+filename+"_minimal.html", "r") as text_file3:
    #         print(text_file3.read(), file=new_text_file)

