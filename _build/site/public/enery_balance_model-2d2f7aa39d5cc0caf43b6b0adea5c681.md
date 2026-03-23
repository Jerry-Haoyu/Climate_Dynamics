---
kernelspec:
  name: python3
  display_name: 'Python 3'
---


# Energy Balance Model 
:::
Edit Log:
Last update : 2026/3/20
:::

## 1D Heat Equation Model
The basic idea behind the **energy balance model** is to take account of transport between different latitude. A model that totally disregard such transport would result in unrealistic temperature distribution due to differential heating. For example,region with latitude not in $[-30,30]$ would be at $0K$ since they have *radiation energy deficit*. 


```{figure}image/differential_heating.png 
:width: 300px
:align: center
Radiation Energy Budget
```



We can discretize the earth to bands at different latitude as [below](#latdis):
:::{tip}
Run the cell below to get an interactive plot explaining the discretization where you can change the resolution and perspective!

*Note* Normally it should take about 45s for the kernel to build, if it takes <5s then it means the build is not 
succesful, refresh the page and click the start button again.

*Note*  After running the cell, scroll down a little bit to see the interactive plot. It is bit laggy but works! You can drag it around as well as play with the slider.

:::
```{code-cell} Latitude Discretization
:tag: [hide-input, remove-stdout,remove-stderr]
:label: latdis

import contextlib
import os

#to redirect stdout when using the line magic command to install and invoke the interactive backend ipympl 
with open(os.devnull, 'w') as devnull:
    with contextlib.redirect_stdout(devnull):
        %pip install ipympl
        %matplotlib ipympl

import matplotlib.pyplot as plt
import ipywidgets as wdgt
import numpy as np

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
# Set an equal aspect ratio
ax.set_aspect('equal')
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
ax.set_title("Latitude Discretization")


theta = np.linspace(0, 2 * np.pi, 100)  #longitude 
phi = np.linspace(0, np.pi, 100) #latitude

x = np.outer(np.cos(theta), np.sin(phi)) #x at (theta,phi) is given by sin(phi)cos(theta)
y = np.outer(np.sin(theta), np.sin(phi)) #y at (theta, phi) is given by sin(phi)sin(theta)
z = np.outer(np.ones(np.size(theta)), 296*np.cos(phi)/297) #z at (theta, phi) is given by cos(phi) with a flattening 

# Plot the surface
ax.plot_surface(x, y, z, zorder=1);

#the resolution of the discretization
Discretization_Resolution = wdgt.IntSlider(value=5, min=5, max=30, step=1)

lines = []

def plot_discretization(Discretization_Resolution):
    global lines
    global fig, ax
    if len(lines) > 0:
        for line in lines:
            line.remove()
    lines = []
    for phi_ in np.linspace(0, np.pi, Discretization_Resolution):
        x = np.cos(theta) * np.sin(phi_) 
        y = np.sin(theta) * np.sin(phi_)
        z = 296*np.cos(phi_)/297
        new_line = (ax.plot(x, y, z, color='black', linewidth=1, linestyle='--', zorder=10))[0]; #plot returns a list
        lines.append(new_line)
    plt.show();

wdgt.interactive(plot_discretization, Discretization_Resolution=Discretization_Resolution)
```

:::{prf:proposition}
$$
\begin{equation}
    C(\phi) \frac{\partial T_s}{\partial t} = ASR(\phi)-OLR(\phi) + \frac{D}{\cos \phi}\frac{\partial }{\partial \phi}\left(\cos \phi \frac{\partial T_s}{\partial \phi}\right)
\end{equation}
$$
:::
where 
- $C(\phi)$ is constant pressure heat capacity at some latittude $\phi$

which is a standard 1D heat equation where $T$ is a function of latitude $\phi$ and temperatre $T$.




## Solving The Heat Equation

### Explicit Radiative Forcing
:::{prf:proposition} ASR as a function of $\phi$
The flux density at a specific latitude $\phi_0$ is:
$$
\text{ASR}(\phi_0) = \frac{S_0|\cos(\phi_0)|}{2}(1-\alpha)
$$
:::
:::{prf:proof} Proof of Explict Form Of ASR
We first need to write $ASR$ and $OLR$ explicitly as a function of $(T, \phi)$.For absorbed incoming short wave radiation, recall the flux density is $S_0$. Now consider a thin strip parallel to the equator that correspond to a $(\phi_0, \phi_0+\delta \phi)$. The **flux density** to the strip is:
\begin{align*}
\text{Flux Density} &= \lim_{\delta \phi \to 0} \frac{\text{Total Flux}}{\text{Total Area}} \\

&= \lim_{\delta \phi \to 0} \frac{\int_{0}^{\pi} d\theta \int_{\phi_0}^{\phi_0+\delta \phi} d\phi r^2\sin(\phi)S_0|\cos\phi|}{\int_{0}^{2\pi} d\theta \int_{\phi_0}^{\phi_0+\delta \phi} d\phi  r^2 \sin(\phi)} \\

&=\lim_{\delta \phi \to 0} \frac{\pi \int_{\phi_0}^{\phi_0+\delta \phi} d\phi r^2\sin(\phi)S_0|\cos\phi|}{2\pi \int_{\phi_0}^{\phi_0+\delta \phi} d\phi  r^2 \sin(\phi)}
\end{align*}
A standard result from mathematical analysis:
$$
\lim_{\delta a\to 0}\frac{\int_a^{a+\delta a}f}{\int_a^{a+\delta a}g} = \frac{f}{g}, \forall g\neq 0
$$
which gets us:
\begin{align*}
&= \frac{1}{2}S_0 |\cos\phi |
\end{align*}
Adjust for planet albedo and we get as desired. 
:::

:::{note} **Assumption** : Black-Body OLR
We will use the simple black-body approximation from iteration 1 of Radiative-Convective Model. That is:
$$
\text{OLR}(T) = \sigma T^4 
$$
:::

We hence finished preparing the forcing term:
$$
\boxed{F(T,\phi) = S_0\cos\phi-\sigma T^4}
$$



### Effects of heat capacity 

Heat capacity $C(\phi)$ is affected by, for instance, the depth we are at. With a taller column of water, we get a larger heat resovoir so reasonably we get higher $C(\phi)$. 

![](image/1d_ebm_seasonal_variation.png)

However for now let's model a simple **aquaplanet** at the surface so we set 
$$
C = 4\left(\frac{kJ}{kg \cdot K}\right)
$$

---
### Semidiscrete Finite Difference 
Let's restate the model:

:::{note} 1D Energy Balance Model
$$ 
    T_t = \frac{1}{C}\left(\textcolor{red}{S_0 |\cos \phi | - \sigma T^4} + \textcolor{blue}{\frac{D}{\cos \phi} \partial_{\phi}  \left( \cos \phi T_{\phi} \right)}\right) 
$$
where the red terms are the radiation forcing and the blue one is the diffusion term. 
The boundary condition is:
$$
T_{\phi}(\phi_0) = 0, \phi_0\in \left\{-\frac{\pi}{2}, \frac{\pi}{2}\right\}
$$
And the inital condition:
$$
T(0, \phi) = T_0
$$
:::

- The name semidiscrete is quite self-explanotry in the sense that we have two conitnous varaibles $T,\phi$ and we would discretize one. 
- In this case, we use the so called **line method** where we discretize the spatial dimension. The result is a system of ODE. 
- Intuitively, imagine a surface $T(t,\phi)$, we reduce into ODE by just focusing on one particular location $\phi'$ and trace the variation of temeprature at that spatial location. This is, of course, an ODE. Geometrically, we are taking slices on lines parallel to the time axis hence the name line method. 

#### STEP1 : Finite Difference Scheme 
We first need to approximate the opeartor $\partial_{\phi}  \left( \cos \phi T_{\phi} \right)$ by a finite difference. I found the following to work well:
$$
\boxed{\partial_{\phi} T(t, \phi_i) = \frac{\cos \phi_{i+1} \frac{T(t, \phi_{i+2}) - T(t, \phi_{i})}{2\Delta \phi} - \cos \phi_{i-1}\frac{T(t, \phi_{i}) - T(t, \phi_{i-2})}{2\Delta \phi}}{2\Delta \phi}}
$$
which just use the 2 order centered difference for first order derivative twice:
$$
f'(x_i) \approx \frac{f(x_{i+1})-f(x_{i-1})}{2\Delta x}
$$


#### STEP2 : Obtain The State-Transition Equation 
I use the following perspective for most finite difference methods for PDEs. 
:::{note} Finite Difference as Subproblems
We can define subproblems as computing $T(t_j, \phi_i)$. To compute this, we need the result of a collection of other subproblems. In our heat equation, it is 
$$\{T(t_{j-1}, \phi_{i+2}), T(t_{j-1}, \phi_{i}), T(t_{j-1}, \phi_{i-2})\}$$
:::

I made the following graph to illustrate the idea:

:::{figure} image/1dedm_subproblems.png

:::

where each arrow depicts dependency, i.e, $A\to B$ if $A$ depends on $B$.

The overall state-transition equation is hence:

:::{prf:proposition} State Transition Equaiton of 1D EBM
\begin{align*}
T_t(t, \phi_i) &= \frac{1}{C} {\huge [ } \frac{D}{\cos \phi_i} {\huge (}\ \frac{\cos \phi_{i+1}}{4\Delta \phi^2}T(t, \phi_{i+2})  \\
&- \frac{\cos \phi_{i+1} + \cos \phi_{i-1}}{2\Delta \phi^2}  T(t, \phi_{i})    \\
&+  \frac{\cos \phi_{i-1}}{4\Delta \phi^2}T(t, \phi_{i-2}) \\
&+ S_0 \cos \phi  {\huge )} - \sigma T^4  {\huge ]}
\end{align*}
:::

In matrix form, we would obtain the overall system of ODEs:

:::{prf:proposition} Matrix Form Of State Transition
Let's define:
$$
\alpha_i = \frac{D}{C\cos \phi_i} \cdot \frac{\cos \phi_i}{4\Delta t^2}
$$
and 
$$
\beta_i = \frac{D}{C\cos \phi_i} \cdot  \frac{\cos \phi_{i+1} + \cos \phi_{i-1}}{2\Delta t^2}
$$
Then the system Of ODE obtained from semidiscretization of the 1d EBM would be:

$$\frac{d\mathbf{T}}{dt} = \begin{pmatrix}
    \purple{\beta_0} & 0 & \alpha_{2} & & & &  \\ 
    0 & \purple{\beta_1} & 0 & \alpha_{3} & & &  \\ 
    \alpha_0 & 0 & \purple{\beta_0} & 0 & \alpha_{4} & &   \\ 
    & \ddots & \ddots & \ddots & \purple{\ddots} &\ddots  & \\
    & &\alpha_{N-5} &0 &\purple{\beta_{N-3}} & 0 & \alpha_{N-1} \\
    & & &\alpha_{N-4} &0 & \purple{\beta_{N-2}} & 0 \\
    & & & &\alpha_{N-3} & 0 & \purple{\beta_{N-1}}\mathbf{T}
\end{pmatrix} + (S_0 \cos\mathbf{\phi} - \sigma \mathbf{T}^4)$$
where $\cos, \mathbf{T}^4$ are element-wise opeartion(i.e, `numpy` broadcasting).
:::

This is a **stiff system[^stiff]**, and for reasons usually discussed in the first lecture of numerical method for PDE/ODE


[^stiff]: Stiffness means the process we are studying(the 'diffusion' of heat has a small time-scale comparing to the interval which we are simulating(which is like, days?)), mathematically, this means the eigenvalues of the state-transition-matrix has very different magnitudes.