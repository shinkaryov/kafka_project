# --------------------------------------------------------
'''
function which prepare data from jsonl file
deleting duplicates, null-values (HW1)
'''
# --------------------------------------------------------


def prepare_data(path_to_file: str):
    with open(path_to_file, encoding='utf-8') as f:
        data = []
        for line in f:
            data.append(line.replace('\n', ''))
        null = 'null'
        false = False
        true = True
        for i in range(len(data)):
            data[i] = eval(data[i])
        data = list({d.get('name') + str(d.get('time_created')): d for d in data}.values())
    unique_keys = set(x for d in data for x in d.keys())
    for key in unique_keys:
        # defining the type of unique keys' values
        for x in data:
            if key in x.keys() and x[key] != 'null':
                type_of_key_value = type(x[key])
                break
        # filling empty fields
        if type_of_key_value == int or type_of_key_value == float:
            list_of_values = [x[key] for x in data if key in x.keys() and x[key] != 'null']
            number_of_values = len(list_of_values)
            sum_of_values = sum(list_of_values)
            if type_of_key_value == int:
                mean_value = sum_of_values // number_of_values
            else:
                mean_value = sum_of_values / number_of_values
            for x in data:
                if key not in x.keys() or x[key] == 'null':
                    x[key] = mean_value
        elif type_of_key_value == str:
            dict_of_values = {}
            for x in data:
                if key in x.keys() and x[key] != 'null':
                    if x[key] in dict_of_values.keys():
                        dict_of_values[x[key]] += 1
                    else:
                        dict_of_values[x[key]] = 1
            max_value = max(dict_of_values, key=dict_of_values.get)
            for x in data:
                if key not in x.keys() or x[key] == 'null':
                    x[key] = max_value
        else:
            for x in data:
                if key not in x.keys() or x[key] == 'null':
                    x[key] = False
    return {d.get('name') + str(d.get('time_created')): d for d in data}