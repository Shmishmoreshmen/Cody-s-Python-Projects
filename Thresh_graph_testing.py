#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Generate some sample data
x = np.random.normal(size=1000)
y = np.random.normal(size=1000)

# Compute KDE with different bandwidths
bandwidths = [0.1, 0.5, 1.0]  # Adjust bandwidth values as needed
kdes = [gaussian_kde([x, y], bw_method=bw) for bw in bandwidths]

# Plot KDE heat maps with different bandwidths
fig, axs = plt.subplots(1, len(bandwidths), figsize=(15, 5))
for i, (bw, kde) in enumerate(zip(bandwidths, kdes)):
    xx, yy = np.mgrid[min(x):max(x):100j, min(y):max(y):100j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    density = np.reshape(kde(positions).T, xx.shape)
    
    axs[i].imshow(density, cmap='inferno', extent=(min(x), max(x), min(y), max(y)))
    axs[i].set_title(f'Bandwidth = {bw}')
    axs[i].set_xlabel('X')
    axs[i].set_ylabel('Y')

#plt.tight_layout()
plt.show()


# In[ ]:


from scipy.stats import gaussian_kde

# Example data
data = [1, 2, 3, 4, 5]

# Create KDE using Scott's method
kde_scott = gaussian_kde(data, bw_method='scott')

# Create KDE using Silverman's method
kde_silverman = gaussian_kde(data, bw_method='silverman')

# Create KDE with a specified bandwidth
kde_custom = gaussian_kde(data, bw_method=0.5)


# In[ ]:




