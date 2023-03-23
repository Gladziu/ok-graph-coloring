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

# Utwórz zbiór wszystkich użytych kolorów
used_colors = set()

# Iteruj przez pozostałe wierzchołki i przypisz każdemu kolor, który nie jest używany przez jego sąsiadów
for vertex in graph.keys():

    # Utwórz zbiór kolorów używanych przez sąsiadów
    local_used_colors = set()
    for neighbour in graph[vertex]:
        if colors[neighbour] is not None:
            local_used_colors.add(colors[neighbour])

    # Dodaj kolor do zbioru użytych kolorów
    used_colors.update(local_used_colors)

    # Przypisz pierwszy nieużywany kolor
    for color in range(1, num_of_vertex+1):
        if color not in local_used_colors:
            colors[vertex] = color
            break

# Policz ile kolorow zostało użytych
all_colors = len(used_colors)

# Wydrukuj wynik
print('used colors', all_colors)

for key, value in sorted(colors.items()):
    print(key, ':', value)
