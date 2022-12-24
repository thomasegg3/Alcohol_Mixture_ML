import numpy as np
from numpy.linalg import det
from scipy.stats import dirichlet
from scipy.spatial import ConvexHull, Delaunay

#Function to prepare uniformly distributed points in given n-dimensional convex hull
def generate_points(points, n):
    dimension = points.shape[-1]
    c_hull = points[ConvexHull(points).vertices]
    delaunay_sim = c_hull[Delaunay(c_hull).simplices]

    sim_vols = np.abs(det(delaunay_sim[:, :dimension, :] - delaunay_sim[:, dimension:, :])) / np.math.factorial(dimension)
    r_sample = np.random.choice(len(sim_vols), size=n, p=sim_vols / sim_vols.sum())

    return np.einsum('ijk','ij -> ik', delaunay_sim[r_sample], dirichlet.rvs([1]*(dimension + 1), size=n))