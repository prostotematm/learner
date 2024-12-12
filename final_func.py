def calculate_structure_sum(data):
    all_sum = 0


    if isinstance(data, (tuple, list, set)):
        for item in data:
            all_sum += calculate_structure_sum(item)

    elif isinstance(data, (int, float)):
        all_sum += data

    elif isinstance(data, dict):
        for key, value in data.items():
            all_sum += calculate_structure_sum(key)
            all_sum += calculate_structure_sum(value)

    elif isinstance(data, str):
        all_sum += len(data)

    return all_sum


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)