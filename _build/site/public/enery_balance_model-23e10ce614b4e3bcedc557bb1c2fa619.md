
---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# Energy Balance Model 

## Heat Equation In Spherical Coordinate 
:::{prf:proposition}
$$
\begin{equation}
    C(\phi) \frac{\partial T_s}{\partial t} = ASR(\phi)-OLR(\phi) + \frac{D}{\cos \phi}\frac{\partial }{\partial \phi}\left(\cos \phi \frac{\partial T_s}{\partial \phi}\right)
\end{equation}
$$
:::
where 
- $C(\phi)$ is constant pressure heat capacity at some latittude $\phi$

which is a standard 1D heat equation.

An idealized model for $ASR$, $OLR$ woud give

:::{prf:proposition}
$$
\begin{equation}
    C(\phi) \frac{\partial T_s}{\partial t} = (1-\alpha)Q(\phi)- (A+BT_s) + \frac{D}{\cos \phi}\frac{\partial }{\partial \phi}\left(\cos \phi \frac{\partial T_s}{\partial \phi}\right)
\end{equation}
$$
:::


### Effects of heat capacity 

Heat capacity $C(\phi)$ is affected by, for instance, the depth we are at. With a taller column of water, we get a larger heat resovoir so reasonably we get higher $C(\phi)$. 
![](image/1d_ebm_seasonal_variation.png)

### Importance of advection 

![](image/effect_of_diffusivity.png)