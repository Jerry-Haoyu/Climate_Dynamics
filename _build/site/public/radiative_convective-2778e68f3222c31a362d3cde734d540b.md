# Radiative Convective Model 
Radiative convective model captures radiation from the sun and vertical convection within the atomsphere. This is a well-known work by the pioneering climate scientist **Syukuro Manabe**[^sm], 

> This is a classic example of **iterative development** of geophysical mathematical model which sound quite familiar from CS classes. The idea is to capture the main idea by the simplest model, then identify disagreement with reality. The anomalies comes from the lack of expressivity of the minimal model hence we iteratively refine the model by adding more structure and details. We hault when we reach a satisfactory modeling accuracy.

## Iteration 1: Earth as a Black Body
The sun emit its energy from nuclear fusion via radiation. The total luminosity is $L_0 = 3.9 \times 10^{26} \mathrm{Js^{-1}}$. At distance $d$ from the sun, the flux density is:
$$
S_0(d)= \frac{L_0}{4\pi d^2}
$$
Now we are interested in how the earth absorb radiative energy. 
:::{prf:observation}
Suppose radiation flux density is $S_0$, then earth will get a total absorbed radiation of 
$$
S_0(1-a)\pi r^2 
$$
where $r$ is the radius of earth.
:::

:::{prf:proof} Proof Of The Above Observation
This is just by simple computation:

Only half of the planet is illuminated hence:
$$
\mathrm{Absorbed\; Radiative \;Energy} = \iint_D S_0|\cos(\phi)|\sin(\phi)r^2 d\phi d\theta 
$$
where $D=\{\theta, \phi : \pi/2\leq \phi\leq \pi/2, 0 \leq \theta \leq \pi\}$. $\phi$ is the latitude with $0$ being north pole and $\pi$ be south pole. $\theta$ is longitude ranging from $0$ to $2\pi$. Note $S_0|\cos(\phi)|$ has adjusted radiation for projection. 

Note: $r^2 \sin\phi d\phi d\theta $ is the surface element, since a surface element has 
$$dS = (r\sin\phi)d\theta \cdot rd\phi$$

Evaluating the integral:
\begin{align*}
\iint_D S_0|\cos(\phi)|\sin(\phi)r^2 d\phi d\theta  &= S_0r^2\pi \int_{0}^{\pi} \sin\phi |\cos\phi |d\phi \\
&= S_0r^2\pi 2 \int_{0}^{\pi/2} \sin\phi \cos\phi d\phi \\
&= S_0r^2\pi \int_{0}^{\pi/2} \sin(2\phi) d\phi \\
&= S_0r^2\pi [-\cos2\phi/2]_0^{\pi/2} \\
&= S_0r^2\pi 
\end{align*}
Next adjust for the *planetary albedo 
:::


:::{note} Earth as a Black Body
Suppose earth is a perfect black body, then we 
:::


[^sm]: Syukuro Manabe is one of the first climate scientist who sucessfully modelled the climate system using computer-aided numerical simulation. He is one of the 2021 Nobel Physics Winner due to his work in climate modelling. **A fun fact of this grand master from Professor Gan** : he is one of the climate scientist who was rigorously educated  at University of Tokyo, however, who chose to immigrate to the U.S after WWII. I felt this fact to be vastly interesting and relevant under the current geopolitial context for controversial reasons. Here is a link to a socioeconomic study [Exodus of Meoeorolgists from University of Tokyo](https://journals.ametsoc.org/view/journals/bams/74/7/1520-0477_1993_074_1351_mftuot_2_0_co_2.xml).