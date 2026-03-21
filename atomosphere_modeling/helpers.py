import numpy as np 
from IPython.display import display, Math
import sympy as sp
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

def shift_numpy_array(array : np.ndarray, step : int):
    if(step > 0): #shift right
        array = np.pad(array[0 : len(array)-step], pad_width=(step, 0), constant_values=0)
    elif(step < 0): #shift left
        step = -step
        array = np.pad(array[step : len(array)], pad_width=(0, step), constant_values=0)
    return array 

def latex_print(A):
    display(Math(sp.latex(sp.Matrix(A.tolist()))))
    
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
    
    u = solution[0]
    sol_curr = ax.plot(spatial_discretization, u)[0]
    ax.set(xlabel=f"x {x_unit}", ylabel=f"T {y_unit}", title=f"f1D {title} at Time 0 {t_unit}")
        
    def update(t):
         # sparse plot to speed up
        sol_curr.set_ydata(solution[t * coarsen_factor])
        time = (int)(t * coarsen_factor * time_factor)
        ax.set_title(f"1D {title} at Time {time} {t_unit}")
        return (sol_curr, )

    anim = animation.FuncAnimation(fig = fig, func=update, frames=int(len(solution) / coarsen_factor), interval=30)
    anim.save(filename=output_path, fps=fps)

   