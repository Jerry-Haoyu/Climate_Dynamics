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

:::{note} Summary
This note aims to develop a simple model called the **energy balance model** that depicts the tempearture distribution across latitude due to differential heating.  In particular, we are considering an static aquaplanet with no fluid dynamics. We first discretize the space across latitude to obtain "rings". We allow heat to transfer between rings and establish a 1D parabolic equation[^pe] by conserving radiative forcing and diffusion of heat. We then solve the equation by numerically solving the equation. **The following animation shows the result**:
:::

:::{figure} output/global_plot_surface.mp4

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

#### STEP3: Backward Step

This is a **stiff system[^stiff]**, and for reasons usually discussed in the first lecture of numerical method for PDE/ODE, we need to take baby steps in euler steps to prevent the instability blowing up the solution. However, it is also known taht backward step doesn't have this problem. Let's first recall what is a backward step. 

:::{prf:definition} Backward step/Implicit method For Model Problem

Consider the model problem $y'=Ay+b$. We can write the state transition as:

$$y_{i+1}=y_{i}+(Ay_{i+1}+b)dt$$

Therefore, solving for $y_{i+1}$ we get:

$$y_{i+1} = (I-Adt)^{-1}(bdt+y_{i})$$
:::

Consider the case when $b=0$, we get:

$$y_{k} = ((I-Adt)^{-1})^ky_{0}$$

It can be proven that:

:::{prf:lemma} Eigenvalue of $(I-Adt)^{-1}$
Let the eigenvalues of $A$ be $\lambda_1,...,\lambda_n$, then the eigenvalues of $(I-Adt)^{-1}$(provided they exists) are $\frac{1}{1-\lambda_1dt},\frac{1}{1-\lambda_2dt},....,\frac{1}{1-\lambda_ndt}$
:::

The proof is out of the scope of this course note, however, one can consider the special case when $A$ is diagonalizable : $A=P^{-1}DP$, then $$(I-Adt)^{-1}= (I-PDdtP^{-1})^{-1}=P^{-1}(I-Ddt)^{-1}P$$ where $(I-Ddt)^{-1} = \mathrm{diag}(\frac{1}{1-\lambda_1dt}, ..., \frac{1}{1-\lambda_ndt})$, as desired.

As a result, eigenvalues of $(I-Adt)^{-1}$ has magnitude less than 1 for all positve step size $dt$ provided that all eigenvalues of $A$ are negative. In otherword, stability is always acheived no matter how small the step-size is. This is known as **unconditional stability**.The conclusion is hence:

:::{tip} Backward step
For stiff system like 1d EBM, always use backward step when using finite difference methods! 
:::

We are now ready to dive into the numerical world. Talk is cheap, Let's CODE!

:::{warning}
The following snippets takes $\sim 1\text{minute}$ to  run, please open a jupyter server to proceed with the computation as the free binder service is not quite sufficient. 
:::

#### Naive Energy Balance Model
With all the theory discussed, we can code up the scheme rather quickly[^fdb].


:::{code-cell}python
class oneDimensionalEBM :
    """1D energy balance model with aquaplanet with second order accuracy in space and first order accuarcy in time
    """
    def __init__(self, N, total_it, dt, T_initial):
        #-----------------model hyperparamter-----------------
        self.N = N
        self.total_it = total_it 
        self.dt = dt
        self.dphi = np.pi / N
        
        #----------------physical constants------------------
        #unit : Jday^{-1}m^{-2} #soloar radiation flux density
        self.S0 = 1370 * 0.7 / 4  * 3600 * 24
        self.T_initial = T_initial 
        self.sigma = 5.67 * 1e-8 * 3600 * 24 #unit: Jday^{-1}m^{-2}K^{-4}
        
        #thermal diffuisivity
        self.D_water =  3 * 1e-6 * 3600 * 24 #m^{2}day^{-1} 
        self.C_water = 4000 #400 J/kg/K

        
        #------------------derived constants--------------------
        self.phi : np.ndarray = np.linspace(-np.pi/2+1e-2, np.pi/2-1e-2, self.N) 
        self.cosphi_i = np.cos(self.phi)
        self.cosphi_i_minus_one = shift_numpy_array(np.cos(self.phi), -1)
        self.cosphi_i_plus_one =  shift_numpy_array(np.cos(self.phi), 1)
        
        #-------------allocate resource for result----------------
        self.T_video = np.empty((total_it, N)) + 0.0
        self.T_video[0] = np.ones_like(self.phi) * self.T_initial 
    
    def compute_linear_system(self, T_prev):
        # bias/forcing
        b = (self.S0 * np.abs(np.cos(self.phi)) - self.sigma * (T_prev ** 4))/self.C_water

        # "state-transition matrix"
        diagonal = np.diag(-self.D_water * ((self.cosphi_i_minus_one + self.cosphi_i_plus_one) / (4 * (self.dphi ** 2) * self.cosphi_i)))
        sup_diagonal = np.diag(self.cosphi_i_plus_one[0 : -2] / (4 * (self.dphi ** 2) * self.cosphi_i[0 : -2]) * self.D_water, k = 2)
        sub_diagonal = np.diag(self.cosphi_i_minus_one[2:] / (4 * (self.dphi ** 2 * self.cosphi_i)[2:]) * self.D_water, k = -2)

        A = (diagonal + sup_diagonal + sub_diagonal) 
        
        # neumann boundary condition by using third order approximation 
        A[self.N-2, self.N-4] = self.D_water * np.cos(self.phi[self.N-1]) / (24 * (self.dphi ** 2) * np.cos(self.phi[self.N-2])) 
        A[1, 3] = self.D_water * np.cos(self.phi[0]) / (24 * (self.dphi ** 2) * np.cos(self.phi[1])) 
        
        A /= self.C_water
        
        return A, b
    
    def explicit_solve(self): 
        """Euler forward step
        """
        for t in tqdm.tqdm(range(1, self.total_it)):
            T_prev = self.T_video[t-1]
            A, b = self.compute_linear_system(T_prev)
            self.T_video[t] = T_prev + (A @ T_prev + b) * self.dt
    
    def backward_solve(self):
        for t in tqdm.tqdm(range(1, self.total_it)):
            T_prev = self.T_video[t-1]
            A, b = self.compute_linear_system(T_prev)
            self.T_video[t] = np.linalg.solve(a=np.eye(self.N) - A*self.dt, b= b*self.dt + T_prev)
            

:::

:::{note} A Note For Fellow Students
:class: dropdown
If you are new to programming, the `class` here just means we are using an abstract object to encapsulate the tiny numerical engine we are using here to solve a problem. The object would collect all necessary compoents like remembering physical constants, storing results etc. It's just a good habbit since by doing so we essentially exposed clean interfaces to users(who want to solve equations). For instance,when we want to run the model with different configurations, we can just modify the dict in the cell above instead of jumping between cells all around the notebook. 

That being said, we are coding up the solver for educational purposes(that's also why AI can replace software engineering but can't replace typing up code by hand, since 
coding itself is a very rewarding learning process), therefore feel free to do whatever you want.
:::

To run the above code, we can use the cell below:

:::{code-cell}python
model_param_back = {
    'N' : 500, 
    'total_it' : int(1e4), 
    'dt' : 1e-3, 
    'T_initial' : 273.15
}

EBM_1d_naive = oneDimensionalEBM(**model_param_back)
EBM_1d_naive.backward_solve()

T_video_naive = EBM_1d_naive.T_video
:::

We can visualize the result by using the following helper function:
:::{code-cell}python
:tag: [hide-input]
def animate1dPDEsolution(solution : np.ndarray, 
                         spatial_discretization,
                         title : str, 
                         output_path : str, 
                         x_unit : str, 
                         y_unit : str, 
                         t_unit : str, 
                         time_factor : int, 
                         fps : int, 
                         coarsen_factor : int =10):
    """plot 1d pde solution

    Args:
        solution : 2D np array, the 0th axis being time, 1th axis being space
        title : the porition of title of the plot that's invariant between frames 
        output_path : where to save the output mp4 to
        time_factor : the ratio between real time and simulation time
        coarsen_factor (int, optional): for speed up, plot once per coarsen_factor

    Returns:
        _type_: _description_
    """
    fig, ax = plt.subplots()
    max = np.max(solution[~np.isnan(solution)])
    min = np.min(solution[~np.isnan(solution)])
    ax.set_ylim(ymin=min)
    ax.set_ylim(ymax=max)
    ax.set_yticks(np.arange(int(min), int(max), 10))
    ax.set_yticklabels(np.arange(int(min), int(max), 10))
    
    total_frames = int(len(solution) / coarsen_factor)
    
    pbar = tqdm.tqdm(total=total_frames)
    
    u = solution[0]
    sol_curr = ax.plot(spatial_discretization, u)[0]
    ax.set(xlabel=f"x {x_unit}", ylabel=f"T {y_unit}", title=f"f1D {title} at Time 0 {t_unit}")
        
    def update(t):
         # sparse plot to speed up
        sol_curr.set_ydata(solution[t * coarsen_factor])
        time = (int)(t * coarsen_factor * time_factor)
        ax.set_title(f"1D {title} at Time {time} {t_unit}")
        pbar.update(1)
        return (sol_curr, )

    anim = animation.FuncAnimation(fig = fig, func=update, frames=total_frames, interval=30)
    anim.save(filename=output_path, fps=fps)

:::

Call the visualization function:
:::{code-cell}python
animate_arg = {
    "solution" : T_video_back[:int(1e3)],
    "spatial_discretization" : EBM_1d_back.phi,
    "output_path" : "output/1dheatebm_naive_backward.mp4", 
    "fps" : 20,
    "x_unit" : "", 
    "y_unit" : "K",
    "time_factor" :0.024,
    "coarsen_factor" : int(1e1), # for speed up, plot once per 10 step
    "title" : "Surface Tempearture Distribution Of Naive 1D EBM", 
    "t_unit" : "hour"
}


animate1dPDEsolution(**animate_arg)
:::

The result:
:::{figure} output/1dheatebm_naive_backward.mp4
:::

We observe that the same problem from iteartion 1 in radiative convevctive modelling emerges. The overall temperature is too cold. We attempt to resolve this following similiar tricks mentioned in the note, that is, adding blankets. Specifically, we proceed with coupled simulation, bookkeeping both $T_{\text{surface}}(t,\phi)$ and $T_{\text{blanket}}(t,\phi)$ for al latitude and update the next $T_{\text{surface}}(t+1,\phi)$ and $T_{\text{blanket}}(t+1,\phi)$ using both groups of subproblems. Recall that the blanket has forcing:

$$
\frac{S_0}{2}|\cos\phi|(1-\alpha) - \sigma T_{\text{blanket}}^4 
$$

and the surface would have:

$$
\frac{S_0}{2}|\cos\phi|(1-\alpha) - \sigma T_{\text{surface}}^4 
$$

[^stiff]: Stiffness means the process we are studying(the 'diffusion' of heat has a small time-scale comparing to the interval which we are simulating(which is like, days?)), mathematically, this means the eigenvalues of the state-transition-matrix has very different magnitudes.
[^fdb]: Indeed, the best thing about finite difference is the ease of implementation, without too much struggle a beginner like me can code up a solution that won't be too much worse than a commercial package for such simple problems. 
[^pe]: Parabolic equations descirebes *time-dependent* physical process that evolves towward a *steady-state*