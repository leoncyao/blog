---
layout: post
title: Rational Tangles
date: 2020/05/6
permalink: /:year/:month/:day
---

I want to share a particular kind of tangle which I thought has a cool correspondence with rational numbers. 

This post will be regurgitating the video series given by <a href = "https://www.youtube.com/playlist?list=PLL0ATV5XYF8BfT8CmmzKnfTlf3V9hQgj9">Matthew Salomone</a  >. I highly recommend you check out this series if you have a background in topology or group theory, and you are interested in knot theory. 

A tangle is a diagram of a small part of a knot. One way to construct tangles to draw a circle on the knot diagram such that the knot intersects the circle at exactly 4 places. Here is an example of a knot diagram. 
<img src = "{{site.baseurl}}/assets/img/KnotDiagramExample.jpg">
Here is an example of a tangle. 
<img src = "{{site.baseurl}}/assets/img/TangleExample.jpg">
One particular type of tangle is called a rational tangle. We construct rational tangles in the following way 

<img src = "{{site.baseurl}}/assets/img/RationalTangles.jpg">

Here is an example of a rational tangle (again all of these were drawn by Matthew Solomone). 

<img src = "{{site.baseurl}}/assets/img/RationalTangleExample.jpg">

The main is reason I feel this is a cool construction is because of the way we can represent these tangle diagrams as rational numbers. 

As we construct these tangles with R and T operations, it is clear that each sequence of letters of R, T determines a tangle. For example, the sequence TTTTTRTTRTTT produces the tangle in the previous example, as seen here.

<img src = "{{site.baseurl}}/assets/img/Tangle.gif">

We note that the R and T operations have inverses. You can see geometrically that R^4 = I, meaning that if you rotate by 90 degrees 4 times you end up with the same tangle. We therefore let the inverse of R, R^(-1), be equal to R^3. 
The proof that TRTRTR = I can be seen with this animation. Note that we say tangles are equal when we stretch and bend one tangle to another, without breaking or tearing any of the strands. 

<img src = "{{site.baseurl}}/assets/img/TwistInverse.gif">




