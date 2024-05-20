import random
import time

class ObjetSac:
    def __init__(self, poids, valeur):
        self.poids = poids
        self.valeur = valeur
        self.ratio = valeur / poids

class Noeud:
    def __init__(self, niveau, valeur, poids, borne):
        self.niveau = niveau
        self.valeur = valeur
        self.poids = poids
        self.borne = borne

def borne(noeud, n, W, objets):
    if noeud.poids >= W:
        return 0

    profit_borne = noeud.valeur
    j = noeud.niveau + 1
    poids_total = noeud.poids

    while (j < n and poids_total + objets[j].poids <= W):
        poids_total += objets[j].poids
        profit_borne += objets[j].valeur
        j += 1

    if (j < n):
        profit_borne += (W - poids_total) * objets[j].ratio

    return profit_borne

def sac_a_dos(W, objets, n):
    objets.sort(key=lambda x: x.ratio, reverse=True)
    Q = []
    u = Noeud(-1, 0, 0, 0)
    v = Noeud(-1, 0, 0, 0)
    Q.append(u)
    profitMax = 0

    while Q:
        u = Q.pop(0)

        if u.niveau == -1:
            v.niveau = 0

        if u.niveau == n-1:
            continue

        v.niveau = u.niveau + 1
        v.poids = u.poids + objets[v.niveau].poids
        v.valeur = u.valeur + objets[v.niveau].valeur

        if v.poids <= W and v.valeur > profitMax:
            profitMax = v.valeur

        v.borne = borne(v, n, W, objets)

        if v.borne > profitMax:
            Q.append(Noeud(v.niveau, v.valeur, v.poids, v.borne))

        v.poids = u.poids
        v.valeur = u.valeur
        v.borne = borne(v, n, W, objets)

        if v.borne > profitMax:
            Q.append(Noeud(v.niveau, v.valeur, v.poids, v.borne))

    return profitMax

if __name__ == "__main__":
    # Génération de données de petite taille
    poids_petit = [random.randint(1, 10) for _ in range(5)]
    valeurs_petit = [random.randint(1, 10) for _ in range(5)]
    W_petit = random.randint(10, 20)
    n_petit = len(poids_petit)
    objets_petit = [ObjetSac(poids_petit[i], valeurs_petit[i]) for i in range(n_petit)]
    debut_petit = time.time()
    profitMax_petit = sac_a_dos(W_petit, objets_petit, n_petit)
    fin_petit = time.time()
    temps_petit = fin_petit - debut_petit
    print("Données de petite taille :")
    print(f"Le profit maximum est : {profitMax_petit}")
    print(f"Temps d'exécution : {temps_petit:.10f} secondes")

    # Génération de données de taille moyenne
    poids_moyen = [random.randint(1, 20) for _ in range(20)]
    valeurs_moyen = [random.randint(1, 20) for _ in range(20)]
    W_moyen = random.randint(20, 50)
    n_moyen = len(poids_moyen)
    objets_moyen = [ObjetSac(poids_moyen[i], valeurs_moyen[i]) for i in range(n_moyen)]
    debut_moyen = time.time()
    profitMax_moyen = sac_a_dos(W_moyen, objets_moyen, n_moyen)
    fin_moyen = time.time()
    temps_moyen = fin_moyen - debut_moyen
    print("\nDonnées de taille moyenne :")
    print(f"Le profit maximum est : {profitMax_moyen}")
    print(f"Temps d'exécution : {temps_moyen:.10f} secondes")

    # Génération de données de grande taille
    poids_grand = [random.randint(1, 50) for _ in range(50)]
    valeurs_grand = [random.randint(1, 50) for _ in range(50)]
    W_grand = random.randint(50, 100)
    n_grand = len(poids_grand)
    objets_grand = [ObjetSac(poids_grand[i], valeurs_grand[i]) for i in range(n_grand)]
    debut_grand = time.time()
    profitMax_grand = sac_a_dos(W_grand, objets_grand, n_grand)
    fin_grand = time.time()
    temps_grand = fin_grand - debut_grand
    print("\nDonnées de grande taille :")
    print(f"Le profit maximum est : {profitMax_grand}")
    print(f"Temps d'exécution : {temps_grand:.10f} secondes")

















