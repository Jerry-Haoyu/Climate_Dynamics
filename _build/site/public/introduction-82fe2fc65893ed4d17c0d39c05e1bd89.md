# Climate Dynamics 

---

:::{figure} _static/site_logo_light.png
:width: 200%
Cover Figure [^tf]
:::
---
## Introduction 


This is a student's lecture note for **ATMS 507 Climate Dynamics, UIUC** taught by Professor [Gan Zhang](https://climatezhang.web.illinois.edu/). The course is composed of three parts 
1. History Of Climate Modelling 
2. Qualitative Modelling 
3. Quantitative Modelling 
   
**This note is primarily going to focus on quantitative modelling**. 



:::{tip} Main Features
The note features \
    1. Detailed derivation that is relevant but too trivial to be covered in a graduate-level climate system  \
    2. Solving important PDEs arising from classical climate models from scratch(using only *numpy*) (ex. solving energy balance model to simulate surface temperature on an aqua-planet)
    3. Custom **visualization package** *ClimaVis* downloadable from PyPI, easy to use for educational purposes
:::

The note features runnable code snippets. To actually run the code, click the *power button* located at the top right of the page, the binder service will then spawn a docker container shortly afterward(might need to wait for ~1m). After the docker container is built, a run buttom would appear above every code box. 


## Purpose and Target Audience
This note is primarily for my own learning. However, I plan to share it with my fellow students and hopefully future students who will be taking this class hence I do hope this turn out to be of some quality.  

:::{error} Mistakes Everywhere
This is just a lecture note by a student who is a total beginer in climate science, and not too much better in Mathematics and CS(A lot to learn!). Also as a second-language speaker in English[^fl], typos and mistakes in spelling is somewhat unavoidable.

Therefore mistakes should be expected among every rendered equation/sentence. I would greatly appreciate reporting mistakes via `github` or my email `hytang2@illinois.edu`. 
:::

## AI-Free Disclaimer
I'm a believer of the idea that AI brings huge cognitive debt and cumbers the learning process. This notebook is hence created AI free(however, conceptual consulting is quite frequent, they are truely valuable resource too when it comes to learning, contradictoraily). In particular, code snippets is absolutely AI-free.

[^fl]: My mother tongue is [**Wu Chinese(ISO639-3 : wuu)**](https://zh.wikipedia.org/zh-tw/%E8%AF%B8%E6%9A%A8%E8%AF%9D)(**枫桥话**-吴语临绍小片) and **Madarin**(**普通话**)

[^tf]: The figure, which I created in pages, aims to represent a GCM. I'm trying to do some data-driven appraoch to come up with a toy GCM, supervised by Professor Gan. However things are just starting and the project is likely too ambitious. 