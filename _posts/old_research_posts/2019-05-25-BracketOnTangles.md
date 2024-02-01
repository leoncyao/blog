---
layout: post
title: Brackets Polynomial for Tangles
excerpt_separator: <!--more-->
---

<style>

img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    }

a {
  color: #900;
  text-decoration: none;
}

a:hover {
  color: red;
  position: relative;
}

a[data]:hover:after {
  content: attr(data);
  padding: 4px 8px;
  color: rgba(0,0,0,0.5);
  position: absolute;
  left: 0;
  top: 100%;
  white-space: nowrap;
  z-index: 2;
  border-radius: 5px ;
  background: rgba(0,0,0,0.5);
}

b {
    display: none;
    height:30px;
    top: -50px;
    width:290px;
    text-align: center;
    position:relative;
}

a:hover + b {
    display: block;
}​



</style>

<!-- 
<a href="http://127.0.0.1:4000/ResearchJournal//2019/05/13/RationalTangles.html#tangle">Tangle</a>  -->

The bracket polynomial of a <a href="{{site.baseurl}}/2019/05/13/RationalTangles.html#tangle">Tangle</a> $T$ counts the ways to smooth a tangle into the infinity tangle $)($ and the zero tangle <font size="+2"> <span>
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
<!--more-->

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

Let two knots $G, H$ have bracket polynomials given by the coefficients $(P_0, P_\infty), (Q_0, Q_{\infty})$. \\
\\
Then the bracket polynomial of $G + H$ is given by  
$(P_0 \cdot Q_0, P_\infty \cdot Q_0 + P_0 \cdot Q_\infty + \delta \cdot P_\infty \cdot Q_\infty)$.

What is the algebraic mess saying? As an example, let $G$ be the 1 twist tangle and $H$ be the 2 twist tangle. Then $G+H$ looks like:

<img src="{{site.baseurl}}/assets/img/1twistPlus2twists.jpg">

Let's draw the resolution tree for $G+H$

<img src="{{site.baseurl}}/assets/img/3twists.jpg">

(I added circles at the bottom just to highlight the leaf nodes)

Looks complicated right. Well let's see what happens if zoom in on the 3 nodes in the bottom left hand corner. 

<img src="{{site.baseurl}}/assets/img/3twistsZoomedIn.jpg">



​If you squint your eyes, you can imagine that the 3 nodes are really just a copy of the 1twist resolution tree. 

One might then realize that you can draw the  resolution for $G + H$ in the following way: 
1. Draw the resolution tree for $G$ 
2. For each state in the tree, add the $H$ tangle 
3. The leaf nodes now have new crossings because of the $H$ tangle, so resolve those crossings to complete the tree

With this construction, the formula for the bracket becomes clearer. 

In order to smooth $G + H$ into the zero tangle, you have to smooth both $G$ and $H$ into the zero tangles. Recall that $P_0$ is the sum of the ways to smooth $G$ into the $0$ tangle, and $Q_0$ is the sum of the ways to smooth $H$ into the $0$ tangle, so each term in the product $P_0 \cdot Q_0$ will correspond to a combination of smoothings that smooth $G+H$ into the $0$ tangle. 

One useful application of tangles is that we can "close" them up to form knots, and the invariants of knots become easy to calculate using the invariants of the tangle. 

<!-- <img src="{{site.baseurl}}/assets/img/3twistsZoomedIn.jpg" title="A mathematician might say that the 2 trees are isomorphic, meaning that each node of the tree on left the gets mapped to a corresponding node of the tree on the right, such that the structure of the tree is preserved. See more into graph theory if you like trees!"> -->