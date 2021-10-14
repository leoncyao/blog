---
layout: page
title: Research
time: 2020-05-15
---
<script src="./jquery-3.4.1.min.js"></script>
<!-- <style>
    .column {
  float: left;
  width: 100.0%;
  padding: 5px;d
}

<!-- /* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
  width: 200%;
} -->
<!-- h1 {text-align: left;}
</style> --> 

<div id="chebyshev_optimization">
<h2><a href="https://github.com/leoncyao/chebyshev_optimization">Integer Chebyshev Problem</a></h2>

Let the supremum norm of a polynomial over the domain $I$ be given by 

$$||p(x)||_I = \sup_{x \in I}{|p(x)|}$$

We want to find the polynomial the minimizes this norm. 
<br>
Formally, this means we want to solve the problem

$$
t_{\mathbb{Z}, n} = \min_{p \in \mathbb{Z}, p \neq 0\}}||p(x)||_I^{1/n}
$$

where the optimal value for a given $n$ is denoted $t_{\mathbb{Z}, n}(I)$. <br>
We can then take the limit as $n \rightarrow \infty$ and we will call this limit the <b>Integer Chebyshev Constant</b> denoted,

$$t_{\mathbb{Z}(I)} = \lim_{n \rightarrow \infty}{t_{\mathbb{Z}, n}(I)}$$

Inside this <a href="https://github.com/leoncyao/chebyshev_optimization">repo</a>, you can find a python script called <b>chebyshev.py</b> which uses the gurobi library to solve this problem. <br><br>
Specifically, you can run <br><br>

<b>python chebyshev.py</b> <br><br>

to calculate the optimum value for $n = 2$ <br><br>

TODO: 
<ul>
<li>Add cases n > 2 </li>
<li>Add option to increase n until value converges within given range</li>
</ul>


<h3>References:</h3>
<ul>
<li>Hare, K. G. , & Hodges, P. W. . (Accepted). <a href="https://uwaterloo.ca/scholar/kghare/publications/applications-integer-and-semi-infinite-programming-integer-chebyshev-problem">Applications of Integer and Semi-Infinite Programming to the Integer Chebyshev Problem</a>. Experimental Mathematics. Retrieved from https://doi.org/10.1080/10586458.2019.1691089
</li>

</ul>




</div>