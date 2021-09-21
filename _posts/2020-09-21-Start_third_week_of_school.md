---
layout: post
title: End of Second week of classes
time: 2021/09/21
---

Have some new ideas for projects, god knows if I ever finish any of them xD.

Pdes heat game (ice age end of the world apocalypse where you assign heat sources in an apartment to keep people alive)

text based job assignment fantasy game

I'm also looking at one of my supervisor's papers. Yo, base golden ratio $$\phi$$ number systems are cool. 

In base $$\phi$$, where $$\phi$$ is the larger root of $$\phi^2 - \phi - 1 = 0$$ i.e $$\phi \approx 1.618$$ numbers are written $$\sum_{i=0}^{\infty}{a_n\phi^{-n}}$$, so the normal decimal system except we have $$\phi$$ instead of $10$. 

In base $$\phi$$, , you can write the number $$1$$ as 
$$1.0, 0.11, 0.1011$$. 

Some trickier expansion are $0.110110110110 ... $ and $0.10101011010$. These can be shown by starting with some algebra
<details> <summary> Messy Algebra showing the above </summary>
$$
\begin{align}
\phi^2 - \phi - 1 &= 0 \text{ start with quadratic equation} \\
1 - \frac{1}{\phi} - \frac{1}{\phi^2} &= 0 \text{ divide both sides by } \phi \\
1 &= \frac{1}{\phi} + \frac{1}{\phi^2} \text{ rearrange } \\
  &= \frac{1}{\phi} + \frac{\frac{1}{\phi} + \frac{1}{\phi^2}}{\phi^2} \text{ sub in previous line for the 1 in the numerator of }\frac{1}{\phi^4} \\
  &= \frac{1}{\phi} + \frac{1}{\phi^3} + \frac{1}{\phi^4} \text{ simplify } \\
  &= \frac{1}{\phi} + \frac{1}{\phi^3} + \frac{\frac{1}{\phi} + \frac{1}{\phi^2} }{\phi^4} \text{ repeat substitution process always on the greatest power term}
 \\
  &= \frac{1}{\phi} + \frac{1}{\phi^3} + \frac{1}{\phi^5} + \frac{1}{\phi^6} \\
  & \vdots 
\end{align} 
$$
which then becomes $$0.10101010...$$ in base $\phi$.
Other expansions such as $$0.110110110...$$ can be shown with a similar method, though you would replace the $1$ with $\frac{1}{\phi^2} - \frac{1}{\phi}$ in a different term (not always the great power one).  
</details>

