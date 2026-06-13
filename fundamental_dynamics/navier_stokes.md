# Navier-Stokes Equation

$$\LARGE{\text{This is where the story begins}}$$

## The Material Perspective 

There are two natural perspetives to model fluid:
:::{note} Two Perspectives
1. (**Eulerian/Field Perspective**) Qeury about properties at location $\mathbf x$. For instance, how fast is temperature changing at $(x,y,z)$?
   
2. (**Lagrangian/Material Perspective**) Qeury about properties of the fluid element. Essentially asking, if we consider the fluid element currently at $(x,y,z)$, how fast is its temeprature changing.
::: 

It turns out that the material perspective is vastly useful.The translator from eulerian perspective to lagrangian perspective is the so-called **material derivative**. The key idea is that to query about some property of interest(like temperature, for instance) for a fluid element, we ask two questions in the following order:

1. Where is the fluid element now ? Answer : at some location $\mathbf x$
2. What is the field property of interest $\phi$ at at that location $\mathbf x$ ? Answer : $\phi(\mathbf{x})$

The mathematical structrue of the above "nested continuous dependency" relationship is just composition of functions, and the rate of change is hence given straigtfowardly by *chain rule*.

:::{prf:definition} Material Derivative
Suppose we have the velocity field $\mathbf{u}:\mathbb{R}^3 \to \mathbb{R}^3$, suppose the property of interest is given as a filed $\phi : \mathbb{R}^3 \to \mathbb{R}^k$, define the material derivative as the time derivative of the property of the fluid element, by chain rule, it is given by:
$$
\frac{D\phi}{Dt} = \frac{\partial \phi}{\partial t} + (\mathbf{u}\cdot \nabla)\phi
$$
where the $D/Dt$ is the notation for material derivative, the operator is defined as:
$$
\frac{D}{Dt}=\frac{\partial }{\partial t} + \mathbf{u} \cdot \nabla 
$$
:::

:::{prf:proof} 
:class: dropdown
Taking the time-derivative of $\phi(x_1(t),x_2(t),x_3(t),t)$:
$$
\frac{d\phi}{dt} = \frac{\partial \phi}{\partial t} + \sum_{i=1}^3\frac{\partial \phi}{\partial x_i}\frac{d\partial x_i}{\partial t}
$$
recognizing the summation as a dot product:
$$
\frac{d\phi}{dt} = \frac{\partial \phi}{\partial t} +   (\nabla \phi) \cdot \mathbf{u}
$$
Note if $k>1$, $\nabla \phi$ would be a $k\times 3$ matrix and the dot product becomes a matrix-vector multiplication.
:::

A major advantage of the material perspective is that divergence theorem is trivial:
:::{prf:proposition} Divergence Theorem
$$\frac{D}{Dt} \int_{\Omega} dV = \int_{\Omega} \nabla \mathbf{u} dV$$
:::
since the advection term in the material derivative already takes care of the advecting phenomenon so we can essentially view the divergence theorem as it was statically. 

Two corollaries:
:::{prf:corollary} 
$$
\frac{D}{Dt}\int_{\Omega} \phi dV = \int_{\Omega}\left\{ \frac{D}{Dt}\phi + \phi \cdot \nabla \mathbf{u} \right\}dV
$$
:::
:::{prf:proof}
:class: dropdown
$$
\frac{D}{Dt}\int_{\Omega} 1 \cdot \phi dV &=
\int_{\Omega} \nabla \mathbf{u} \cdot \phi + \frac{D}{Dt}\phi dV
$$
:::

## The Navier-Stokes Equation

### Momentum Equation
The momentum equation in NS equation is just newton's second law. 
$$ 
\frac{D}{Dt}\int_{\Omega} \rho \mathbf{u} dV  = \int_{\Omega} \mathbf{F} dV
$$
Exchanging integration and derivative:
$$
\int_{\Omega} \rho \frac{D\mathbf{u}}{Dt} dV &=  \int_{\Omega} \mathbf{F} dV\\
$$
Hence:
:::{note} General Momentum Equation
$$
\int_{\Omega}\partial_t \mathbf{u} + (\mathbf{u}\cdot \nabla)\mathbf{u} &= \int_{\Omega}\frac{\mathbf{F}}{\rho}
$$ (gme)
:::

#### Body Force and Contact Force
It can be seen in {eq}`gme` that the L.H.S is generic for any fluid. The difference between different fluids and the forcing exerted on them is all encapsulated in the forcing term $\mathbf{F}$. 
:::{prf:definition} Body Force and Contact Force
In general the force on the fluid can be roughly categorized as body force and contact force. 
1. The internal force due to interaction between fluid particle which give rise to viscosity and pressure force is known as **contact force**.
2. External forces is known as **body force**
   
In that case we denote by:
$$
\mathbf{F}=\mathbf{F}_b + \mathbf{F}_{c}
$$


with the contact force further decomposed to pressure and viscosity : 
$$
\mathbf{F}=\mathbf{F}_b + \int_{\Omega}\nabla p + \mu\nabla^2 \mathbb{u}dV
$$

where $\nabla p$ is the *pressure term* and $\mu \nabla^2 \mathbf{u} $ is the *viscosity term*
:::
We derive the pressure term explicitly here:

The pressure force on the fluid element enclosed by $\partial \Omega$ is just:
$$
\mathbf{F}_p = -\int_{\partial \Omega} p\cdot \mathbf{n}dS
$$
where the minus sign is to counter the fact that normal vector points outwards. Applying divergence theorem we get:
$$
\mathbf{F}_p = -\int_{\Omega}\nabla p dS
$$

The viscosity term on the other hand requires *incompressibility approximation* and is inexact. We take it as it is. However, one word about this term is required about a common pitfall. The laplacian is normally introduced as a scalar valued function $\mathbb{R}^3 \to \mathbb{R}$ which immediately results in a dimensionality mismatch. This is due to a notation polymorphism, $\nabla^2 \mathbf{u}$ here is a *vector laplacian* $\mathbb{R}^3 \to \mathbb{R}^3$ defined as:

\begin{pmatrix}
\nabla^2 u \\
\nabla^2 v \\
\nabla^2 w \\
\end{pmatrix}


Now we have the momentum equation.Since $\Omega$ is arbitrary, we remove the integrals:
:::{prf:proposition} Momentum Equaton 
$$
\frac{D\mathbf{u}}{Dt} &=  -\frac{1}{\rho} \nabla p + \nu \nabla^2 \mathbf{u} + \mathbf{F}_b \\
$$
where $\nu=\mu/\rho$ is the *kinemetic viscosity*($m^2s^{-1}$) and $\mathbf{F}_b$ is the external force per unit mass(e.g. gravity would be $-g$ in the z-component).



If we assume gravity is the only body force, the component form is:
$$
D_t u &= -\frac{1}{\rho} \partial_x p + \nu \nabla^2 u \\
D_t v &= -\frac{1}{\rho} \partial_y p + \nu \nabla^2 v \\
D_t w &= -\frac{1}{\rho} \partial_z p - g
$$
where we've omitted the viscosity term for the z-component since it is much less significant than pressure and gravity.
:::



### Continuity Equation

Continuity equation is just the mathematical expression for mass conservation, or:
$$
\frac{D}{Dt}\int_{\Omega} \rho dV = 0 \\
$$
We would like to translate this constraint explicitly to an constraint on $\mathbf{u}$.
$$
\frac{D}{Dt}\int_{\Omega} \rho dV &=
$$
By arbitrariness of $D$:
$$
 \frac{D(\rho \nabla \mathbf{u})}{Dt} &=0
$$