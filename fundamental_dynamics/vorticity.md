# Vorticity Equation 

Although intuitive, $(u,v,w)$ isn't the only way we can capture a GFD system. The *vorticity* $\omega$ defined as the curl of the velocity is an alternative. Similar to streamline, we can define **vortex line** which is the tangential field to the vorticity field. 

## Motivation 
Vorticity is interesting because of its **frozen-in** property, characterized by the following proposition:
:::{prf:theorem} Frozen-in Property
Consider unforced($F=0$) and invisicd($\nu=0$) barotropic fluid, the vortex line always coincide the material line. 
:::

We can disregrad what barotropic is for now, this basically says a vortex line always contains the same material elemetns, i.e., it is a property glued to the material. 

Intuitively, we can transform the physical constraint on $u,v,w$ to physical constraint on $\omega$ by taking the curl on both sides of the NS equation. The result is known as the vorticity equation:

:::{prf:proposition} Vorticity Equation
Taking the curl on NS equation obtains: 
$$\frac{D\tilde \omega}{Dt} =  (\tilde \omega \cdot \nabla)v + \frac{\nabla \rho \times \nabla p}{\rho^3} + \frac{1}{\rho}\nabla \times F$$
:::

:::{prf:proof} Vorticity Equation
:class: dropdown 
There is no virtue in deriving this equation as it is pure algebraic manipulation. The identity is applied after taking the curl:
$$
\nabla \times (w\times v) = (v\cdot \nabla)w - (w\cdot \nabla)v + w\nabla \cdot v - v\nabla \cdot w
$$
:::

## Barotropic and Baroclinic Fluid 
The term $\frac{\nabla \rho \times \nabla p}{\rho^2}$ is often known as the **baroclinic term** for a good reason, as explained below.


:::{prf:definition} Barotropic and Baroclinic Fluid 
- *Baroclinic fluid* has $\nabla p$ not parallel to $\nabla \rho$
- *Barotropic fluid* has $\rho=\rho(p)$, i.e. density is just a function of pressure. As a result $\nabla p$ is parallel to $\nabla \rho$
:::
A clarification is needed to for why $\rho=\rho(p)$ implies the gradients are parallel. A short proof reads like:
:::{math}
\nabla \rho \times \nabla p = \nabla \rho \times 
\begin{pmatrix}
\frac{d p}{d \rho} \frac{\partial \rho}{\partial x} \\
\frac{d p}{d \rho} \frac{\partial \rho}{\partial y} \\
\frac{d p}{d \rho} \frac{\partial \rho}{\partial z} \\
\end{pmatrix}
=\frac{dp}{d\rho}\underbrace{\nabla \rho \times \nabla \rho}_{0}=0
:::

Hence for barotropic fluid the baroclinic term disappears and we have:
$$
\boxed{\frac{D\tilde \omega}{Dt} = (\tilde \omega \cdot \nabla)v + \frac{1}{\rho} F}
$$
In the simplest case, if $F=0$ and $\rho$ is constant(*imcompressible*) we have
\begin{align*}
\frac{D\omega}{Dt} &= (\omega \cdot \nabla)v 
\qquad \qquad &\text{(Barotropic;Imcompressible)}
\end{align*}

## Topological Properties of The Vorticity Field
:::{prf:definintion} Vortex Line 
:::


