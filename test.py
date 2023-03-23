with open("myciel4.txt", "r") as f:
    lines = f.readlines()

colors = lines[0]
print(colors)
edges = []

for line in lines[1:]:
    values = line.strip().split(" ")
    tup = tuple(map(int, values))
    edges.append(tup)

print(edges)