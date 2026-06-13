# Earth's Rotation 

## Rotation Frame 
Rotation frame can be viewed as a continuous change of coordinate. At time $t$, given angular speed $\Omega$, the rotating frame has basis
$$
\left\{\begin{pmatrix}
\cos \Omega t\\  
\sin \Omega t\\ 
0 \\
\end{pmatrix}, \begin{pmatrix}
-\sin \Omega t\\  
\cos \Omega t\\ 
0 \\
\end{pmatrix},\begin{pmatrix}
0\\  
0\\ 
1 \end{pmatrix}\right\}
$$
Hence the change of coordinate to inertial frame from the rotating frame is given by:
:::{prf:proposition} Change Of Coordinate To Inertial Frame 
Let $r_R=(x_R,y_R,z_R)$ be the position vector in rotating frame and $r_I=(x_I,y_I,z_I)$ be the inertial counter parts. Then:
$$
r_I = R r_R
$$
where 
[^cvt]
$$
R=\begin{pmatrix}
\cos \Omega t & -\sin \Omega t & 0 \\
\sin \Omega t & \cos \Omega t & 0 \\ 
0 & 0 & 1
\end{pmatrix}
$$ 
::: 

It is now quite easy to obtain the change of coordinate for the velocity vector:

$$
\frac{dr_I}{dt}=\frac{dR}{dt}r_R + R\frac{dr_R}{dt}
$$

We want to make the coefficient of $\frac{dr_R}{dt}$ to be $0$. Recall that $R$ is an orthogonal matrix hence $R^TR=I$, this motivates us to multiply both side by $R^T$:
$$
R^T\frac{dr_I}{dt}=R^T\frac{dR}{dt}r_R + \frac{dr_R}{dt}
$$

:::{prf:lemma} Quick Computational Fact : Emergence of Cross Product
:label: ecp
$$
R^T\frac{dR}{dt}r_R = \boldsymbol{\Omega} \times r_R
$$
where $\boldsymbol \Omega = (0,0,\Omega)^T$
::: 

:::{prf:proof} Emergence of Cross Product
:class: dropdown
Note 
$$R^T\frac{dR}{dt}=\begin{pmatrix}
0 & -\Omega & 0 \\
\Omega & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}$$
It then becomes trivial to notice the equivalence. 
:::
Multiply by $R$ again, we obtain the well-known formula:
:::{prf:proposition} Change of Coordinate Formula For Velocity Vector  
$$\frac{dr_I}{dt}=R\left(\frac{dr_R}{dt}+\boldsymbol{\Omega} \times r_R\right)$$

Rmk. the formula also applies if $\Omega$ is time-varying, i.e. $\Omega=\Omega(t)$. One only need to check [](ecp) still hold. 
:::




[^cvt]: Note how $R$ contains basis of the rotating frame represented in inertial coordinate(i.e. the basis are changed to rotating basis) but $R$ itself transforms rotating basis to inertial basis. Such transformation with opposite direction is referred as "contravariant transformation"
