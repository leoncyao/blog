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

We note that the R operation has an inverse. You can see geometrically that R^2 = I, meaning that if you rotate by 90 degrees 2 times you end up with the same tangle (this is due to the symmetry we started with at with empty tangle). Therefore the inverse of R, R^(-1), is equal to itself. 

We also note that the T operation has an inverse. The proof that
TRTRTR = I 
can be seen with this animation below. Note that we say tangles are equal when we stretch and bend one tangle to another, without breaking or tearing any of the strands. 

<img src = "{{site.baseurl}}/assets/img/TwistInverse.gif">

Thus, we let the inverse of T, T^(-1) = RTRTR

Next, we first identify every sequence of R, T, R^(-1)，T^(-1) with a sequence of integers. We will first cancel out the chunks of Rs and R^(-1)s and Ts, T^(-1)s. 

For example:
RRRR^(-1)TRTT^(-1)TTTRRR^(-1) = RRTRTTTR = R^2TRT^3R 

Note we also shorten consecutive strings of the same letter using exponents. 

After shortening, we see that every sequence is of the form R^(a_0)T^(a_1)R^(a_2)T^(a_3) ... for some integers a_i. 

We will then adopt the convention that to get from a sequence of  integers to a tangle, we treat each integer as an exponent for the corresponding operation (starting with a twist). 

For example:
3 -4 -10 2 -> T^3R^-4T^(-10)R^2

Why is this a useful encoding? 
Recall that the R and T operations satisfiy TRTRTR = I.
It turns out there are operations rational numbers that this same equation. Let r(x) = -1/x, t(x) = x+1. 
We see that r^2(x) = -1/(-1/x) = x.
We can also see that 
t(r(t(r(t(r(x)))))) = 


Phew, if you made it this far, you are now an expert on rational tangles. Pat yourself on the back!

A few questions you might consider:

Are there tangles that are not rational tangles? By which I mean, tangles you cannot be constructed from the Twist and Rotation operations?

In general proving that such a tangle is difficult. 
<!-- Given an arbitrary tangle, one to way prove it can be constructed from R and T operations is to give a sequence of such operations, and then twist and bend the tangle such that it matches up.  -->
<!-- It is usually easier to prove that it cannot be constructed.  -->
One way to prove a given tangle is not rational is by finding things called "invariants".

An easy example of an invariant can be found in rock paper scissors. Let's say we have two players alice and bob, who play a number of rounds of rock papers scissors. Let's also say that a player gets +1 if they win and -1 if lose and 0 if they draw. Then after every round, we notice that the sum of the players scores is always 0 (these are called zero sum games). What this means is that, if ever the scores of two the players added up to something nonzero, then we know the scores of the two players could not come from watching alice and bob playing a fair game of rock paper scissors (perhaps alice is cheating). 

Going back to tangles, we need a property of tangle that does not change when we rotate or twist. If we can calculate such an invariant for empty tangle and for the given tangle, and the invariants are not equal, then it must be that the given tangle is not rational. 



