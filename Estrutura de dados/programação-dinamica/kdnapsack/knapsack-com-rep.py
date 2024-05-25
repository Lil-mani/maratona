def knapsack(values, weights, k, lookup=None):
    lookup = {} if lookup is None else lookup
    if k in lookup:
        return lookup[k]
    max_value = 0
    for i in range(len(values)):
        if weights[i] <= k:
            max_value = max(max_value, values[i]+knapsack(values, weights, k-weights[i], lookup))
    lookup[k] = max_value
    return lookup[k]