---
layout: default
title: Capped Trivial Tangles
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



{% assign lol = "0_1,3_1,4_1-A,4_1-B,5_1,5_2-A,5_2-B,6_1,6_2-A,6_2-B,6_3,7_1,7_2,7_3,7_4,7_5" | split: ',' %}

{% for test in lol %}
{% assign stuff = test | split: "-" %}
{% assign number = stuff | first %}
{% assign type = stuff[1] %}
<a href="http://katlas.org/wiki/{{number}}">${{number}}{{type}}$</a> 



<div class="row">
<img src ="{{site.baseurl}}/assets/img/Capped-Trivial-Tangles/{{test}}/{{test}}.png" style="width:50%">


  <!-- <a href="{{site.baseurl}}/assets/img/Capped-Trivial-Tangles/{{test}}/{{test}}.html">Khovanov Invariants</a>  -->
  <a href="{{site.baseurl}}/KhT/examples/{{test}}.html">Khovanov Invariants</a>
{% comment %}
  {% include {{test}}.html %}
{% endcomment %}

{% comment %}
<!-- {% for item in site.static_files %}
{% if item.path contains test and item.path contains "png" %}
  <div class="column">
    <img src ="{{site.baseurl}}/{{ item.path }}" style="width:100%">
  </div>
{% endif %}
{% endfor %} -->
{% endcomment %}
</div>




{% for tangle in site.data.invariants %}
    {% if tangle.name == test %}
      Sakuma-polynomial : {{tangle.Sakuma-polynomial}}
    {% endif %} 
{% endfor %}    
{% endfor %}
