from sys import argv
import json
from pprint import pprint

json_data = json.loads(open(argv[1]).read())

def getLeaves(data, list):
    for dic in data:
        if "leaves" in dic:
            list.extend(dic["leaves"])
        if "branches" in dic:
            getLeavesList(dic["branches"], list)
    return(list)

def leavesPerNode(data):
    for dic in data:
        if "branches" in dic:
            leavesPerNode(dic["branches"])
            print(dic["id"] + " " + str(getLeavesList(dic["branches"], [])))
        if "leaves" in dic:
            print(dic["id"] + " " + str(dic["leaves"]))
