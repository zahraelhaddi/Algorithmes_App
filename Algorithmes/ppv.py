import numpy as np
import time

# Données des villes (coordonnées x, y)
villes = [(1, 2), (3, 4), (2, 5), (4, 3), (5, 1)]

# Fonction distance entre deux points
def distance(point1, point2):
  return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Initialisation
tournee = []
distance_totale = 0
ville_actuelle = villes[0]

# Début du chronomètre
start_time = time.time()

# Algorithme du plus proche voisin
for _ in range(len(villes) - 1):
  ville_prochaine = min((distance(ville_actuelle, ville), ville) for ville in villes if ville not in tournee)
  tournee.append(ville_prochaine[1])
  distance_totale += ville_prochaine[0]
  ville_actuelle = ville_prochaine[1]

# Retourner au point de départ
tournee.append(villes[0])
distance_totale += distance(ville_actuelle, villes[0])

# Fin du chronomètre
end_time = time.time()

# Calcul du temps d'exécution
execution_time = end_time - start_time

# Affichage de la tournée, de la distance totale et du temps d'exécution
print("Tournée :", tournee)
print("Distance totale :", distance_totale)
print("Temps d'exécution :", execution_time, "secondes")
