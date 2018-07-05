from sys import argv
import json
from pprint import pprint

path_to_json_file = argv[1]
#check if argument is path
#check if their are to many arguments

json_data = open(path_to_json_file).read()
print(json_data)
