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

def calculate_conflict(graph, colors):
    cost = 0

    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            if colors[vertex] == colors[neighbor]:
                cost += 1

    return cost


colors = {58: 0, 38: 0, 36: 1, 11: 2, 68: 2, 99: 3, 23: 4, 27: 5, 39: 5, 75: 6, 12: 4, 29: 7, 30: 8, 64: 9, 66: 1, 44: 9, 45: 10, 53: 7, 77: 11, 80: 11, 10: 12, 33: 12, 61: 13, 73: 5, 78: 8, 93: 14, 96: 10, 7: 15, 19: 9, 55: 16, 1: 20, 2: 14, 5: 3, 22: 17, 25: 18, 35: 6, 63: 15, 69: 11, 72: 7, 82: 4, 85: 14, 98: 19, 100: 20, 6: 17, 24: 15, 40: 10, 46: 13, 49: 1, 67: 17, 89: 19, 95: 16, 97: 16, 8: 12, 9: 21, 20: 6, 21: 21, 37: 22, 50: 22, 51: 10, 56: 3, 57: 18, 62: 23, 71: 20, 74: 5, 79: 24, 90: 23, 92: 23, 15: 25, 31: 25, 41: 22, 48: 26, 54: 9, 60: 26, 65: 4, 81: 0, 4: 25, 14: 27, 17: 8, 28: 27, 52: 24, 91: 28, 26: 18, 47: 1, 70: 2, 84: 13, 94: 21, 3: 19, 18: 29, 43: 14, 59: 28, 34: 19, 13: 27, 88: 18, 16: 30, 32: 29, 42: 12, 87: 13, 76: 3, 83: 1, 86: 12}


sorted_colors = {key: value for key, value in sorted(colors.items())}

print(sorted_colors)

conflict = calculate_conflict(graph, sorted_colors)

print("Conflicts: ", conflict)
