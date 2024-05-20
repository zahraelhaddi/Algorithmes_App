from collections import deque

def bfs_labyrinthe(labyrinthe, start, end):
    rows = len(labyrinthe)
    cols = len(labyrinthe[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], [])])  # (ligne, colonne, chemin)

    while queue:
        i, j, chemin = queue.popleft()
        if (i, j) == end:
            return chemin + [(i, j)]  # Retourne le chemin trouvé
        if 0 <= i < rows and 0 <= j < cols and labyrinthe[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            queue.append((i+1, j, chemin + [(i, j)]))  # Bas
            queue.append((i-1, j, chemin + [(i, j)]))  # Haut
            queue.append((i, j+1, chemin + [(i, j)]))  # Droite
            queue.append((i, j-1, chemin + [(i, j)]))  # Gauche

    return None  # Aucun chemin trouvé

# Exemple de labyrinthe représenté sous forme de matrice où 0 représente un chemin libre et 1 représente un mur
labyrinthe_exemple = [
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]  # Chemin libre jusqu'à (4,4)
]

start_exemple = (0, 0)
end_exemple = (4, 4)

chemin_exemple = bfs_labyrinthe(labyrinthe_exemple, start_exemple, end_exemple)
if chemin_exemple:
    print("Chemin trouvé:")
    for i, j in chemin_exemple:
        print(f"({i}, {j})")
else:
    print("Aucun chemin trouvé.")
