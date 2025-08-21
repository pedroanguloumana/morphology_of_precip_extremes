import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def discrete_cmap(cmap_name="viridis", N=5):
    """
    Return a discrete version of a continuous colormap.

    Parameters
    ----------
    cmap_name : str or Colormap
        Name of the Matplotlib colormap (e.g. 'viridis') 
        or a Colormap object.
    N : int
        Number of discrete intervals.

    Returns
    -------
    ListedColormap
        Discrete colormap with N bins.
    """
    # Get the base colormap (handles both string and Colormap input)
    cmap = plt.get_cmap(cmap_name)
    
    # Sample N colors spaced evenly across the colormap
    colors = cmap(np.linspace(0, 1, N))
    
    # Build a new ListedColormap
    return ListedColormap(colors, name=f"{cmap_name}_{N}")