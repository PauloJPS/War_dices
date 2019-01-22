import numpy as np
import matplotlib.pyplot as plt
import time

# Monte Carlo to roll dice

class War_battle:
    def __init__(self, atack, defense):
        self.atk = atack
        self.df = defense

    def roll(self, n):
        return np.random.randint(1,7, n)

    def round(self, aux_atk, aux_df):
        atk_dices, def_dices = self.n_dices(aux_atk, aux_df)
        red = -np.sort(-self.roll(atk_dices))
        yellow = -np.sort(-self.roll(def_dices))

        results = []
        for i, j in zip(red, yellow):
            results.append(j>=i)
        return results

    def n_dices(self, atk, df):
        if atk == 0:
            print(oi)
        if df == 0:
            print(oi)

        if atk >=3:
            n_atk = 3
        else:
            n_atk = atk
        if df >=3:
            n_df = 3
        else:
            n_df = df
        return n_atk, n_df

    def simulation(self, n_int):
        attacker = 0
        defender = 0
        sigma_attacker = 0
        sigma_defender = 0
        for it in range(n_int):
            aux_atk = self.atk
            aux_df = self.df
            while(aux_atk !=0 and aux_df !=0):
                result = self.round(aux_atk, aux_df)
                for i in result:
                    if i==True:
                        aux_atk += -1
                    else:
                        aux_df += -1
            if aux_atk > aux_df:
                attacker += 1
            else:
                defender += 1
        attacker = attacker/n_int
        defender = defender/n_int
        sigma_attacker = np.sqrt((1. - attacker)/n_int)
        sigma_defender = np.sqrt((1. - defender)/n_int)
        return attacker, sigma_attacker, defender, sigma_defender

    @staticmethod
    def probability_surface(n=20, precision=0.1):
        N = int((1/precision)**2)
        print(N)
        attackers = [i for i in range(1, n+1)]
        defenders = [i for i in range(1, n+1)]

        p_mat = np.zeros((n,n))

        for at in attackers:
            for df in defenders:
                a = War_battle(at, df)
                results = a.simulation(N)
                p_mat[at-1][-(df)] = results[0]
            print(at)

        fig, ax = plt.subplots()
        mat_plot = ax.matshow(p_mat.T, interpolation='nearest')
        cbar = plt.colorbar(mat_plot)
        cbar.set_label('probability of the attack winning', fontsize=15)
        ax.set_ylabel('nº defenders', fontsize=15)
        ax.set_xlabel('nº attackers', fontsize=15)
        
        ax.set_xticks(range(1, n+1, 2))
        ax.set_xticklabels([str(i) for i in range(1, n+1, 2)])
        ax.set_yticks(range(1, n+1, 2))
        ax.set_yticklabels([str(i) for i in np.arange(n-1, -1, -2)])
        

        plt.grid(True)
        plt.tight_layout()
        plt.savefig('war.jpg', format='jpg')

        return p_mat



                
                    
                 
                
                



            




