import random
from copy import deepcopy


def initial_coloring(graph):
    # Zapisanie do słownika degrees ilość sąsiadów każdego wierzchołka
    degrees = {}
    for vertex, neighbors in graph.items():
        degrees[vertex] = len(neighbors)

    vertices = list(graph.keys())
    vertices.sort(key=lambda v: degrees[v], reverse=True)

    colors = {}
    for vertex in vertices:
        neighbor_colors = set()
        # Iteracja po sąsiadach wierzchołków i zapisanie kolorów sasiednich do neighbor_colors
        for neighbor in graph[vertex]:
            if neighbor in colors:
                neighbor_colors.add(colors[neighbor])

        # Usuwanie zajętych kolorów przez sąsiadów i uzyskanie wszytskich
        available_colors = set(range(len(graph))) - neighbor_colors
        if available_colors:
            colors[vertex] = min(available_colors)
        else:
            colors[vertex] = len(graph)  # Nowy kolor

    return colors


def color_graph(graph, iteration, max_tabu_length):
    # Inicjalizacja kolorowania
    colors = {}
    tabu_list = []
    best_solution = None
    best_coloring = None

    # Funkcja pomocnicza do wyznaczania puli kolorów możliwych do pokolorowania danego wierzchołka
    def get_allowed_colors(vertex):

        # Przypisanie do used_colors kolorów używanych przez sąsiadów
        used_colors = set()
        for neighbor in graph[vertex]:
            if neighbor in colors:
                used_colors.add(colors[neighbor])

        # Przypisanie do available_colors od 0 do liczby wierzcholkow
        available_colors = []
        for color in range(len(graph)):
            if color not in used_colors:
                available_colors.append(color)

        return available_colors

    # Inicjalizacja początkowego kolorowania
    colors = initial_coloring(graph)

    """
    for vertex in graph:
        colors[vertex] = random.randint(0, len(graph) - 1)
    """

    # Główna pętla algorytmu Tabu Search
    iterations = 0
    while iterations < iteration:  # Można dostosować liczbę iteracji
        best_neighbor = None
        best_color = None
        best_conflict = float('inf')

        # Wybieranie najlepszego sąsiada
        for vertex in graph:
            current_color = colors[vertex]
            for color in get_allowed_colors(vertex):
                if color != current_color:
                    colors[vertex] = color
                    # delta = sum(1 for neighbor in graph[vertex] if colors[neighbor] == color)

                    # Sprawdzenie konfliktu miedzy sasiadami
                    conflict = 0
                    for neighbor in graph[vertex]:
                        if colors[neighbor] == color:
                            conflict += 1

                    # Jezeli konflikt sie zmniejszyl i kolor nie jest w tabu to przypisz ten kolor do best_color
                    if conflict < best_conflict and color not in tabu_list:
                        best_neighbor = vertex
                        best_color = color
                        best_conflict = conflict
                    colors[vertex] = current_color

        # Aktualizacja kolorowania
        if best_neighbor is not None:
            colors[best_neighbor] = best_color
            tabu_list.append(best_color)  # Elastyczna lista tabu
            if len(tabu_list) > max_tabu_length:
                tabu_list.pop(0)

            # Zapisanie pokolororwania do best_coloring, gdzie użyto najmniej różnych kolorów
            if best_solution is None or len(set(colors.values())) < best_solution:
                best_solution = len(set(colors.values()))
                best_coloring = deepcopy(colors)



        iterations += 1

    return best_coloring


# Wczytanie grafu z pliku
with open('lista_sasiedztwa.txt', 'r') as file:
    lines = file.readlines()

# Liczba wierzchołków
num_of_vertexes = int(lines[0])

# Zdefiniowanie grafu jako słownik listy sąsiedztwa
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

del lines

# Sortowanie grafu
graph = {k: sorted(v) for k, v in sorted(graph.items())}


# Ustawienie zmiennych do Tabu Search
iteration = 50
tabu_lenght = 20


coloring = color_graph(graph, iteration, tabu_lenght)


# Policz ile kolorow zostało użytych
temp = []
for key, value in sorted(coloring.items()):
    if value not in temp:
        temp.append(value)

print('Colors of each vertex ',coloring)
print('Used colors', len(temp))
