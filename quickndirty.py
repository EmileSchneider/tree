from sys import argv
import json
from pprint import pprint

json_data = json.loads(open(argv[1]).read())

def get_leaves(data, return_list):
    for dic in data:
        if "leaves" in dic:
            return_list.extend(dic["leaves"])
        if "branches" in dic:
            get_leaves(dic["branches"], return_list)
    return return_list

def leaves_per_node(data, return_list):
    for dic in data:
        if "branches" in dic:
            return_list.append((dic["id"], get_leaves(dic["branches"], [])))
            leaves_per_node(dic["branches"], return_list)
        if "leaves" in dic:
            return_list.append((dic["id"], dic["leaves"]))
    return return_list

print("Leaves: ", get_leaves(json_data, []))
print("Leaves per node:", leaves_per_node(json_data, []))
