import streamlit as st
import numpy as np

# Dictionary to store algorithm information (GIF, explanation, complexity)
algorithms = {
    "BFS, Parcours en Largeur": {
        "gif": r"Breadth-First-Search-Algorithm.gif",
        "Explication": """
        Le parcours en largeur (BFS, Breadth-First Search) est un algorithme permettant de parcourir ou de rechercher des structures de données en arborescence ou en graphe. 
        Il commence à un nœud racine (source sélectionnée) et explore tous les nœuds voisins au niveau courant avant de passer au niveau suivant. 
        Le BFS utilise une file FIFO (First-In-First-Out) pour stocker les nœuds découverts mais pas encore explorés.
        """,
        "Applications":"""
        - Trouver le plus court chemin entre deux nœuds dans un graphe non pondéré.
        - Algorithmes de routage réseau.
        - Détection de cycles dans les graphes.
        - Trouver des composantes connexes dans un graphe.
        """,
        "Complexité": "O(S + A)  avec S: sommets, A: arêtes"  # V: vertices, E: edges
    },
    "DFS, Parcours en Profondeur": {
        "gif": r"Depth-First-Search.gif",
        "Explication": """
        Le parcours en profondeur (DFS, Depth-First Search) est un algorithme permettant de parcourir ou de rechercher des structures de données en arborescence ou en graphe. 
        Il commence à un nœud racine (source sélectionnée) et explore le plus loin possible le long de chaque branche avant de revenir en arrière. 
        Le DFS utilise une pile LIFO (Last-In-First-Out) pour suivre les nœuds visités.
        """,
        "Applications":"""
        - Trouver des composantes connexes dans un graphe.
        - Tri topologique (ordonner un graphe acyclique dirigé).
        - Détection de cycles dans les graphes.
        """,
        "Complexité": "O(S + A)   avec  S: sommets, A: arêtes"  # V: vertices, E: edges
    },
    "Recherche d'une clé dans un arbre binaire de recherche": {
        "gif": r"Binary_search_tree_example.gif",
        "Explication": """
        La recherche dans un arbre binaire de recherche (ABR) est un algorithme permettant de rechercher efficacement une valeur spécifique (clé) dans un arbre binaire de recherche trié. 
        Il commence au nœud racine et compare la clé avec la valeur du nœud. Si elles sont égales, la recherche est réussie. 
        Si la clé est inférieure à la valeur du nœud, la recherche continue de manière récursive sur le sous-arbre gauche. Sinon, la recherche continue de manière récursive sur le sous-arbre droit.
        """,
        "Applications":"""
        - Rechercher efficacement des éléments dans des ensembles de données triés.
        - Implémentation de magasins de valeurs clés et de dictionnaires.
        """,
        "Complexité": "O(h)   avec h: hauteur de l'ABR (cas moyen)"  # h: height of the BST (average case)
    
    },
    "Heuristique Gloutonne, Rendu de monnaie (MAD)": {
        "gif": "flos.png",  # Replace with a suitable GIF
        "Explication": """
        Le problème du rendu de monnaie consiste à trouver le nombre minimal de pièces et billets nécessaires pour rendre une somme donnée en monnaie marocaine (MAD). 
        Les pièces et billets disponibles sont:
        - 1 Dirham
        - 2 Dirhams
        - 5 Dirhams
        - 10 Dirhams
        - 20 Dirhams
        - 50 Dirhams
        - 100 Dirhams

        **Exemple:**
        Si la somme à rendre est de 27 Dirhams, une solution possible est d'utiliser:
        - 1 billet de 20 Dirhams
        - 1 billet de 5 Dirhams
        - 2 pièces de 1 Dirham

        **Algorithme:**
        L'algorithme glouton peut être utilisé pour résoudre ce problème. 
        L'algorithme glouton consiste à sélectionner à chaque étape la pièce ou billet de valeur maximale qui peut encore être utilisée pour rendre la somme restante. 
        Ce processus est répété jusqu'à ce que la somme restante soit nulle.
        """,
        "Applications":"""
        - Distribution de monnaie dans les distributeurs automatiques
        - Calcul du change dans les magasins
        """,
        "Complexité": "O(n)    avec n: montant à rendre"  # n: montant à rendre
    },
    "Floyd Warshall , problème du plus court chemin": {
        "gif": r"Floyd_warshall_gif.gif",
        "Explication": """
        L'algorithme de Floyd Warshall est utilisé pour trouver le plus court chemin entre tous les paires de sommets dans un graphe pondéré. Contrairement à Dijkstra qui trouve le plus court chemin d'un sommet source à tous les autres sommets, Floyd Warshall peut être utilisé pour trouver le plus court chemin entre tous les paires de sommets.
        """,
        "Applications":"""
        - Calculer les chemins les plus courts dans les réseaux de transport.
        - Trouver le chemin le plus court pour livrer des marchandises à partir de différents entrepôts à différents clients.
        - Analyse de réseaux informatiques pour la transmission de données efficace.

        """,
        "Complexité": "O(n^3)    avec n: Nombre de sommets dans le graphe"  # V: nombre de sommets dans le graphe
    },
    "Heuristique du Plus Proche Voisin": {
        "gif": r"Nearestneighbor.gif",
        "Explication": """
        L'HPVN fonctionne en construisant une solution de manière itérative en sélectionnant, 
        à chaque étape, l'élément le plus proche (en termes de distance ou de similarité) d'un point de référence.
        Ce processus se poursuit jusqu'à ce que tous les éléments soient inclus dans la solution.
        """,
        "Applications":"""
        - Résolution de problèmes de tournées: Détermination du chemin le plus court pour visiter un ensemble de points dans un ordre spécifique, comme dans la livraison de colis ou la planification de trajets.
        - Clustering: Regroupement d'objets en fonction de leur similarité, utilisé en analyse de données et en apprentissage automatique.
        - Appariement: Association d'éléments en fonction de leur compatibilité, comme dans la recommandation de produits ou la mise en relation de personnes.
        - Optimisation de placement: Disposition d'objets dans un espace donné de manière à minimiser une certaine mesure, comme la distance ou le temps de déplacement.
        """,
        "Complexité": "O(n^2)    avec n: Nombre de villes à visiter"  # h: height of the BST (average case)
    
    }
    ,
    "Algorithme du Backtracking, Jeu de Sudoku": {
        "gif":"Sudoku_solved_by_bactracking.gif",
        "Explication": """
        Le solveur Sudoku est un algorithme qui résout des grilles de Sudoku en utilisant une approche de recherche exhaustive combinée à un processus de rétrogradation (backtracking).
        """,
        "Applications":"""
        - Résolution de grilles de Sudoku pour le plaisir ou la compétition.
        """,
        "Complexité": "O(9^(n*n))"  # Exponential time complexity
    }
}

def solve_sudoku(board):
    # Find empty cell
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Puzzle solved

    row, col = empty_cell

    # Try values from 1 to 6
    for num in range(1, 7):
        if is_valid_move(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # If puzzle is solved recursively

            # Backtrack if the puzzle cannot be solved with current configuration
            board[row][col] = 0

    return False  # Puzzle cannot be solved

# Helper function to find empty cell
def find_empty_cell(board):
    for i in range(6):
        for j in range(6):
            if board[i][j] == 0:
                return (i, j)
    return None

# Helper function to check if move is valid
def is_valid_move(board, num, pos):
    # Check row
    if num in board[pos[0]]:
        return False

    # Check column
    if num in [board[i][pos[1]] for i in range(6)]:
        return False

    # Check 2x3 box
    box_row, box_col = pos[0] // 2 * 2, pos[1] // 3 * 3
    for i in range(2):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True

# Function to display Sudoku board
def display_sudoku(board):
    for i in range(6):
        row = ""
        for j in range(6):
            row += str(board[i][j]) + " "
        st.write(row)

st.title("Visualisation des Algorithmes")
additional_info_container1 = st.sidebar.container()
additional_info_container1.image("ENSABERRECHID_logo20230124170433.png", width=200)
  # Adding space
additional_info_container1.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        width: 20px;
        position: relative;
    }
    .sidebar img {
        position: absolute;
        top: 2px; /* Adjust top position as needed */
        left: 1px; /* Adjust left position as needed */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.sidebar.title("Projet Implémentation des Algorithmes Avancés:")

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        width: 0px;
    }
    </style>
    """,unsafe_allow_html=True,
)


selected_algorithm = st.sidebar.selectbox("veuillez choisir un algorithme", list(algorithms.keys()))

algorithm_info = algorithms[selected_algorithm]



st.header(selected_algorithm)
st.image(algorithm_info["gif"])

if selected_algorithm == "Rendu de monnaie (MAD)":
    def coin_change_mad(total_amount, price):
        """
        Calculates the minimum number of MAD coins to return change for a given price.

        Args:
            total_amount (float): The total amount paid by the customer.
            price (float): The price of the item purchased.

        Returns:
            List: A list containing the denominations and quantities of coins to be returned.
        """

        change = total_amount - price
        coins = []

        # Available MAD denominations
        denominations = [100, 50, 20, 10, 5, 2, 1]

        while change > 0:
            for denomination in denominations:
                if change >= denomination:
                    coins.append((denomination, int(change / denomination)))
                    change %= denomination
                    break

        return coins

    # User input for total amount and price
    total_amount = st.number_input("Somme totale payée:", min_value=0.01)
    price = st.number_input("Prix de l'article:", min_value=0.01)

    # Calculate and display coin change
    if st.button("Calculer le rendu de monnaie"):
        if total_amount < price:
            st.error("La somme totale payée doit être supérieure ou égale au prix de l'article.")
        else:
            change_coins = coin_change_mad(total_amount, price)
            st.write("Rendu de monnaie:")
            for coin in change_coins:
                st.write(f"{coin[0]} Dirhams: {coin[1]} pièces")


# if selected_algorithm == "Algorithme du Backtracking, Jeu de Sudoku":
#     st.subheader("Jeu de Sudoku 6x6")
#     sudoku_board = [[0 for _ in range(6)] for _ in range(6)]
#     for i in range(6):
#         for j in range(6):
#             sudoku_board[i][j] = st.number_input(f"Cellule ({i}, {j})", min_value=0, max_value=6, key=f"cell_{i}_{j}")

#     if st.button("Résoudre Sudoku"):
#         if solve_sudoku(sudoku_board):
#             st.success("Sudoku résolu avec succès!")
#             st.subheader("Sudoku Solution")
#             display_sudoku(sudoku_board)
#         else:
#             st.error("Impossible de résoudre le Sudoku. Veuillez vérifier la configuration.")

if selected_algorithm == "Algorithme du Backtracking, Jeu de Sudoku":
    st.subheader("Sudoku Puzzle (6x6)")
    sudoku_board = [[0 for _ in range(6)] for _ in range(6)]
    for i in range(6):
        row = st.columns(6)
        for j in range(6):
            sudoku_board[i][j] = row[j].number_input(f"Cellule ({i}, {j})", min_value=0, max_value=6, key=f"cell_{i}_{j}")

    if st.button("Résoudre Sudoku (6x6)"):
        if solve_sudoku(sudoku_board):
            st.success("Sudoku résolu avec succès!")
            st.subheader("Sudoku Solution (6x6)")
            display_sudoku(sudoku_board)
        else:
            st.error("Impossible de résoudre le Sudoku. Veuillez vérifier la configuration.")



st.subheader("Explication")
st.write(algorithm_info["Explication"])
st.subheader("Applications")
st.write(algorithm_info["Applications"])
st.subheader("Complexité")
st.write(algorithm_info["Complexité"])

# Enhancements (consider implementing based on feedback):
# -
additional_info_container = st.sidebar.container()
# additional_info_container.image("ENSABERRECHID_logo20230124170433.png", use_column_width=True)
additional_info_container.markdown("### Projet Encadré par: Mr.Naimi Mohamed")
additional_info_container.markdown("## Projet préparé par: ")
additional_info_container.markdown("###                     Zahra EL Haddi")

additional_info_container.markdown("###                     Hafsa Aziz")
additional_info_container.markdown("###                     Nihal Snaj")

additional_info_container.markdown("## Filière: Ingénierie des systèmes d'information et Big Data")
additional_info_container.markdown("## Semestre: S8")
additional_info_container.markdown("## école: ENSA Berrechid")
additional_info_container.write("2023/2024")
