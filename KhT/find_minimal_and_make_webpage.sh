tangle=$1
python3 KhT/find-minimal-framing.py $1

FILE="$1_minimal.txt"
if test -f "$FILE"; then
    python3 KhT "$1_minimal" "$1" 
    python3 KhT/concat-webpages.py $1
fi

# pdf_file_path="examples/${tangle}/PSTricks/${tangle}_BNr7-tangle-pics.pdf"
# png_output_file_name="examples/${tangle}/${tangle}-tangle"
# pdftoppm ${pdf_file_path} ${png_output_file_name} -png