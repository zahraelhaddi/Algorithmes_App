import time

class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

def bfs(racine):
    if racine is None:
        return

    start_time = time.time()
    queue = [racine]

    while queue:
        current = queue.pop(0)
        print(current.valeur, end=' ')

        if current.gauche is not None:
            queue.append(current.gauche)

        if current.droite is not None:
            queue.append(current.droite)
    
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def generer_arbre(profondeur, valeur_initiale=1):
    if profondeur < 1:
        return None
    
    racine = Noeud(valeur_initiale)
    queue = [(racine, 1)]

    while queue:
        current, level = queue.pop(0)
        if level < profondeur:
            current.gauche = Noeud(current.valeur * 2)
            current.droite = Noeud(current.valeur * 2 + 1)
            queue.append((current.gauche, level + 1))
            queue.append((current.droite, level + 1))
    
    return racine

# Arbre binaire de petite taille (profondeur 3)
racine_petite = generer_arbre(3)
print("BFS de l'arbre de petite taille (profondeur 3):")
temps_petite = bfs(racine_petite)
print(f"\nTemps d'exécution: {temps_petite:.10f} secondes\n")

# Arbre binaire de taille moyenne (profondeur 6)
racine_moyenne = generer_arbre(6)
print("BFS de l'arbre de taille moyenne (profondeur 6):")
temps_moyenne = bfs(racine_moyenne)
print(f"\nTemps d'exécution: {temps_moyenne:.10f} secondes\n")

# Arbre binaire de grande taille (profondeur 10)
racine_grande = generer_arbre(10)
print("BFS de l'arbre de grande taille (profondeur 10):")
temps_grande = bfs(racine_grande)
print(f"\nTemps d'exécution: {temps_grande:.10f} secondes\n")
