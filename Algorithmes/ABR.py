import time
import random

class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

def inserer(racine, valeur):
    if racine is None:return Noeud(valeur)
    if valeur < racine.valeur:racine.gauche = inserer(racine.gauche, valeur)
    else:racine.droite = inserer(racine.droite, valeur)
    return racine

def rechercher(racine, clé):
    if racine is None or racine.valeur == clé:return racine
    if clé < racine.valeur:return rechercher(racine.gauche, clé)
    return rechercher(racine.droite, clé)

def generer_ABR(taille):
    valeurs = random.sample(range(1, taille * 10), taille)
    racine = None
    for valeur in valeurs:
        racine = inserer(racine, valeur)
    return racine, valeurs

def mesurer_temps_recherche(racine, clés):
    temps_total = 0
    for clé in clés:
        start_time = time.time()
        rechercher(racine, clé)
        end_time = time.time()
        temps_total += end_time - start_time
    return temps_total / len(clés)

# Génération et recherche dans un ABR de petite taille (10 nœuds)
racine_petite, valeurs_petite = generer_ABR(10)
clés_petite = random.sample(valeurs_petite, 5)
print("Recherche dans un ABR de petite taille (10 nœuds) :")
temps_petite = mesurer_temps_recherche(racine_petite, clés_petite)
print(f"Temps de recherche moyen : {temps_petite:.20f} secondes\n")

# Génération et recherche dans un ABR de taille moyenne (5000 nœuds)
racine_moyenne, valeurs_moyenne = generer_ABR(5000)
clés_moyenne = random.sample(valeurs_moyenne, 900)
print("Recherche dans un ABR de taille moyenne (5000 nœuds) :")
temps_moyenne = mesurer_temps_recherche(racine_moyenne, clés_moyenne)
print(f"Temps de recherche moyen : {temps_moyenne:.20f} secondes\n")

# Génération et recherche dans un ABR de grande taille (59000 nœuds)
racine_grande, valeurs_grande = generer_ABR(59000)
clés_grande = random.sample(valeurs_grande, 800)
print("Recherche dans un ABR de grande taille (59000 nœuds) :")
temps_grande = mesurer_temps_recherche(racine_grande, clés_grande)
print(f"Temps de recherche moyen : {temps_grande:.20f} secondes\n")
