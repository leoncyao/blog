---
layout: default
title: viewer
time: 2020-05-15
---
<script src="./jquery-3.4.1.min.js"></script>
<style>
    .column {
  float: left;
  width: 50.0%;
  padding: 5px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
  width: 200%;
}
h1 {text-align: left;}
</style>

<div id='test'></div>

<img id="knot" src="{{site.baseurl}}/assets/img/Capped-Trivial-Tangles/3_1/3_10001.png"/>
<div class="row">
<button id="click_previous_image">prev</button>  
<button id="click_next_image">next</button>
</div>
<script>
$(document).ready(function () {
    // var img = document.createElement('img'); 
    // img.src =  
    // '{{site.baseurl}}/assets/img/Capped-Trivial-Tangles/3_1/3_10001.png'; 
    // document.getElementById('test').appendChild(img); 
});



var i = 1;
function click_next_image () {
    i = ((i + 1) % 10);
    console.log(i)
    document.getElementById("knot").src = `{{site.baseurl}}/assets/img/Capped-Trivial-Tangles/3_1/3_1000${i}.png`
}
function click_previous_image () {
    i = ((i - 1) % 10);
    console.log(i)
    document.getElementById("knot").src = `{{site.baseurl}}/assets/img/Capped-Trivial-Tangles/3_1/3_1000${i}.png`
}



$('#my_image').on({
    'click': function(){
        $('#my_image').attr('src','second.jpg');
    }
});
$('#click_next_image').on('click', click_next_image)
$('#click_previous_image').on('click', click_previous_image)


</script>

