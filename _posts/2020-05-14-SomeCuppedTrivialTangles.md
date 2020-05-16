---
layout: post
title: Some Cupped Trivial Tangles
time: 2020-05-15
---
<style>
    .column {
  float: left;
  width: 33.33%;
  padding: 5px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
}
</style>

<div class="row">
{% for item in site.static_files %}
{% if item.path contains 'Figure-8-vertical/' %}
  <div class="column">
    <img src ="{{site.baseurl}}/{{ item.path }}" style="width:100%">
  </div>
{% endif %}
{% endfor %}
</div>