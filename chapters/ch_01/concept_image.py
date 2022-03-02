# %% [markdown]
# # Conceptual Overview
# 
# This paints a picture showing the k-NN concept.
# 
# An unknown sample, shown as a ◆ is surrounded by two groups of known items, shown as ⚫︎ and ◼︎.
# 
# In this example, we're using the Euclidean distance between points, computed by `math.hypot`. There are 3 neighbors within a distance of 2.0. Among these, two are ⚫︎, and one is ◼︎. For a k-value of 3, the most common neighbor is ⚫︎.
# 
# If we switch to k-value of 5, we dicover 3 ◼︎ and 2 ⚫︎, flipping the outcome.
# 
# This situation is relatively rare and requires an unknown sample to be carefully perched almost midway between two populations.


# %%
# Imports
import matplotlib.pyplot as plt
import matplotlib.path
from matplotlib.patches import Circle

# %%
sample = (5, 5)
circles = [(2, 8), (4, 6), (5, 7)]
squares = [(4, 2), (6, 2), (6, 4)]
fig, ax = plt.subplots()
plt.set_cmap('gray')

plt.axis('equal')
plt.scatter(*sample, marker="D", label="??", color='0.0')
plt.scatter([x for x, y in circles], [y for x, y in circles], marker="o", color='.20')
plt.scatter([x for x, y in squares], [y for x, y in squares], marker="s", color='.33')

# k = 3 nearest neighbors
circle3 = Circle((5, 5), 2, facecolor='none',
                edgecolor='black', linestyle='--', alpha=0.8)
ax.add_patch(circle3)
plt.ylim(0, 10)
plt.ylim(0, 10)
# k = 5 nearest neighbors
circle5 = Circle((5, 5), 3.2, facecolor='none',
                edgecolor='black', linestyle=':', alpha=1.0)
ax.add_patch(circle5)

plt.grid(True)


# %%


# %%
import math
sorted(math.hypot((sample[0]-t[0]), (sample[1]-t[1])) for t in circles+squares)

# %%



