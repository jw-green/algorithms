from config import ALGO_ROOT, DETAILS_FILE_NAME
from os import listdir

from algo import Algo

algos = []
# type_paths = []
# name_paths = []

type_list = listdir(ALGO_ROOT)                              #Get list of types

for algo_type in type_list:

    algo_type_path = ALGO_ROOT + algo_type + "/"            #Get path of algo type
    # type_paths.append(algo_type_path)                       #DEBUG: Create list of algo type paths

    algo_name_list = listdir(algo_type_path)                #Get list of algo names for type

    for algo_name in algo_name_list:

        details = ""
        
        algo_name_path = algo_type_path + algo_name + "/"   #Make algo name path string
        # name_paths.append(algo_name_path)                   #DEBUG: Create list of algo name paths
        print(algo_name_path)

        algo_languages = listdir(algo_name_path)            #Get list of algo languages

        if DETAILS_FILE_NAME in algo_languages:             #If there's a details file, log it and remove
            details = algo_name_path + DETAILS_FILE_NAME    # - Log
            algo_languages.remove(DETAILS_FILE_NAME)        # - Remove
               
        algos.append(Algo(algo_name, algo_type, details, algo_languages))  #All details collected. Log Algo

for algo in algos:
    algo_desc = algo.__str__()
    print(algo_desc)

    