import numpy as np
from numpy.linalg import det
from scipy.stats import dirichlet
from scipy.spatial import ConvexHull, Delaunay
import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


#Function to prepare uniformly distributed points in given n-dimensional convex hull
#Credit to Daniel F on StackOverflow for the function idea/sample code!
def generate_points(points, n, n_components):
    dimension = points.shape[-1]
    c_hull = points[ConvexHull(points).vertices]
    delaunay_sim = c_hull[Delaunay(c_hull).simplices]

    sim_vols = np.abs(det(delaunay_sim[:, :dimension, :] - delaunay_sim[:, dimension:, :])) / np.math.factorial(dimension)
    r_sample = np.random.choice(len(sim_vols), size=n, p=sim_vols / sim_vols.sum())

    return np.einsum('ijk, ij -> ik', delaunay_sim[r_sample], dirichlet.rvs([1]*(dimension + 1), size=n))
        

#Main to generate the points
if __name__ == '__main__':
    #Get points
    p_bounds = np.array([
        [1, 0],
        [0, 1],
        [0, 0]
    ])
    p_list = generate_points(p_bounds, 100, 3)
    
    #Concentration dataframe
    p_frame = pd.DataFrame(p_list, columns=['Water_mFrac', 'Methanol_mFrac'])
    p_frame['Ethanol_mFrac'] = 1 - p_frame['Water_mFrac'] - p_frame['Methanol_mFrac']

    print(p_frame.head())
        
    #Plot points with Seaborn and Matplotlib
    sns.set_style(style = 'darkgrid')

    figure = plt.figure()
    axes = plt.subplot(111, projection = '3d')

    x_ax = p_frame['Water_mFrac']
    y_ax = p_frame['Methanol_mFrac']
    z_ax = p_frame['Ethanol_mFrac']

    axes.set_xlabel('Water Mole Fraction')
    axes.set_ylabel('Methanol Mole Fraction')
    axes.set_zlabel('Ethanol Mole Fraction')

    #Create and show plot
    axes.scatter(x_ax, y_ax, z_ax)
    plt.show()