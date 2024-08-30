import numpy as np
import numpy.random as npr
import pandas as pd
import matplotlib.pyplot as plt

class MyBrownian:
    def __init__(self, times, N):
        self.times = np.array(times)  #Liste des temps
        self.N = N  #Nombre de scénarios
        self.B = None  #Brownien
        self.df = None  #DataFrame du brownien

    def SimulBrownian(self):
        n = len(self.times)  #Nombre de pas de temps (longueur de la liste)
        self.B = np.zeros((n, self.N)) #Creation de la matrice de Brownien
        dt = np.diff(self.times, prepend=0)  #Calcul des différences de temps (entre deux valeurs de la liste)

        for j in range(self.N):
            for i in range(1, n):  #Valeurs de 1 à n-1
                self.B[i, j] = self.B[i-1, j] + np.sqrt(dt[i]) * npr.randn()
        self.df = pd.DataFrame(self.B,
                               index=self.times)
        print(self.df)

    def GraphTraj(self):
        if self.df is None:
            print("Lancer la premiere methode.")
            return

        plt.figure(figsize=(10, 6))
        for j in range(self.N):
            plt.plot(self.df.index, self.df[j])
        plt.title('Trajectoires de mouvements Browniens')
        plt.xlabel('Time')
        plt.ylabel('Position')
        plt.show()

#Exemple d utilitsation (avec donnees de pas de temps du SWAP sur VBA)
times = [1, 2, 3, 4.002740, 5.002740, 6.002740, 7.002740, 8.005479, 9.005479, 10.005479, 
         11.005479, 12.008219, 13.008219, 14.008219, 15.008219, 16.010959, 17.010959, 
         18.010959, 19.010959, 20.013699, 21.013699, 22.013699, 23.013699, 24.016438, 
         25.016438, 26.016438, 27.016438, 28.019178, 29.019178]

brownian = MyBrownian(times=times, N=500)
brownian.SimulBrownian()
brownian.GraphTraj()

