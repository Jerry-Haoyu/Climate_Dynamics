# Radiative Convective Model 
Radiative convective model captures radiation from the sun and vertical convection within the atomsphere. This is a well-known work by the pioneering climate scientist **Syukuro Manabe**[^sm], 

> This is a classic example of **iterative development** of geophysical mathematical model which sound quite familiar from CS classes. The idea is to capture the main idea by the simplest model, then identify disagreement with reality. The anomalies comes from the lack of expressivity of the minimal model hence we iteratively refine the model by adding more structure and details. We hault when we reach a satisfactory modeling accuracy.

## Iteration 1: Earth as a Black Body
The sun emit its energy from nuclear fusion via radiation. The total luminosity is $L_0 = 3.9 \times 10^{26} \mathrm{Js^{-1}}$. At distance $d$ from the sun, the flux density is:
$$
S_0(d)= \frac{L_0}{4\pi d^2}
$$
Now a
:::{note} Earth as a Black Body
Suppose earth is a perfect black body, then we 
:::


[^sm]: Syukuro Manabe is one of the first climate scientist who sucessfully modelled the climate system using computer-aided numerical simulation. He is one of the 2021 Nobel Physics Winner due to his work in climate modelling. **A fun fact of this grand master from Professor Gan** : he is one of the climate scientist who was rigorously educated  at University of Tokyo, however, who chose to immigrate to the U.S after WWII. I felt this fact to be vastly interesting and relevant under the current geopolitial context for controversial reasons. Here is a link to a socioeconomic study [Exodus of Meoeorolgists from University of Tokyo](https://journals.ametsoc.org/view/journals/bams/74/7/1520-0477_1993_074_1351_mftuot_2_0_co_2.xml).