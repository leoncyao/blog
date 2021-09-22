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
    var iframe = document.querySelector('ViewShift');
    console.log(iframe)
    // This code could probably be tidied up, depending on how familiar you are with the game code
    iframe.contentDocument.getElementById("muted").checked = true;
    iframe.contentWindow.speaker[0].muted = true
    iframe.contentWindow.speaker[1].muted = true
});

</script>
<!-- <script src="blob:{{site.baseurl}}public/Builds/index.html"></script> -->