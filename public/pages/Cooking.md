---
layout: page
title: Cooking
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


{% for item in site.static_files %}
{% if item.path contains "Cooking"%}
  <div class="column">
    {{item.name}}
    <img src ="{{site.baseurl}}/{{ item.path }}" style="width:100%">
  </div>
{% endif %}
{% endfor %}


