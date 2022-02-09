import numpy as np
from scipy import optimize

class consommateur:
    
    def __init__(self,**kwargs): # appel lors de la création
        
        # a. paramètres de base
        self.alpha = 0.5
        
        self.p1 = 1
        self.p2 = 2
        self.R = 10
        
        self.q1 = np.nan # ce n'est pas un nombre
        self.q2 = np.nan
        
        # b. réglages de base
        self.q2_max = 10
        self.n = 100
            
        # c. mise à jour des paramètres et réglages
        for key, value in kwargs.items():
            setattr(self,key,value) # comme self.key = valeur
        
         # remarque: "kwargs" est un dictionnaire à mot-clés
            
    def __str__(self): # appel lors de l'affichage
        
        lines = f'alpha = {self.alpha:.3f}\n'
        lines += f'vecteur de prix = (p1,p2) = ({self.p1:.3f},{self.p2:.3f})\n'
        lines += f'revenu = R = {self.R:.3f}\n'

        # ajout de lignes sur la solution si elle a été calculée
        if not (np.isnan(self.q1) or np.isnan(self.q2)):
            lines += 'solution:\n'
            lines += f' q1 = {self.q1:.2f}\n'
            lines += f' q2 = {self.q2:.2f}\n'
               
        return lines

        # remarque: \n donne un saut de ligne

    # fonction d'utilité
    def utilite(self,q1,q2):
        return q1**self.alpha*q2**(1-self.alpha)
    
    # solution du problème
    def solve(self):
        
        # a. fonction objectif(à minimiser) 
        def valeur_du_choix(q):
            return -self.utilite(q[0],q[1])
        
        # b. contraintes
        contraintes = ({'type': 'ineq', 'fun': lambda q: self.R-self.p1*q[0]-self.p2*q[1]})
        bornes = ((0,self.R/self.p1),(0,self.R/self.p2))
        
        # c. appel du solveur
        valeurs_initiales = [self.R/self.p1/2,self.R/self.p2/2]
        sol = optimize.minimize(valeur_du_choix,valeurs_initiales,
                                method='SLSQP',bounds=bornes,constraints=contraintes)
        
        # d. sauvegarde
        self.q1 = sol.x[0]
        self.q2 = sol.x[1]
        self.u = self.utilite(self.q1,self.q2)
 
    # courbes d'indifférence
    def courbe_indifference(self):
        
        # affectation de mémoire
        self.q1_vecs = []
        self.q2_vecs = []
        self.us = []
        
        for fac in [0.5,1,1.5]:
            
            # fac = 1 -> courbe d'indifférence traversant optimum
            # fac < 1 -> ... au-dessous l'optimum
            # fac > 1 -> ... au-dessus de l'optimum
                
            # a. utilité en (fac*q1,fac*q2)
            u = self.utilite(fac*self.q1,fac*self.q2)
            
            # b. affectation d'arrays
            q1_vec = np.empty(self.n)
            q2_vec = np.linspace(1e-8,self.q2_max,self.n)

            # c. boucle sur q2 et calcul de q1
            for i,q2 in enumerate(q2_vec):

                # fonction locale donnant la valeur de u et q2
                def objectif(q1):
                    return self.utilite(q1,q2)-u
            
                sol = optimize.root(objectif, 0)
                q1_vec[i] = sol.x[0]
            
            # d. sauvegarde
            self.q1_vecs.append(q1_vec)
            self.q2_vecs.append(q2_vec)
            self.us.append(u)
    
    # graph de l'ensemble de budget
    def plot_budgetset(self,ax):
        
        x = [0,0,self.R/self.p1] # cordonnées x dans un triangle
        y = [0,self.R/self.p2,0] # cordonnées x dans un triangle
        
        # remplissage du triangle
        ax.fill(x,y,color="firebrick",lw=2,alpha=0.5) # alpha contrôle la transparence
        
    # graph de la solution
    def plot_solution(self,ax):
        
        ax.plot(self.q1,self.q2,'ro',color='black') # a black dot
        ax.text(self.q1*1.03,self.q2*1.03,f'$u^{{max}} = {self.u:.2f}$')
        
    # graph des courbes d'indifférence
    def graph_courbe_indifference(self,ax):
        
        for q1_vec,q2_vec,u in zip(self.q1_vecs,self.q2_vecs,self.us):
            ax.plot(q1_vec,q2_vec,label=f'$u = {u:.2f}$')
    
    # détails pour le graph (labels,limites,grille,légende)
    def plot_details(self,ax):

        ax.set_xlabel('$q_1$')
        ax.set_ylabel('$q_2$')
                
        ax.set_xlim([0,self.q2_max])
        ax.set_ylim([0,self.q2_max])

        ax.grid(ls='--',lw=1)
        ax.legend(loc='droite sup')
