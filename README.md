# Alcohol_Mixture_ML
This project has been a significant part of my undergraduate computational chemistry research. 
I utilize high-performance-computing and Python code/scikit-learn in order to train several models that can predict the 
concentration of a three component mixture based on a given IR spectrum. 

I used many tools to accomplish this task. First, I used Wolfram Mathematica to generate three mole fractions for each of 1000 mixtures corresponding to 
theoretical water, methanol, and ethanol concentrations. This task of randomness was not as easy as it sounds! I actually generated a 
tetrahedron with side lengths 1 and sampled this shape randomly to achieve truly random results. Then, I exported a CSV of these random concentrations into my account
on Clemson's Palmetto supercluster. From here, I carried out calculations using Gaussian software for pure water, methanol, and ethanol to extract vibrational modes and convert them to IR spectra. Initially, to accomplish this I applied a distribution function to my calculated vibrational modes to acquire pure IR spectral functino. Then, I took the dot product of a matrix containing spectral points from 1000 to 4000 nm and a matrix containing my randomly sampled concentrations. Lastly, I added/subtracted random values in a given range to each data point to simulate IR noise. This method is very similar to that of Angulo et al.

To enhance the thorougness of our models and research, we introduced the effect of solvent through a polarizable continuum model. I specified dielectric constants for water, ethanol, and methanol and multiplied them by the concentrations of each respective mixture.

Finally, after obtaining vibrational frequency calculations for every mixture, I exported these values into a Jupyter notebook. I wrote several 
functions that turn frequencies and energies into neat spectra, like the spectra that can be gathered manually with a spectrophotometer in a lab
except these are all simulated! With the points of these simulated spectra, I created a numpy array of dimensions 3000 x 1000. Each point is a 
"feature" in my model. I simulate noise using a function that adds a noise factor to each data point that is a random value between -0.05 and +0.05.

I was able to train three models (Linear Regression (RIDGE), Decision Tree, and Random Forest that all boast predictive accuracy of over 90%. 
Random Forest performs the best of these with a consistent accuracy around 98%!

This is not a perfect project, and I already have ideas for refinement (only training a model based on points where I know a peak may be present,
optimizing hyperparameters, and gathering spectra in a more thorough way). But I am pleased with the result and my lab group will be continuing the study
of mixture prediction. Our next steps involve refinement of the code in this repo and automating real-world data collection with a liquid handler we built. We repurposed an Ender 3 3D printer into a liquid handler similar to Saggiomo et al. which we are rigging to automate data collection and to apply machine learning with mixtures to other mixtures and experiments. 

This repository contains the Jupyter notebook of my Python code, the CSV of concentrations created in Mathematica, the pure molecular geometry
of water, ethanol, and methanol. The data regarding all 3000 calculated data points is available upon request.
