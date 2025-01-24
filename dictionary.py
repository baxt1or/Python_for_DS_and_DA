# Variable / ozgaruvchi - a container of a value like string, integer, boolean or float


def group_data_by_lenths(arr: list[str]):

    result = {}

    for word in arr:
        word_len = len(word)

        if word_len in result:
            result[word_len].append(word)
        else:
            result[word_len] = [word]
    return result


data = {'a': 3, 'b': 7, 'c': 1}  


def get_max_value(data):

    max_val = max([val for val in data.values()])

    for key, val in data.items():
        if val == max_val:
            return key
    return "No data"

def get_squares(nums:list[int]):

    return {n:n**2 for n in nums}

def sort_by_values(data, ascending=False):
    
    return {key:val for key, val in sorted(data, key=lambda x: x[1], reverse=ascending)}

def sort_by_keys(data, ascending=False):

    result = {key:data[key] for key in sorted(data.keys(), reverse=ascending) }

    return result

def get_frequency_words(sentence:str):
    counter = {}

    for word in sentence.split():
        counter[word] = counter.get(word, 0)+1
    
    return counter
 


def get_common_keys(dict1, dict2):
    keys = [key for key in dict1.keys()]
    keys.extend([key for key in dict2.keys()])

    counter = {}

    for key in keys:
        counter[key] = counter.get(key,0)+1

    result = [key for key, val in counter.items() if val == 2]
    
    return result


