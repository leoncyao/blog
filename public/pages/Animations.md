---
layout: page
title: Animations
time: 2020-05-15
---
<script src="./jquery-3.4.1.min.js"></script>
<style>
.column {
  float: left;
  width: 100%;
  padding: 5px;
}

.row::after {
  content: "";
  clear: both;
  display: table;
  width: 200%;
}
</style>

<div class="row">
{% for item in site.static_files %}
{% if item.path contains "Animations" %}
  {% if item.path contains "mp4" %}
      <video width="320" height="240" controls loop>
      <source src="{{site.baseurl}}/{{item.path}}" type="video/mp4">
    </video>
  {% elsif item.path contains "gif" %}
  <div class="column">
    <img src ="{{site.baseurl}}/{{ item.path }}" style="width:100%">
  </div>
  {% endif %}  
{% endif %}
{% endfor %}
</div>

