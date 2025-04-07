import json
import os

from setuptools.dist import sequence

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as file_obj:
        data = json.load(file_obj)
    if field in data.keys():
        return data[field]
    else:
        print(f"Field {field} not exist.")
        return None

def pattern_search(sequence, pattern):
    set_of_idxs = set()
    pattern_length = len(pattern)
    for idx in range(0, len(sequence) - pattern_length):
        pattern_similarity = 0
        for idx_pattern, pattern_element in enumerate(pattern):
            if sequence [idx + idx_pattern] == pattern_element:
                pattern_similarity = pattern_similarity + 1
            else:
                pass
        if pattern_similarity == pattern_length:
            set_of_idxs.add(idx + pattern_length // 2 - 1)
        else:
            pass
    return set_of_idxs





def main():
    my_data = read_data("sequential.json", "unordered_numbers")
    print(my_data)

def linear_search(sequence, number):
    list_of_idxs = []
    for idx, element in enumerate(sequence):
        if element == number:
            list_of_idxs.append(idx)
        else:
            continue
    return {"positions":list_of_idxs, "count":len(list_of_idxs)}

if __name__ == '__main__':
    main()
    my_list = [1, 2, 5, 7]
    searched_number = 5
    found_numbers = linear_search(my_list, searched_number)