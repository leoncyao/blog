tangle=$1
tangle_path=$2
# assuming i have the original tangle text file
# python3 KhT.py $1 $2
python3 find-minimal-framing.py $1 $2
# FILE=$2 "$1_minimal.txt"
# if test -f "$FILE"; then
#     python3 KhT "$1_minimal" $1 $2
#     python3 KhT/concat-webpages.py $1 
# fi
