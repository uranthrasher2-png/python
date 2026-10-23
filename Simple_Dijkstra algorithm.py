graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'fin': 1},
    'b': {'a': 3, 'fin': 5},
    'fin': {}
}

costs = {'a': 6, 'b': 2, 'fin': float('inf')}
parents = {'a': 'start', 'b': 'start', 'fin': None}
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

print("🚀 Начинаем поиск кратчайшего пути\n")

node = find_lowest_cost_node(costs)

while node is not None:
    print(f"🔍 Обрабатываем '{node}' (стоимость: {costs[node]})")
    current_cost = costs[node]
    neighbors = graph[node]
    print(f"   Соседи: {neighbors}")

    for neighbor in neighbors:
        new_cost = current_cost + neighbors[neighbor]
        print(f"   Путь до '{neighbor}': {current_cost} + {neighbors[neighbor]} = {new_cost}")
        if costs[neighbor] > new_cost:
            print(f"   ✅ Обновляем '{neighbor}': {costs[neighbor]} → {new_cost}")
            costs[neighbor] = new_cost
            parents[neighbor] = node
        else:
            print(f"   ❌ Не короче (было {costs[neighbor]})")

    processed.append(node)
    print(f"   📌 Обработано: {processed}\n")
    node = find_lowest_cost_node(costs)

print(f"🎉 Кратчайшее расстояние до 'fin': {costs['fin']}")
path = []
step = 'fin'
while step is not None:
    path.append(step)
    step = parents.get(step)
path.reverse()
print(f"✅ Путь: {' -> '.join(path)}")