from sys import argv
import json
from pprint import pprint

path_to_json_file = argv[1]
#check if argument is path
#check if their are to many arguments

def load_json_dictionary_from_path(path):
    ####
    # arg: get the path given as argument
    # ret: return python dictionary
    ####
    return_dictionary = {}

    json_data = json.loads(open(path).read())

    # what if the json is a list?
    # IMPORTANT !!!!!
    # if the json is a list, that means it is just a list of multiple trees
    # act accordingly, prepare the data for counting in a different function
    # or use a datastructure / object handling the multiple trees
    def make_json_to_dictionary(json_data):
        for dictionary in json_data:
            return_dictionary[str(json_data.index(dictionary))] = dictionary

    if isinstance(json_data, list):
        make_json_to_dictionary(json_data)

    return(return_dictionary)

def count_leaves(json_tree):
    ###
    # arg: the tree like data structure
    # return: the list of all Leaves
    #
    ###
    leaves_list = []

    for data in json_tree:

        if data['leaves']:
            # if the node contains leaves
            leaves_list.append(data['leaves'])
        elif data['branches']:
            # if the node contains branches
            count_leaves(data['branches'])
        else:
            # if
            count_leaves(json_tree.index(data))

    return(leaves_list)        
