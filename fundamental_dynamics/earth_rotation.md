# Earth's rotation 

## Rotating Frame 
Let $(X,Y,Z)$ be the rotating frame and $(x,y,z)$ denote the inertial frame, clearly:

```{math}
\begin{pmatrix}
X \\
Y
\end{pmatrix} = 
\begin{pmatrix}
\cos \Omega t & \sin \Omega t \\
-\sin \Omega t & \cos \Omega t 
\end{pmatrix}

\begin{pmatrix}
x \\
y
\end{pmatrix}

```

The rotation axis was parallel to $z$ hence $Z=z$. The coordinate transformation matrix from rotational frame to inertial frame is then:

```{math}
\begin{pmatrix}
\cos \Omega t & \sin \Omega t & 0\\
-\sin \Omega t & \cos \Omega t & 0\\
0 & 0 & 1
\end{pmatrix}
```

:::{prf:remark}
Note the change of coordinate matrix above changes a vector represented in rotating frame to a vector represented in inertial frame. However, it also changes the basis vector from inertial frame to rotating frame. Such opposite direction is referred to as **contravariant transformation**. 
:::

## Momentum Equation After Transformation

Recall that the *Boussinisq momentum equation* takes the form:
```{math}
:label: bme
D_t\mathbf{u} = -\nabla \phi - g \frac{\rho}{\rho_0}\mathbf{z}+\mathbf{F}
```

We consider this equation transformed into rotating frame. The time derivative of vector $\mathbf{v}$ in the rotating frame relates to its representation in inertial frame by the following equation:
$$
D_t \mathbf{v}|_s = D_t\mathbf{v} |_r + \Omega \times \mathbf{v}
$$
We substitue $\mathbf u$ as $\mathbf v$ into the L.H.S of  [](bme)

\begin{align*}
D_t\mathbf{u}|_v = D_T \mathbf{u}|_r + \Omega \times (\mathbf{u})
\end{align*}



