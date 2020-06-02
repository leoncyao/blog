---
layout: default
title: Capped Trivial Tangles
time: 2020-05-15
---
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

{% assign lol = "1-trivial, 1-one-crossing, 4_1, 5_2-vertical, 5_2-horizontal, 6_1-vertical" | split: ', ' %}
{% for test in lol %}
${{test}}$
{% assign xD = "/" %}
<div class="row">
{% for item in site.static_files %}
{% if item.path contains {{test | append: xD }} %}
  <div class="column">
    <img src ="{{site.baseurl}}/{{ item.path }}" style="width:100%">
  </div>
{% endif %}
{% endfor %}
</div>
{% endfor %}
