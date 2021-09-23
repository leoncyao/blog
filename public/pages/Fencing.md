---
layout: page
title: Fencing!
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
{% if item.path contains "Fencing" and item.path contains "mp4" %}
  <div class="column">
      <video width="100%" height="500" controls loop autoplay muted>
      <source src="{{site.baseurl}}/{{item.path}}" type="video/mp4">
  </div>

{% endif %}
{% endfor %}
</div>

