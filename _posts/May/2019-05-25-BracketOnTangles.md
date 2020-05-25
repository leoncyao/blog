---
layout: post
title: Brackets Polynomial for Tangles
---

<style>
div.a {
  margin-left: 200px;
  width: 5px;
  height: 5px;
  top: -45px;
  transform: rotate(90deg);
  position: relative;
}
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    }
</style>

<!-- 
<a href="http://127.0.0.1:4000/ResearchJournal//2019/05/13/RationalTangles.html#tangle">Tangle</a>  -->

The bracket polynomial of a <a href="https://leoncyao.github.io/ResearchJournal///2019/05/13/RationalTangles.html#tangle">Tangle</a> $T$ counts the ways to smooth a tangle into the infinity tangle $)($ and the zero tangle <font size="+2"> <span>
    &#xFE35;.
    <span style="position:relative; left:-37px; top:0.5px;">&#xFE36;</span>
</span></font>

It is easiest to calculate the bracket polynomial with a <b>resolution tree</b>.

Here are some examples of resolution trees.

Example 1: $T_1$ - Tangle with 1 crossing 
<img src = "{{site.baseurl}}/assets/img/1twist.jpg">

In the left child, we have performed $0$ smoothing on the crossing in the middle of the knot, while on the right child, we have performed an $\infty$ smoothing on the crossing instead.


Example 2: $T_2$ - Tangle with 2 crossings 

<img src = "{{site.baseurl}}/assets/img/2twists.jpg">

Each node in the resolution tree corresponds a state of the tangle where some of the crossings have been smoothed. The left child of each node represents a $0$ smoothing while the right child represents an $\infty$ smoothing. I ordered the crossings arbitrary from left to right, so the first level represents the choices for smoothing the crossing on the left. 

Each leaf node of the "resolution tree" corresponds to a combination of smoothings for each crossing. For each crossing, we can smoothing the crossing in one of two ways

<img src = "{{site.baseurl}}/assets/img/SplittingRule.jpg">

A exercise that is left to the reader is that each leaf node will either look like infinity tangle $)($ or the zero tangle with $0$ or more circles in between number of circles. 

Here the variable for the polynomial is $A$ instead of the usual variable x (perhaps because x looks too much like a crossing). 

For tangle $T$, then we define the bracket polynomial $\langle T \rangle := P_0(A)\langle )( \rangle + P_{\infty}(A)\langle$ <font size="+2"> <span>
    &#xFE35;$\rangle$
    <span style="position:relative; left:-42px; top:0.5px;">&#xFE36;</span>
</span></font>

So for the tangle $T_1$ in Example 1, we have that \\
$\langle T_1 \rangle := A \langle )( \rangle + A^{-1}\langle$ <font size="+2"> <span>
    &#xFE35;$\rangle$
    <span style="position:relative; left:-42px; top:0.5px;">&#xFE36;</span>
</span></font>

Note that for a tangle with $n$ crossings, we have $2^n$ possible smoothings

For any two tangles $G$ and $H$, we can "add" $G$ and $H$ together in the following way: 
<img src="{{site.baseurl}}/assets/img/TangleAddition.jpg">
-credit to <a href="https://youtu.be/o6UnPngxbOo?t=192">Matthew Salmone</a> for the drawing. 

It turns out the formula for the bracket of the sum of tangles is really nice! 




