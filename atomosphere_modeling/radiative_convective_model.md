# Radiative Convective Model 
Radiative convective model captures radiation from the sun and vertical convection within the atomsphere. A numerical scheme based on this model is a well-known work by the pioneering climate scientist **Syukuro Manabe**[^sm]

> This is a classic example of **iterative development** of geophysical mathematical model which sound quite familiar from CS classes. The idea is to capture the main idea by the simplest model, then identify disagreement with reality. The anomalies comes from the lack of expressivity of the minimal model hence we iteratively refine the model by adding more structure and details. We hault when we reach a satisfactory modeling accuracy.

## Iteration 1: Earth as a Black Body
The sun emit its energy from nuclear fusion via radiation. The total luminosity is $L_0 = 3.9 \times 10^{26} \mathrm{Js^{-1}}$. At distance $d$ from the sun, the flux density is:
$$
S_0(d)= \frac{L_0}{4\pi d^2}\approx 1370 Wm^{-2}
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
:class: dropdown
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
&= S_0r^2\pi [-\cos2\phi]_0^{\pi/2} \\
&= S_0r^2\pi 
\end{align*}
Next adjust for the *planetary albedo* and we get the desired result. 
:::


:::{note} Earth as a Black Body
Suppose earth is a perfect black body, then we can compute the surface temperature by:
$$
T = \left(\frac{\text{Incoming Radiation Flux Density}}{\sigma}\right)^{1/4}
$$
by the stefan-boltzmann law where $\sigma=5.67\times 10^{-8}Wm^{-2}K^{-4}$ is the Stefan-Boltzmann constant.
:::

With these two tools in place, we can calculate surface temperature easily:
:::{prf:proposition} Black Body Model Surface Temperature
The simplest black body model gives a surface tempearture of:
$$
T = \left(\frac{S_0(1-a)/4}{\sigma}\right)^{1/4} \approx 255 K
$$
:::

:::{prf:proof} Proof of Black Body Model Surface Temperature
:class: dropdown
The earth has surface area $4\pi r^2$ therefore the radiative flux density is:
$$
\frac{S_0(1-a)\pi r^2}{4\pi r^2}=\frac{S_0(1-a)}{4}
$$
The rest is just direct arithmetic.
:::

### Problem With The First Iteration
:::{tip} A Climate Student's Drama
🧐 ： $255K？$ \
🤓 ： That is $-18.15C$ \
🧐 ： hmmmm \
😱 ：  That's WAY too cold! 
:::

## Iteration 2: Single Layer Atomosphere

:::{figure} image/1-layer_blanket.png

:::

If we add a single layer atomosphere, the control equations now become:

$$
\begin{cases}
\sigma T_s^4 &= 2 \sigma T_A^4  \\
\sigma (T_e^4 + T_A^4) &= \sigma T_s^4 
\end{cases}
$$

- $\sigma T_e^4 = \frac{S_0}{4}(1-\alpha)$ where $T_e$ is the "averaged earth temperatrue" in the first iteration
- the first equation describes the **flux at the atomosphere**, the atomosphere is assumed to be transparted to short-wave radiation hence the only in-come radiaiton is the OLR from the surface. The R.H.S is the out-going flux; 
- the second equation describes th **flux at the surface**. 

Solving both we get:

$$
T_A = T_e = 255K \\
T_s = 2^{1/4}T_e=303K
$$


## Iteration 3: Multi-layer Atomosphere With Partial Absorbing 

:::{figure} image/multi_layer_blanket.png
Multi-layered Blanket Model 
:::

We can just straight up add more layers to achieve a better approximation of the "continum". However, numerically speaking, we can think the above as the finite-difference scheme for the system:

:::{prf:proposition}
Let $\tau$ be the *optical depth* with $\tau=0$ being at the top of the atomosphere and increase downward. Let $U(\tau), D(\tau)$ being the upward and downward flux respectively. It follows:
$$
\begin{cases}
\frac{dU}{d\tau} &= U(\tau) - B(\tau) \\
\frac{dD}{d\tau} &= B(\tau) - D(\tau)
\end{cases}
$$
where $B$ is the planck's function. This system of equation is known as *Schwarzschild's equation*.
The numerical solution shows some of the important pattern:
:::

:::{figure} image/pure_radiative_diff.png

:::

However, there are three critical issues:

1. The surface is too warm 
2. The *lapse rate* $\frac{dT}{dp}$ is too high
3. The stratosphere is too cold 
## A Breif Digression About Bouyancy 
:::{figure} image/BV_frequency.png
:::
:::{prf:proposition} Brunt-Väisälä frequency 
The BV frequency $N$ can be computed from:
$$
N = \sqrt{\frac{dB}{dz}} = \sqrt{\frac{g}{C_p}\frac{dS}{dz}}
$$
for ideal gases.

- If $dB/dz <0$ then $N$ is imaginary(parcel will rise, convection) hence no oscillation. This is the *unstable* state.
- If $dB/dz = 0$ then $N=0$, parcel is fixed. This is the  *neutral* state. 
- If $dB/dz >0$, we have postive $N$ hence oscilaation. This is the desired *stable* state.
:::







[^sm]: Syukuro Manabe is one of the first climate scientist who sucessfully modelled the climate system using computer-aided numerical simulation. He is one of the 2021 Nobel Physics Winner due to his work in climate modelling. **A fun fact of this grand master from Professor Gan** : he is one of the climate scientist who was rigorously educated  at University of Tokyo, however, who chose to immigrate to the U.S after WWII. I felt this fact to be vastly interesting and relevant under the current geopolitial context for controversial reasons. Here is a link to a socioeconomic study [Exodus of Meoeorolgists from University of Tokyo](https://journals.ametsoc.org/view/journals/bams/74/7/1520-0477_1993_074_1351_mftuot_2_0_co_2.xml).
