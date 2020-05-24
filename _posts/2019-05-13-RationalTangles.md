---
layout: post
title: Rational Tangles
time: 2020/5/20
excerpt_separator: <!--more-->
---
<style>
    img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    }
    details {
        margin-left: 5%;
    }
    summary {
        margin-left: -5%;
        position : relat;
    }
</style>

I want to share a particular kind of tangle which I thought has a cool correspondence with rational numbers. 

This post will be regurgitating the video series given by <a href = "https://www.youtube.com/playlist?list=PLL0ATV5XYF8BfT8CmmzKnfTlf3V9hQgj9">Matthew Salomone</a  >. I highly recommend you check out this series if you have a background in topology or group theory, and you are interested in knot theory. 

A tangle is a diagram of a small part of a knot. One way to construct tangles to draw a circle on the knot diagram such that the knot intersects the circle at exactly 4 places. Here is an example of a knot diagram. 
<img src = "{{site.baseurl}}/assets/img/KnotDiagramExample.jpg">
Here is an example of a tangle. 
<img src = "{{site.baseurl}}/assets/img/TangleExample.jpg">

<!--more-->

One particular type of tangle is called a rational tangle. We construct rational tangles in the following way:

<img src = "{{site.baseurl}}/assets/img/RationalTangles.jpg" class="center">

Here is an example of a rational tangle (again all of these were drawn by Matthew Solomone). 

<img src = "{{site.baseurl}}/assets/img/RationalTangleExample.jpg" class="center">

<details>
<summary>Cool fact! $R$ and $T$ operations have inverses</summary> 
We note that the $R$ operation has an inverse. You can see geometrically that $R^2 = I$, meaning that if you rotate by 90 degrees 2 times you end up with the same tangle (this is due to the vertical symmetry we started with at with empty tangle). Therefore the inverse of $R, R^{-1}$, is equal to itself. 

We also note that the $T$ operation has an inverse. The proof that
$TRTRTR = I$ can be seen with this animation below. Note that we say tangles are equal when we stretch and bend one tangle to another, without breaking or tearing any of the strands. 

<img src = "{{site.baseurl}}/assets/img/TwistInverse.gif">

Thus, we let the inverse of $T, T^{-1} = RTRTR$
</details>
<br>
The main is reason I feel this is a cool construction is because of the way we can represent these tangle diagrams as rational numbers. 

As we construct these tangles with $R$ and $T$ operations, it is clear that each sequence of letters of $R, T$ determines a tangle. For example, the sequence $TTTTTRTTRTTT$ produces the tangle in the previous example, as seen here.

<img src = "{{site.baseurl}}/assets/img/Tangle.gif">


Next, we first identify every sequence of $R, T, R^{-1}，T^{-1}$ with a sequence of integers. We will first cancel out the chunks of $R$s and $R^{-1}$s and $T$s, $T^{-1}$s. 

For example:

$$RRRR^{-1}TRTT^{-1}TTTRRR^{-1} = RRTRTTTR = R^2TRT^3R$$

Note we also shorten consecutive strings of the same letter using exponents. 

After shortening, we see that every sequence is of the form $R^{a_0}T^{a_1}R^{a_2}T^{a_3} ... $ for some integers $a_i$. 

We will then adopt the convention that to get from a sequence of  integers to a tangle, we treat each integer as an exponent for the corresponding operation (starting with a twist). 

For example:
$3, -4, -10, 2 \iff  T^3R^{-4}T^{-10}R^2$

Why is this a useful encoding? 

The $R$ and $T$ operations above are specific examples of the more general operations $+$ and $\cdot$. 

Recall that the R and T operations satisfiy TRTRTR = I.
It turns out there are operations rational numbers that this same equation. 

Let $r(x) = -\frac{1}{x}, t(x) = x+1$. 

We see that $r^2(x) = \frac{-1}{\frac{-1}{x}} = x$.

You can show with a bit of algebra that $t(r(t(r(t(r(x)))))) = x$ 
<details>
<summary> Beware of Messy algebra </summary>
$$
\begin{equation*}
    \begin{split}
        t(r(t(r(t(r(x)))))) &= t(r(t(r(t(-\frac{1}{x})))))) \\ 
                            &= t(r(t(r(-\frac{1}{x} + 1))))) \\
                            &= t(r(t(\frac{-1}{(-\frac{1}{x} + 1)}))) \\
                            &= t(r(\frac{-1}{(-\frac{1}{x} + 1)} + 1)) \\
                            &= t(\frac{-1}{\frac{-1}{-\frac{1}{x} + 1} + 1}) \\
                            &= \frac{-1}{\frac{-1}{-\frac{1}{x} + 1} + 1} + 1 \\
                            &= \frac{-1}{\frac{-1}{\frac{x - 1}{x}} + 1} + 1 \\
                            &= \frac{-1}{\frac{-x}{x - 1} + 1} + 1 \\
                            &= \frac{-1}{\frac{-x + (x - 1)}{x - 1}} + 1 \\
                            &= x - 1 + 1 = x \\
    \end{split}    
\end{equation*}
$$
</details>

<br>
Using these operations, we can turn the sequence of integers into a rational number. 

We will take the sequence of integers and alternate between applying the $r$ and $t$ functions on the number built up so far. 

For $3, -4, -10, 2$, this would look like:

$$(((3 \cdot \frac{-1}{4}) + (-10)) \cdot \frac{1}{2} $$

It turns out these operations encapsulate the twist and rotation operations on tangle. If you take two tangles G and H, and convert them to their continued fraction representation, and then

Isn't this cool? This means that if you add or multiply rational tangles together 


Phew, if you made it this far, you are now an expert on rational tangles. Pat yourself on the back!

A few questions you might consider:

Are there tangles that are not rational tangles? By which I mean, tangles that cannot be constructed by starting from the empty tangle and performing the Twist and Rotation operations?

In general proving that such a tangle is difficult. 
<!-- Given an arbitrary tangle, one to way prove it can be constructed from R and T operations is to give a sequence of such operations, and then twist and bend the tangle such that it matches up.  -->
<!-- It is usually easier to prove that it cannot be constructed.  -->
One way to prove a given tangle is not rational is by finding things called "invariants".

An simple example of an invariant can be found in rock-paper-scissors. Let's say we have two players Billbert and Billiam, who play a number of rounds of rock-papers-scissors. Let's also say that a player gets +1 if they win and -1 if lose and 0 if they draw. Then after every round, we notice that the sum of the players scores is always 0 (these are called zero sum games, as the sum is invariant at 0). What this means is that, if ever the scores of two the players added up to something nonzero, then we know the scores of the two players could not come from watching Billbert and Billiam playing a fair game of rock paper scissors (perhaps Billiam is cheating). 

Going back to tangles, we need a property of tangle that does not change when we rotate or twist. If we can calculate such an invariant for empty tangle and for the given tangle, and the invariants are not equal, then it must be that the given tangle is not rational. 

Part of my research this summer will be to calculate such an invariant, called the Khovanov Homology, for certain tangles. Wish me luck!



