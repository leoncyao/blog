---
layout: page
title: Sports! (Athletics)
time: 2020-05-15
---

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
{% if item.path contains "Sports" and item.path contains "mp4" %}
  <div class="column" id="{{item.name}}">
      <video width="500" height="100%" controls loop autoplay muted>
      <source src="{{site.baseurl}}/{{item.path}}" type="video/mp4">
      </video>
  </div>
{% endif %}
{% endfor %}
</div>