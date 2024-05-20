import csv
import random

# Nombre de villes à générer
nombre_villes = 5000  # Vous pouvez modifier ce nombre selon vos besoins

# Plage des coordonnées x et y
min_x = 0
max_x = 50
min_y = 0
max_y = 50

# Initialiser la liste des villes
villes = []

# Générer des villes aléatoires
for _ in range(nombre_villes):
    x = random.uniform(min_x, max_x)
    y = random.uniform(min_y, max_y)
    villes.append((x, y))

# Ouvrir le fichier CSV en mode écriture
with open('villes_taille_grande.csv', 'w', newline='') as csvfile:
    # Créer un objet écrivain CSV
    writer = csv.writer(csvfile)

    # Écrire l'en-tête
    writer.writerow(['X', 'Y'])

    # Écrire les données de chaque ville
    for ville in villes:
        writer.writerow([ville[0], ville[1]])

print(f"{nombre_villes} villes générées et enregistrées dans 'villes_taille_grande.csv'")
