# Solution Tâche 2: espérance et variance.

# Exécutez les cellules de ce fichier Python ou 
# copiez-les et collez-les dans les cellules 
# d'un Notebook.
# %%
import numpy as np
# a. paramètres
sigma = 3.14
omega = 2
N = 10000
np.random.seed(1986)

# %%
# b. tirage aléatoire
x = np.random.normal(loc=0, scale=sigma, size=N)

# %%
# c. fonction g(.)

def g(x, omega):
    y = x.copy()
    y[x < -omega] = -omega
    y[x > omega] = omega
    return y

# %%
# d. moyenne et variance
mean = np.mean(g(x, omega))
var = np.var(g(x-mean, omega))
print(f'mean = {mean:.5f}, var = {var:.5f}')

# %%
