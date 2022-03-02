# %% [markdown]
# # Distance Images
# 
# These illustrate a few of the distance computations used for k-NN algorithm.

# %%
import matplotlib.pyplot as plt
from math import hypot

# %% [markdown]
# ## Euclidean

# %%
plt.figure("Euclidean", (5, 5))
plt.set_cmap('gray')

plt.axis((6, 10, 6, 10))
plt.xticks((6, 7, 8, 9, 10))
plt.yticks((6, 7, 8, 9, 10))
plt.grid(axis='both')
plt.scatter((7, 8), (8, 9), marker="o", label="??", color='0.0')

plt.annotate('(7, 8)', xy=(7, 8), xytext=(7, 7.8))
plt.annotate('(8, 9)', xy=(8, 9), xytext=(8, 8.8))

plt.annotate("", xy=(8, 9), xytext=(7, 8), arrowprops=dict(width=2.5, shrink=.1, color='black'))
plt.text(7, 8.5, "Euclidean = 1.4", bbox=dict(boxstyle='square', fc='white', ec='white', pad=0.2), color='black')
plt.show()

# %% [markdown]
# ## Manhattan

# %%
plt.figure("Manhattan", (5, 5))
plt.set_cmap('gray')

plt.axis((6, 10, 6, 10))
plt.xticks((6, 7, 8, 9, 10))
plt.yticks((6, 7, 8, 9, 10))
plt.grid(axis='both')
plt.scatter((7, 8), (8, 9), marker="o", label="??", color='0.0')

plt.annotate('(7, 8)', xy=(7, 8), xytext=(7, 7.8))
plt.annotate('(8, 9)', xy=(8, 9), xytext=(8, 8.8))

plt.annotate("", xy=(7, 9), xytext=(7, 8), arrowprops=dict(width=2.5, shrink=.1, color='black'))
plt.annotate("", xy=(8, 9), xytext=(7, 9), arrowprops=dict(width=2.5, shrink=.1, color='black'))

plt.text(7, 8.5, "Manhattan = 2.0", bbox=dict(boxstyle='square', fc='white', ec='white', pad=0.2), color='black')
plt.show()

# %% [markdown]
# ## Chebyshev

# %%
plt.figure("Chebyshev", (5, 5))
plt.set_cmap('gray')

plt.axis((6, 10, 6, 10))
plt.xticks((6, 7, 8, 9, 10))
plt.yticks((6, 7, 8, 9, 10))
plt.grid(axis='both')
plt.scatter((7, 8), (8, 9), marker="o", label="??", color='0.0')

plt.annotate('(7, 8)', xy=(7, 8), xytext=(7, 7.8))
plt.annotate('(8, 9)', xy=(8, 9), xytext=(8, 8.8))

plt.annotate("", xy=(8, 9), xytext=(7, 8), arrowprops=dict(width=2.5, shrink=.1, color='black'))
plt.text(7, 8.5, "Chebyshev = 1.0", bbox=dict(boxstyle='square', fc='white', ec='white', pad=0.2), color='black')
plt.show()

# %% [markdown]
# ## Sorensen

# %%
plt.figure("Sorensen", (5, 5))
plt.set_cmap('gray')

plt.axis((0, 10, 0, 10))
plt.xticks(list(range(11)))
plt.yticks(list(range(11)))
plt.grid(axis='both')
plt.scatter((6, 8), (7, 9), marker="o", label="??", color='0.0')

plt.annotate('(6, 7)', xy=(6, 7), xytext=(6, 6.8), va='top')
plt.annotate('(8, 9)', xy=(8, 9), xytext=(8, 8.8), va='top')

plt.annotate("", xy=(6, 9), xytext=(6, 7), arrowprops=dict(width=2.5, shrink=.1, color='black'))
plt.annotate("", xy=(8, 9), xytext=(6, 9), arrowprops=dict(width=2.5, shrink=.1, color='black'))

plt.text(4.5, 5.6, "Manhattan = 4\nSorensen = (2+2)/(14+16)", bbox=dict(boxstyle='square', fc='white', ec='white', pad=0.2), color='black')
plt.show()

# %%



