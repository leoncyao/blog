---
layout: page
title: Piano
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


{% for item in site.static_files %}
{% if item.path contains "Piano" and item.path contains "mp4" %}
  <div class="column">
      <video width="320" height="240" controls>
      <source src="{{site.baseurl}}/{{item.path}}" type="video/mp4">
    </video>
  </div>
{% endif %}
{% endfor %}


