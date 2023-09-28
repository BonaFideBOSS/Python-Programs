def knapsack(cap, wgt, val):
    n = len(val)
    ks = [[0 for _ in range(cap + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(cap + 1):
            if wgt[i - 1] <= w:
                ks[i][w] = max(ks[i - 1][w], ks[i - 1][w - wgt[i - 1]] + val[i - 1])
            else:
                ks[i][w] = ks[i - 1][w]

    max_value = ks[n][cap]

    selected_items = []
    w = cap
    for i in range(n, 0, -1):
        if ks[i][w] != ks[i - 1][w]:
            selected_items.append(i - 1)
            w -= wgt[i - 1]

    selected_items.reverse()
    return max_value, selected_items


items = [
    {"name": "green", "weight": 12, "value": 4},
    {"name": "purple", "weight": 1, "value": 2},
    {"name": "brown", "weight": 1, "value": 1},
    {"name": "blue", "weight": 2, "value": 2},
    {"name": "yellow", "weight": 4, "value": 10},
]

values = [item["value"] for item in items]
weights = [item["weight"] for item in items]
capacity = 15

max_value, selected_items = knapsack(capacity, weights, values)

print("Maximum value:", max_value)
print("Selected items:", [items[i]["name"] for i in selected_items])
print("Selected items weight:", sum([items[i]["weight"] for i in selected_items]))
