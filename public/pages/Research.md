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
t_{\mathbb{Z}(n), n} = \min_{p \in \mathbb{Z}(n), p \neq 0\}}||p(x)||_I^{1/n}
$$

where the optimal value for a given $n$ is denoted $t_{\mathbb{Z}(n), n}(I)$. <br>
We can then take the limit as $n \rightarrow \infty$ and we will call this limit the <b>Integer Chebyshev Constant</b> denoted,

$$t_{\mathbb{Z}(n)(I)} = \lim_{n \rightarrow \infty}{t_{\mathbb{Z}(n), n}(I)}$$

Inside this <a href="https://github.com/leoncyao/chebyshev_optimization">repo</a>, you can find a python script called <b>chebyshev.py</b> which uses the gurobi library to solve this problem. <br><br>
Specifically, you can run <br><br>

<b>python chebyshev.py</b> <br><br>

to calculate the optimum value for $n = 2$ <br><br>

The script doesn't actually calcluate the above equation, as taking the min of function which itself is a max of a polynomial is quite tricky to optimize. Instead, becomes of how nice polynomials are, we can directly calculate the minimum and maximum values of the polynomial. <br><br>
For the case of $n=2$, we know that the maximum and minimum values of the quadratic $p(x) = ax^2 + bx + c$ must either be at the endpoints $p(0), p(1)$, or at the center, which has $x = -\frac{b}{2a}$. Note that center point can be calculated with calculus, i.e take the derivative $p'(x) = 2ax - b$ and set it to $0$. <br><br>
It then follows that 
$$||p(x)||_I = \sup_{x \in I}{|p(x)|} = \max{\{p(0), p(1), p(-\frac{b}{2a}})\}$$ 
(assuming the center point is within the domain, otherwise we only consider the endpoints) <br>
Next, I found that it was difficult to minimize 3 values at once in gurobi, so instead I minimized the squared sum of them. 
$$
\min_{p \in \mathbb{Z}(n), p \neq 0}p(0)^2 + p(1)^2 + p(-\frac{b}{2a})^2
$$
The gurobi library can only minimize quadratic functions, which is unfortunate as the $p(-\frac{b}{2a})^2 = \frac{1}{16}b^4$ contains a $b^4$ term. Fortunately, we can convert this problem into an equivalent one that uses more variables and has lower powers. Specifically, the above problem is equivalent to
$$
\begin{align}
\min_{p \in \mathbb{Z}(n), p \neq 0}&(a + b + c)^2  + c^2 + \frac{b^4}{16a^2} - \frac{b^2c}{a} + c^2\\
a^2 &= a \cdot a \\
b^2 &= b \cdot b \\
c^2 &= c \cdot c \\
a^4 &= a^2 \cdot a^2 \\
b^4 &= b^2\cdot b^2 \\
\end{align}
$$
where the terms on the left are their own variable. <br><br>
We also need the constraints 
$$
\begin{align}
1 &= a \cdot a^{-1} \\ 
1 &= c \cdot c^{-1} \\
\end{align}
$$
and variables $a^{-1}, c^{-1}$ for the denominators.
<h4>TODO:</h4> 
<ul>
<li>Add cases $n > 2$ </li>
<li>Add option to increase $n$ until value converges within given range</li>
</ul>

<h3>References:</h3>
<ul>
<li>Hare, K. G. , & Hodges, P. W. . (Accepted). <a href="https://uwaterloo.ca/scholar/kghare/publications/applications-integer-and-semi-infinite-programming-integer-chebyshev-problem">Applications of Integer and Semi-Infinite Programming to the Integer Chebyshev Problem</a>. Experimental Mathematics. Retrieved from https://doi.org/10.1080/10586458.2019.1691089
</li>

</ul>




</div>