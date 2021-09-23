---
layout: page
title: Leon's Blog(n-1)
time: 2020-05-15
---
<!-- <style>
    .column {
  float: left;
  width: 100.0%;
  padding: 5px;d
}

<!-- /* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
  width: 200%;
} -->
<!-- h1 {text-align: left;}
</style> --> 

<iframe src="https://leoncyao.github.io/blog//public/pages/Recurse" id="test" style="border:0px #000000 none;" name="Game name" scrolling="yes" frameborder="10" marginheight="5px" marginwidth="5px" height="1080px" width="1920px"></iframe>

<!-- Lol how do you do this, want to change the n in Leon's Blog(n) to be n - 1 -->
<script>
$( document ).ready(function() {
    
    // lmao need to wait for inner document to load first, gonna hack it with a delay
    setTimeout(
        ()=>{
            setTimeout(()=>{
                var title = document.getElementById("test").contentDocument.body.querySelector("#blog_title")
                if (title){
                    check = title.text
                    console.log(check)
                    index_1 = check.indexOf("(")
                    index_2 = check.indexOf(")")
                    word = check.slice(index_1,index_2+1)
                    console.log(word)
                    digits = word.length
                    if (digits == 3){
                        check = check.substring(0, index_1+1) + "n-1" + ")"
                    } else {
                        number = check.substring(index_1+1, index_2)
                        check = number
                        // check = check.substring(0, index_1) + "n-" + (digits - 2).toString() + ")")
                    }
                    title.text = check
                }
        }, 1000)
    },1000)
 
    // 
    // var check = document.getElementById("test").contentWindow.document.getElementbyId("blog_title");

});

</script>
