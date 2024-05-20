import csv
import random

def generer_donne_arbre(num_nodes, max_depth, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['node_id', 'parent_id', 'value'])

        for node_id in range(num_nodes):
            parent_id = None if node_id == 0 else random.randint(0, node_id - 1)
            value = random.randint(-100, 100)
            writer.writerow([node_id, parent_id, value])

if __name__ == '__main__':
    num_nodes = 1000 
    max_depth = 10  
    filename = 'tree_data_medium.csv'

    generer_donne_arbre(num_nodes, max_depth, filename)
