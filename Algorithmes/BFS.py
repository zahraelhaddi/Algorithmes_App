import time
from numpy import roots
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def BFS(root):
    if root is None:
        return
    queue = []  # Create a queue for storing nodes to be visited
    queue.append(root)  # Enqueue the root node

    while queue:  # Loop until the queue is empty
        current_node = queue.pop(0)  # Dequeue the next node to visit
        print(current_node.value)  # Process the current node

        if current_node.left is not None:  # Enqueue the left child
            queue.append(current_node.left)
        if current_node.right is not None:  # Enqueue the right child
            queue.append(current_node.right)

start_time = time.time()

#Exemple
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
BFS(root)

end_time = time.time()

temps_execution = end_time - start_time
print("Temps d'exécution:", temps_execution)