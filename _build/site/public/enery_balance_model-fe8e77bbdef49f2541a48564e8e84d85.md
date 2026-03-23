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
Run the cell to get an interactive plot explaining the discretization where you can change the resolution and perspective!

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

We first need to write $ASR$ and $OLR$ explicitly as a function of $(T, \phi)$.For absorbed incoming short wave radiation, recall the flux density is $S_0$. Now consider a thin strip parallel to the equator that correspond to a $(\phi_0, \phi_0+\delta \phi)$. The total flux to the strip is:
$$
\int_{0}^{\pi}d\theta \int_{\phi}^{\phi + \delta \phi}d\phi r^2\sin(\phi)S_0|\cos(\phi)| 
$$
which gets us:
\begin{align*}
    &= S_0\pi r^2 [-\cos(2\phi)]_{\phi_0}^{\phi_0 + \delta \phi} \\
    &= S_0\pi r^2 (\cos(2\phi_0)-\cos(2(\phi_0 + \delta\phi))) \\
    &= S_0 \pi r^2\left[ \cos(2\phi_0) - (\cos(2\phi_0)\cos(\delta \phi) - \sin(2\phi_0)\sin(\delta ))\right]
\end{align*}


### Effects of heat capacity 

Heat capacity $C(\phi)$ is affected by, for instance, the depth we are at. With a taller column of water, we get a larger heat resovoir so reasonably we get higher $C(\phi)$. 

![](image/1d_ebm_seasonal_variation.png)

