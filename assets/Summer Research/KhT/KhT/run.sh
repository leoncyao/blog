
tangle=$1
tangle_path=$2
python3 KhT.py ${tangle} ${tangle_path}
pdf_file_path="../examples/${tangle_path}/${tangle}/PSTricks/${tangle}_BNr7-tangle-pics.pdf"
png_output_file_name="../examples/${tangle_path}/${tangle}/${tangle}-tangle"

# wolframscript -code parse.wls < "examples/trefoil/trefoil_jones_poly.txt"
pdftoppm ${pdf_file_path} ${png_output_file_name} -png
# pdftoppm examples/4_1/PSTricks/4_1_BNr7-tangle-pics.pdf examples/4_1/PSTricks/4_1-tangle -png
