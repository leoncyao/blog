---
layout: page
title: Animations
time: 2020-05-15
---
<script src="./jquery-3.4.1.min.js"></script>
<style>
.page{
    width:130%
}


.column {
  float: left;
  width: 50%;
  padding: 20px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>

{% comment %}
YOU CANT PLAY AVI MOVIES FROM SITE, can only download
{% endcomment %}


<div class="row">
{% for item in site.static_files %}
{% if item.path contains "Animations" %}
  <div class="column" id="{{item.name}}">
  {% if item.path contains "mp4"%}
      <video width="100%" height="500" controls loop autoplay muted>
      <source src="{{site.baseurl}}/{{item.path}}" type="video/mp4">
    </video>
  {% elsif item.path contains "gif" %}
    <img src ="{{site.baseurl}}/{{ item.path }}" style="width:100%">
  {% endif %}  
  </div>
{% endif %}
{% endfor %}
</div>

