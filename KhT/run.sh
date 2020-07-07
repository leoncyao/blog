
tangle=$1
python3 KhT ${tangle}
pdf_file_path="examples/${tangle}/PSTricks/${tangle}_BNr7-tangle-pics.pdf"
png_output_file_name="examples/${tangle}/${tangle}-tangle"

# wolframscript -code parse.wls < "examples/trefoil/trefoil_jones_poly.txt"
pdftoppm ${pdf_file_path} ${png_output_file_name} -png
# pdftoppm examples/4_1/PSTricks/4_1_BNr7-tangle-pics.pdf examples/4_1/PSTricks/4_1-tangle -png
