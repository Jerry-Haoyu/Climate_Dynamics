# Wind-driven Circulation

## Ekman Transport
:::{prf:theorem} Ekman Transport 
If we define mass-transport in the ekman layer as a vertical integral:
$$
\mathbf{M}_{ag} = \int_{Ek} \rho_0 \mathbf{u}_Edz 
$$
Then we get that *ekman transport is orthogonal to the wind stress*, formally:

At top ekman layer(ex. ocean surface), we have:
$$\mathbf{M_{ag}} &=-\frac{1}{f} \mathbf{k} \times \boldsymbol{\tau_{T}}$$

:::

### Geostrophic Equation 
Recall **frictional-geostrophic** balance gives us the simplified primitive equations:
$$
\begin{cases}
\mathbf{f}\times \mathbf{u} &=-\nabla_z \phi + \frac{1}{\rho_0}\frac{\partial \tau}{\partial z} \\ 
\frac{\partial \phi}{\partial z} &= 0 \\
\nabla \cdot \mathbf{v} &= 0
\end{cases}
$$
where 
- first equation is a horizontal momentum equation that looses its advection term as $Ro\to 0$
- second equation we used hydrostatic balance 
- the last equation being the continuity equation. 

Now we recall that sufficiently far away from the boundary layer, we have *geostrophic balance*, but near the boundary friction increases hence coriolis force 
would decrease. Nevertheless pressure gradient force remains roughly the same. Hence we need a boundary layer correction:
$$
\phi = \phi_g + \phi_{ag}
$$
:::{note}Claim
We calim that $\phi_{ag} = 0$, $\forall z$ if the whole layer is hydrostatic
:::
This follows since 
$$
\frac{\partial \phi }{\partial z} = \frac{\partial_g \phi }{\partial_{g} z}  + \frac{\partial_{ag} \phi }{\partial_{ag} z}= 0
$$
But $\frac{\partial_g \phi }{\partial_{g} z} = 0$(interior is always hydrostatic) so 

$$
 \frac{\partial_{ag} \phi }{\partial_{ag} z}= 0
$$
i.e., the ageostrophic potential is also constant. 
In addition, we know that $\exists z$ such that $\phi_{ag}(z)=0$, hence the $\phi_{ag}=0$ everywhere. 

This simplies the horizontal momentum equation as 
:::{attention} Hydrostatic Balance Simplified Geostrophic Equation
$$
\mathbf{f}\times \mathbf{u} &= \frac{1}{\rho_0}\frac{\partial \tau}{\partial z}
$$
:::

#### Ageostrophic Transport : Horizontal Motion
Integrating w.r.p to $z$ on both sides gets us:


$$
\mathbf{f}\times \int_{Ek}  \rho_0\mathbf{u} dz &= \int_{Ek}\frac{\partial \tau}{\partial z} \\
\mathbf{f}\times\mathbf{M_{ag}}  &= \boldsymbol{\tau_{T}}-\boldsymbol{\tau_{B}}
$$

Where we define the **agestrophic transport** as:
:::{prf:definition} Agestrophic Transport
$$
\mathbf{M}_{ag} \equiv \int_{Ek} \rho_0 \mathbf{u}dz
$$
:::

Consider the specific instance of top Ekman layer, we have:
$$
\mathbf{f}\times\mathbf{M_{ag}} &= \boldsymbol{\tau_{T}} \\
f\mathbf{k}\times\mathbf{M_{ag}} &= -\frac{1}{f} \boldsymbol{\tau_{T}} \\
\mathbf{k} \times f\mathbf{k}\times\mathbf{M_{ag}} &= -\mathbf{k} \times \frac{1}{f} \boldsymbol{\tau_{T}} \\ 
\mathbf{M_{ag}} &=-\frac{1}{f} \mathbf{k} \times \boldsymbol{\tau_{T}} 
$$

#### Ekman Pumping/Sucking : Vertical Motion
:::{prf:proposition}
The vertical velocity of the ekman layer is given by:
$$
w_E = \frac{1}{\rho_0}\left(\mathrm{curl_z}\frac{\tau_T}{f} \right)
$$
:::

:::{prf:proof} 
Start from the continuity equation:
$$
\int_{Ek}\partial_z w dz &= - \frac{1}{\rho_0}\int_{Ek} \nabla_2 \cdot (u, v) dz \\
(w_T - w_B) &= - \frac{1}{\rho_0}\nabla \cdot \mathbf{M_{ag}} \\
w_T &= - \frac{1}{\rho_0} \nabla \cdot \mathbf{M_{ag}} \\
w_T &= -\frac{1}{\rho_0}  \nabla \cdot \left(\frac{1}{f} k\times \tau_{T}\right)
$$

Now recall the divergence of a cross product is:
$$
\nabla \cdot (A\times B) = (\nabla \times A)\cdot B  - A \cdot (\nabla \times B)
$$
where we can regard $k$ to be a constant vector field(clearly curl-free). Hence we have 


$$
w_T &= - \frac{1}{f}\left(- k\cdot \nabla \times \left(\frac{\tau_{T}}{f}\right)\right) \\
&= \frac{1}{\rho_0}\left(\mathrm{curl_z}\frac{\tau_T}{f} \right)
$$

:::

### Real World Example 

#### Antarctic Transport

## Stommel Model
:::{prf:lemma} Cross-Differentiation
Given that $Ro<<1$, alongside with *Boussinesq Approximation, Hydrostatic Approximation* as well as the frictional approximation $\mathbf{F}=\frac{\partial \mathbf{\tau}}{\partial z}$ we can rewrite the **horizontal momentum equation** as:
$$
\beta v = \mathbf{k}\cdot \nabla \times (\partial_z \mathbf{\tau})
$$
:::
Starting again with the horizontal momentum equation with advection term omitted:
$$
f\times u = \nabla \phi + \partial_z \tau 
$$
We take the curl on both sides:
$$
\nabla \times (\mathbf{f}\times \mathbf{u}) &= \mathbf{f}(\nabla \cdot \mathbf{u}) - (\mathbf{f}\cdot \nabla) \mathbf{u} -
 [\mathbf{u}(\nabla \cdot \mathbf{f}) - (\mathbf{u}\cdot \nabla) \mathbf{f}]
$$
Note that the $\nabla \cdot \mathbf{f} = 0$ since 
$$
\mathbf{f}=\begin{pmatrix}
0 \\
0 \\
f(y)
\end{pmatrix} 
$$
As a result we can kill $\mathbf{u}(\nabla \cdot \mathbf{f})$, also 

$$
(\mathbf{f}\cdot \nabla) \mathbf{u} = 
\begin{pmatrix}
0 \\ 0 \\ f(y)
\end{pmatrix}
\cdot 
\begin{pmatrix}
u \\ v \\ 0
\end{pmatrix} =0 
$$
and 
$$\mathbf{u}\cdot \nabla \mathbf{f}=\begin{pmatrix} 0 \\ 0 \\ \beta v \end{pmatrix}
$$
The only surviving term is $\mathbf{f} (\nabla \cdot \mathbf{u}) + \begin{pmatrix} 0 \\ 0 \\ \beta v \end{pmatrix}$.
On the R.H.S, the first term is the curl of a gradient hence $0$. Collecting all terms:
$$                  
\mathbf{f} (\nabla \cdot \mathbf{u}) + \begin{pmatrix} 0 \\ 0 \\ \beta v \end{pmatrix}= \nabla \times \partial_z \mathbf{\tau}
$$
Now recall that:
:::{prf:proposition}
In **Boussinesq approximation**[^bsnsqaprox], the velocity field becomes *divergence free*, i.e.:
$$
\nabla \cdot \mathbf{u}=0
$$
:::
:::{prf:proof}
From the continuity equation:
$$
\frac{D\rho }{Dt} + \rho \nabla \cdot \mathbf{u}=0 
$$
If $\frac{D\rho }{Dt}=0$, then $\rho(\nabla \cdot \mathbf{u})=0$. As desired
::: 
Therefore, our 3D equations becomes 2D:
$$
\boxed{\beta v = \mathbf{k}\cdot (\nabla \times \partial_z  \mathbf{\tau})}
$$

We already have most of the algebra done! However, the true novelty of Stommel lies with the simple assumption:
:::{attention} Ralayeigh Friction
At the bottom of ocean, we approximate stress as a linear drag:
$$
\mathbf{\tau_B}=r\mathbf{u}
$$
:::
:::{prf:theorem} Stommel Model
Using the ralayeigh friction, given surface windstress curl $F_{\tau}(x,y): \mathbb{R}^2 \to \mathbb{R}^2$. There exists a function $\psi : \mathbb{R^2} \to \mathbb{R}$ such that:
$$
u &= - \frac{\partial \psi}{\partial y} \\
v &=  \frac{\partial \psi}{\partial x}
$$
where $\mathbf{u}_2$ is the $u,v$ component of the full velocity field and it satisfies that:
$$
\boxed{r\nabla ^2 \psi + \beta \frac{\partial \psi}{\partial x} = F_{\tau}(x,y)}
$$
:::

We need a simple lemma:
:::{prf:lemma}
Let $\mathbf{u}=(u,v,w)$ be a vector field.Suppose $\nabla \cdot \mathbf{u}=0$ in a simply connected region, and **if $w=0$** then we can find a *stream function* $\psi:\mathbb{R}^3\to \mathbb{R}$ such that $u=-\partial_y \psi, v=\partial_x \psi$.
:::

:::{prf:proof}
Recall that divergence free guarantees a vector potential function, i.e., $\exists \mathbf{A}=(A_x, A_y, A_z), \nabla \times A = \mathbf{u}$. We need to show we can pick $A_x=0, A_y=0$.Firstly, there must exists an $\mathbf{B}$ such that:
$$
\nabla \times \mathbf{B} = \begin{pmatrix}
\partial_y B_z - \partial_z B_y \\
\partial_z B_x - \partial_x B_z \\
\partial_x B_y - \partial_y B_x
\end{pmatrix}
$$
We can let our deisred $\mathbf{A}=\mathbf{B}+\nabla g$ for some scalar function $g$. Now, the desired relationship is:
$$
B_y &= -\partial_y g \\
B_x &= -\partial_x g \\
$$
which is equivalent to the **exact differential equation**:
$$
g=B_ydy + B_xdx
$$
The condition for solution to exists is:
$$
\partial_x B_y = \partial_y B_x
$$
But this is equivalent to $w=\partial_x B_y - \partial_y B_x=0$. Now we let $\mathbf{A}=\mathbf{B}+g$ , $\psi = \mathbf k \cdot \mathbf{A}$ and we are done.
:::
We're now read to show *Stommel's model*:
:::{prf:proof}
$$
\int \beta v dz &= \int \mathbf{k} \cdot (\nabla \times \partial _z \mathbf{\tau}) \\ 
\beta \bar v &= \mathbf{k} \cdot \left[\nabla \times  (\mathbf{\tau}_{S}- \mathbf{\tau}_{B})\right]
$$
Now using the surface wind stress and the rayleigh friction, the R.H.S becomes $F_\tau(x,y)- r\bar \zeta$ since:
$$
\mathbf{k} \cdot \nabla  \times \boldsymbol{\tau}_S-\mathbf{k} \cdot \nabla \times  \boldsymbol{\tau}_B &=
F_{\tau}(x,y)- r\mathbf{k} \cdot \nabla \times  \mathbf{u}_B 
$$
For convenience, we would replace $\mathbf{u}_B \approx \overline{\mathbf{u}}$, i.e., the vertically integrated velocity field.

As a result we get:
$$
\beta \overline{v} = F_\tau(x,y)- r\overline{\zeta}
$$
Now note since we have **Boussineq Approximation**, we have a divergence-free field. By the lemma, there exists a stream function $\psi$. Now, the vertically integrated vorticity is just:
$$
\nabla \times \overline{\mathbf{u}}=\partial_xv-\partial_y u &= \partial_{xx}\psi + \partial_{yy}\psi \\
&=\nabla^2 \psi
$$
and we are done.
            
:::
[^bsnsqaprox]: ignores density differences except where they appear in terms multiplied by $g$