---
layout: page
title: Projects
time: 2020-05-15
---
<script src="./jquery-3.4.1.min.js"></script>
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

<h1><a href="https://neonleon123.itch.io/viewshift">ViewShift</a></h1>
<p>3D perspective puzzle game for the Video Game Design course I took. </p>
<p>Note you can mute the audio from the options menu.</p>

<iframe src="{{site.baseurl}}public/Builds/index.html" id="ViewShift" title="ViewShift" width="1920px" height="1080px" volume="0"></iframe>
<script>
$( document ).ready(function() {
    // Couldn't mute ViewShift element by itself
    // var iframe = document.querySelector('ViewShift');
    // console.log(iframe)
    // // This code could probably be tidied up, depending on how familiar you are with the game code
    // iframe.contentDocument.getElementById("muted").checked = true;
    // iframe.contentWindow.speaker[0].muted = true
    // iframe.contentWindow.speaker[1].muted = true

    // this doesnt work either, maybe cause the embeded game is inside an iframe ...
    // Mute a singular HTML5 element
    function muteMe(elem) {
        elem.muted = true;
        elem.pause();
    }

    // Try to mute all video and audio elements on the page
    function mutePage() {
        var elems = document.querySelectorAll("iframe");
        alert(elems)
        [].forEach.call(elems, function(elem) { muteMe(elem); });
    }
    mutePage()
});

</script>

