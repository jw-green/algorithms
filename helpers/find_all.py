from config import DETAILS_FILENAME
from os import listdir

from algo import Algo


def find_all(path, output=False):

    algos = []
    type_list = listdir(path)  # Get list of types

    for algo_type isn type_list:

        algo_type_path = path + algo_type + "/"  # Get path of algo type

        # Get list of algo names for type
        algo_name_list = listdir(algo_type_path)

        for algo_name in algo_name_list:

            details = ""  # Blank details filename
            algo_name_path = algo_type_path + algo_name + "/"  # Make algo name path string

            # Get list of algo languages
            algo_languages = listdir(algo_name_path)

            if DETAILS_FILENAME in algo_languages:  # If there's a details file, log it and remove
                details = algo_name_path + DETAILS_FILENAME    # - Log
                algo_languages.remove(DETAILS_FILENAME)        # - Remove

            # All details collected. Log Algo
            algos.append(Algo(algo_name, algo_type, details, algo_languages))

    if output is True:
        for algo in algos:
            algo_desc = algo.__str__()
            print(algo_desc)

    return algos
