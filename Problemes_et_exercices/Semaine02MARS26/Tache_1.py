# Solution Tâche 1: Nombres aléatoires.

# Exécutez les cellules de ce fichier Python ou 
# copiez-les et collez-les dans les cellules 
# d'un Notebook.
# %%
import numpy as np
np.random.seed(1986)
state = np.random.get_state()
for i in range(3):
    np.random.set_state(state)
    for j in range(2):
        x = np.random.uniform()
        print(f'({i},{j}): x = {x:.3f}')
# %%
