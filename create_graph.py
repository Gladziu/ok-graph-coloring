import random

# Ustaw liczbe wierzcholkow i nasycenie krawedzi
num_vertices = 10
edge_density = 0.55

def generate_graph(num_vertices, edge_density):

    adjacency_list = []

    # Dodaj polaczenie wierzcholkow uwzgledniajac nasycenie krawedzi
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            random_number = random.random()     # Random number between 0.0 - 1.0
            if random_number < edge_density:
                adjacency_list.append((i + 1, j + 1))
                
    return sorted(adjacency_list)

graph = generate_graph(num_vertices, edge_density)

with open('lista_sasiedztwa.txt', 'w') as f:
    f.write(f"{num_vertices}")
    for edge in graph:
        f.write(f"\n{edge[0]}  {edge[1]}")
