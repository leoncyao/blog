---
layout: default
title: Capped Trivial Tangles
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



{% assign lol = "0_1,3_1,4_1-vertical,4_1-horizontal,5_1,5_2-vertical,5_2-horizontal,6_1-vertical,6_2-horizontal,6_3,7_1,7_2,7_3,7_4,7_5" | split: ',' %}

{% for test in lol %}
{% assign stuff = test | split: "-" %}
{% assign number = stuff | first %}
{% assign type = stuff[1] %}
<a href="http://katlas.org/wiki/{{number}}">${{number}}$</a> 
<!-- {{type}} -->
<div class="row">
{% for item in site.static_files %}
{% if item.path contains test and item.path contains "png" %}
  <div class="column">
    <img src ="{{site.baseurl}}/{{ item.path }}" style="width:100%">
  </div>
{% endif %}
{% endfor %}
</div>
{% endfor %}
