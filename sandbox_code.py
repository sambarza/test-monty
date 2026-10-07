# Probe: mutate a dict while iterating its items.
# Checks if Monty's dict iterator is safe against structural mutation.
d = {'a': 1, 'b': 2, 'c': 3}
result = []
try:
    for k, v in d.items():
        result.append(k)
        if k == 'a':
            d['x'] = 99  # add new key during iteration
    result = 'survived: ' + str(result)
except Exception as e:
    result = type(e).__name__ + ': ' + str(e)
result
