import sys
if __name__ == "__main__":
    filename = sys.argv[1]
    new_filename = filename + "_together"
    header="""
    <link rel="stylesheet" href="css/main.css">
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <script>
    function on(file,pagenumber) {
        document.getElementById("overlay_content").src=String(file)+".pdf";
        document.getElementById("overlay_title").innerHTML=String(file);
        document.getElementById("overlay").style.display = "block";
    }

    function off() {
        document.getElementById("overlay").style.display = "none";
    } 
    </script>

    <div id="overlay" onclick="off()" >
    <div id="text">
    <div id="overlay_title_frame"><h4 id="overlay_title"></h4></div>
    <iframe id="overlay_content" width="500px" height="500px">
    </iframe></div>
    </div> 
    """
    with open("examples/"+new_filename+".html", "w+") as new_text_file:
        print(header, file=new_text_file)
        with open("examples/"+filename+".html", "r") as text_file1:
            print(text_file1.read(), file=new_text_file)
        with open("examples/"+filename+"_minimal.html", "r") as text_file2:
            print(text_file2.read(), file=new_text_file)

