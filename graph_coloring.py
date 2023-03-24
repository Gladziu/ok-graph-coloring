# Wczytaj plik z listą sąsiedztwa
with open('lista_sasiedztwa.txt', 'r') as file:
    lines = file.readlines()

num_of_vertex = int(lines[0])

# Zdefiniuj graf jako słownik list sąsiedztwa
graph = {}
for line in lines[1:]:
    line = line.strip().split()
    vertex1, vertex2 = int(line[0]), int(line[1])
    if vertex1 not in graph:
        graph[vertex1] = []
    if vertex2 not in graph:
        graph[vertex2] = []
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

# Zdefiniuj słownik kolorów, w którym każdy wierzchołek ma początkowo przypisany kolor 'None'
colors = {}
for vertex in graph:
    colors[vertex] = None

# Greedy algorithm
# Iteruj przez pozostałe wierzchołki i przypisz każdemu kolor, który nie jest używany przez jego sąsiadów
for vertex in graph.keys():

    # Utwórz zbiór kolorów używanych przez sąsiadów
    used_colors = set()
    for neighbour in graph[vertex]:
        if colors[neighbour] is not None:
            used_colors.add(colors[neighbour])

    # Przypisz pierwszy nieużywany kolor
    for color in range(1, num_of_vertex+1):
        if color not in used_colors:
            colors[vertex] = color
            break

# Wydrukuj wyniki
# Policz ile kolorow zostało użytych
temp = []
for key, value in sorted(colors.items()):
    if value not in temp:
        temp.append(value)
print('used colors', len(temp))

# Spis koloru każdej krawedzi
for key, value in sorted(colors.items()):
    print(key, ':', value)
