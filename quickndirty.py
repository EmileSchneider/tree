from sys import argv
import json
from pprint import pprint

json_data = json.loads(open(argv[1]).read())

def getLeaves(data, list):
    for dic in data:
        if "leaves" in dic:
            list.extend(dic["leaves"])
        if "branches" in dic:
            getLeaves(dic["branches"], list)
    return(list)

def leavesPerNode(data, list):
    for dic in data:
        if "branches" in dic:
            leavesPerNode(dic["branches"], list)
            list.append(dic["id"] + " " + str(getLeaves(dic["branches"], [])))
        if "leaves" in dic:
            list.append(dic["id"] + " " + str(dic["leaves"]))
    return(list)

pprint("Leaves: " + str(getLeaves(json_data, [])))
print("Leaves per node: " + str(leavesPerNode(json_data, [])))
