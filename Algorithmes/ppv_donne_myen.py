import numpy as np
import time
import csv

# Fonction distance entre deux points
def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Fonction pour lire les données d'un fichier CSV
def read_csv_data(filename):
    villes = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Ignorer l'en-tête (assumer que la première ligne contient les noms de colonne)
        next(reader)
        for row in reader:
            # Convertir chaque valeur en float
            villes.append((float(row[0]), float(row[1])))
    return villes

# Algorithme du plus proche voisin (APN)
def apn(villes):
    tournee = []
    distance_totale = 0
    ville_actuelle = villes[0]

    start_time = time.time()

    for _ in range(len(villes) - 1):
        ville_prochaine = min((distance(ville_actuelle, ville), ville) for ville in villes if ville not in tournee)
        tournee.append(ville_prochaine[1])
        distance_totale += ville_prochaine[0]
        ville_actuelle = ville_prochaine[1]

    tournee.append(villes[0])
    distance_totale += distance(ville_actuelle, villes[0])

    end_time = time.time()
    execution_time = end_time - start_time

    return tournee, distance_totale, execution_time

# Exemple d'utilisation (modifier le nom du fichier si nécessaire)
villes = read_csv_data('villes_taille_grande.csv')
tournee, distance_totale, execution_time = apn(villes)

print("Tournée :", tournee)
# print("Distance totale :", distance_totale)
print("Temps d'exécution :", execution_time, "secondes")
