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



{% assign lol = "1,2,3,4,5,6,7,8,9,10" | split: ',' %}

{% for test in lol %}

<div class="row">
  <a href="{{site.baseurl}}/KhT/examples/asimov/asimov_{{test}}_together.html">Khovanov Invariants</a>
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
