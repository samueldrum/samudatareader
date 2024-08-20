import numpy as np

def format_element(list):
    new_list = []
    for elem in list:
        if elem.isnumeric():
            new_list.append(float(elem))
        else:
            new_list.append(elem)
    return new_list
        
