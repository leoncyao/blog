---
layout: page
title: Recursion
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

<div id="iframe_holder"></div>
<!-- <iframe src="{{site.baseurl}}//public/pages/Recurse" id="test" style="border:0px #000000 none;" name="Game name" scrolling="yes" frameborder="10" marginheight="5px" marginwidth="5px" height="1080px" width="1920px"></iframe> -->

<style>
    
.blog_title
{
    opacity: 0;
    transition: all 600ms ease-out;
}

    </style>


<script>
$( document ).ready(function() {
    var iframe = document.createElement('iframe');
    iframe.width = "1920px"
    iframe.id="test"
    iframe.height = "1080px"
    iframe.src = "{{site.baseurl}}//public/pages/Recurse"
    var place = document.getElementById("iframe_holder")
    console.log(place) 
    place.appendChild(iframe);
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
            if (window.location === window.parent.location){
                check = check.substring(0, index_1+1) + "n-1" + ")"
                title.text = check
            } else {
                number = check.substring(index_1+1, index_2)
                check = check.substring(0, index_1+1) + "n-2" + ")"
                // check = check.substring(0, index_1) + "n-" + (digits - 2).toString() + ")"
                title.text = check
            }
            
        }
}, 1000)
 
    // 
    // var check = document.getElementById("test").contentWindow.document.getElementbyId("blog_title");

});

</script>
