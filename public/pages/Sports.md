---
layout: page
title: Sports!
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
<video width="100%" height="500" controls loop autoplay muted>
<source src="{{site.baseurl}}/assets/Sports/backwards_badminton_shot.mp4" type="video/mp4">
asdiofh
<video width="100%" height="500" controls loop autoplay muted>
<source src="{{site.baseurl}}/assets/Sports/1v1_me_bosco.mp4" type="video/mp4">


<div class="row">
{% for item in site.static_files %}
{% if item.path contains "Sports" and item.path contains "mp4" %}
  <div class="column">
      <video width="100%" height="500" controls loop autoplay muted>
      <source src="{{site.baseurl}}/{{item.path}}" type="video/mp4">
  </div>
{% endif %}
{% endfor %}
</div>

