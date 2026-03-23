---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Energy Balance Model 

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
\text{ASR}(\phi_0) = S_0|\cos(\phi_0)|
$$
:::
:::{prf:proof} Proof of Explict Form Of ASR
We first need to write $ASR$ and $OLR$ explicitly as a function of $(T, \phi)$.For absorbed incoming short wave radiation, recall the flux density is $S_0$. Now consider a thin strip parallel to the equator that correspond to a $(\phi_0, \phi_0+\delta \phi)$. The **flux density** to the strip is:
\begin{align*}
\text{Flux Density} &= \lim_{\delta \phi \to 0} \frac{\text{Total Flux}}{\text{Total Area}} \\

&= \lim_{\delta \phi \to 0} \frac{\int_{0}^{\pi} d\theta \int_{\phi_0}^{\phi_0+\delta \phi} d\phi r^2\sin(\phi)S_0|\cos\phi|}{\int_{0}^{\pi} d\theta \int_{\phi_0}^{\phi_0+\delta \phi} d\phi  r^2 \sin(\phi)} \\

&=\lim_{\delta \phi \to 0} \frac{\pi \int_{\phi_0}^{\phi_0+\delta \phi} d\phi r^2\sin(\phi)S_0|\cos\phi|}{\pi \int_{\phi_0}^{\phi_0+\delta \phi} d\phi  r^2 \sin(\phi)}
\end{align*}
A standard result from mathematical analysis:
$$
\lim_{\delta a\to 0}\frac{\int_a^{a+\delta a}f}{\int_a^{a+\delta a}g} = \frac{f}{g}, \forall g\neq 0
$$
which gets us:
\begin{align*}
&= S_0 |\cos\phi |
\end{align*}
:::

:::{note} **Assumption** : Black-Body OLR
We will use the simple black-body approximation from iteration 1 of Radiative-Convective Model. That is:
$$
\text{OLR}(T) = \sigma T^4 
$$
:::

We hence finished preparing the forcing term:
$$
\boxed{F(T,\phi) = S_0|\cos\phi|-\sigma T^4}
$$



### Effects of heat capacity 

Heat capacity $C(\phi)$ is affected by, for instance, the depth we are at. With a taller column of water, we get a larger heat resovoir so reasonably we get higher $C(\phi)$. 

![](image/1d_ebm_seasonal_variation.png)

However for now let's model a simple **aquaplanet** at the surface so we set 
$$
C = 4\left(\frac{kJ}{kg \cdot K}\right)
$$

### Semidiscrete Finite Difference Scheme
Let's rewrite the equation cleanly:
:::{note} Model Description
$$
T_t = \frac{S_0|\cos\phi| + \sigma T^4 }{C}-\frac{D}{C}\tan\phi T_{\phi}+ D T_{\phi\phi}  
$$
We can use a uniform initial condition and wait for the aquaplanent to be heated up gradually: 
$$
T(0,\phi) = 0K
$$
Also, we impose **Neumann conditions** at the boundaries, that is, the poles where no heat can can flow through[^nbc]. 

$$
T_{\phi}(t,\phi) = 0, \phi\in \{0, \pi\}
$$
:::

Now that we reduced a physical situation to a standard PDE with proper initial and boundary conditions, we are ready to *simulate*! That is, to numerically solve the equation. 

#### Line Method 

$T(t, \phi)$ is a bivariate function and we hence get a PDE. However, we can discretize the spatial dimension and thus reduce the PDE into ODE. This means we are 
tracing the temperature at a particular latitude as time marches on. Generally, imagine $T(t,\phi)$ being a surface, we are taking cross sections that are parallel to the time axis, hence the name *line method*. 

We discretize the spatial dimension : $[\phi_1, \phi_2,....,\phi_N]$ where $N$ is discretization resolution. Let's use the following finite difference scheme:

:::{math}
\begin{cases}
    T_{\phi}(t,\phi_{i}) \approx \frac{T(\phi_{i+1}, t)-T(\phi_i, t)}{2\Delta t} \\
    T_{\phi\phi}(t,\phi_{i}) \approx \frac{T(\phi_{i+1}, t)-2T(\phi_{i}, t) + T(\phi_i, t)}{\Delta t ^2} \\
\end{cases}
:::

which has a local truncation error $\mathcal O(\Delta t^2)$.

Let's denote the forcing term as $F(\phi, T)\equiv \frac{S_0|\cos \phi| + \sigma T^4}{C}$. Writing out each term we get, for $\phi_i$:
$$
T_{t}(t,\phi_i) &= F(T(t, \phi_i)) -  T(\phi_{i+1} ,t) \left\{ \frac{D}{\Delta t^2} - \frac{D\tan \phi_i}{2C\Delta t} \right\} \\
&+ T(\phi_i, t)\left\{ -\frac{2D}{\Delta t^2}\right\} \\
&+ T(\phi_{i+1},t)\left\{ \frac{D}{\Delta t^2} + \frac{D\tan \phi_i}{2C\Delta t} \right\}
$$

:::
:::
In matrix form, we get:

$$
\frac{dT}{dt} = 
\begin{pmatrix}
 
\end{pmatrix}
$$




[^nbc]: Technically we can flow through the pole, however, as all trajectories converge to a single point(which is measure-zero), there is essentially no area for the heat to diffuse through even though temperature difference exists.
