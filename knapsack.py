def knapSack(cap, wgt, val, n):
    n = n if n == 0 else n - 1

    if n == 0 or cap == 0:
        return 0, []

    if wgt[n] > cap:
        return knapSack(cap, wgt, val, n)

    old_max_val, old_item_set = knapSack(cap, wgt, val, n)
    new_max_val, new_item_set = knapSack(cap - wgt[n], wgt, val, n)
    new_max_val += val[n]

    if new_max_val > old_max_val:
        return new_max_val, new_item_set + [n]
    else:
        return old_max_val, old_item_set


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
item_count = len(items)

max_value, selected_items = knapSack(capacity, weights, values, item_count)

print("Maximum value:", max_value)
print("Selected items:", [items[item]["name"] for item in selected_items])
print("Selected items weight:", sum([items[item]["weight"] for item in selected_items]))
