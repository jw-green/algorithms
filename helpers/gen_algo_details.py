from config import *
from os import listdir

from algo import Algo
from file_manager import FileManager
from find_all import find_all


class Block:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def setContent(self, value):
        self.content = content

    def setContentFromFile(self, filename):
        file_handle = open(filename, "r")
        file_content = file_handle.read().splitlines()
        self.setContent(file_content)

    def __str__(self):
        if self.title is not "":
            return(self.title + "\n\n" + self.content)
        else:
            return(self.content)


def createDetailsFile(algo):
    details_path = ALGO_ROOT + "/" + algo.algo_type + \
        "/" + algo.name + "/" + DETAILS_FILENAME
    new_details = open(details_path, "w")
    algo.setDetailsPath(details_path)
    print("Created New Details File for: %s, %s" % (algo.algo_type, algo.name))
    return new_details


def replaceTitle(string, new_value):
    return string.replace(DETAILS_TEMPLATE_TITLE_TOKEN, new_value)


def replaceLanguageBlock(details_file, token_line, algo):

    if len(algo.languages) < 1:
        return token_line.replace(DETAILS_TEMPLATE_LANGUAGE_TOKEN, "No Implementations")

    blocks = []

    for language in algo.languages:

        section_header = '#' * DETAILS_TEMPLATE_LANGUAGE_HLEVEL + " " + language

        if section_header not in details_file:
            # Create a new block if the language isn't in the file

            language_code_block = DETAILS_DEFAULT_CODE_BLOCK.replace(
                DETAILS_TEMPLATE_LANGUAGE_TOKEN, language)

            new_block = Block(section_header, language_code_block)

            if "Pseudo" in language:  # For clarity, ensure Pseudo is at the top
                blocks = [new_block.__str__()] + blocks
            else:
                blocks.append(new_block.__str__())

    block_string = ""

    for block in blocks:
        # If not the last block, pad accordingly
        if block is not blocks[len(blocks) - 1]:
            block_string += block + "\n\n"
        else:
            block_string += block

    return block_string

    # Check if there's anything under the header before the next '#'


file_manager = FileManager()

algo_list = find_all(ALGO_ROOT)

template_file = open(DETAILS_TEMPLATE_FILENAME, "r")
file_manager.addFile(template_file)
template_lines = template_file.read().splitlines()

for algo in algo_list:
    print("Algo Details: %s" % (algo.details_path))
    if algo.details_path is "":
        details_file = createDetailsFile(algo)
        file_manager.addFile(details_file)

        for line in template_lines:
            if DETAILS_TEMPLATE_TITLE_TOKEN in line:
                # Method for replacing Title with Algo Name
                line = replaceTitle(line, algo.name)
            # elif DETAILS_TEMPLATE_CODE_AREA in line:
            elif DETAILS_TEMPLATE_LANGUAGE_TOKEN in line:
                # Method for replacing Language with Blocks
                line = replaceLanguageBlock(template_lines, line, algo)

            if line is not None:
                details_file.write(line + "\n")
    else:
        details_file = open(algo.details_path, "r+")
        file_manager.addFile(details_file)
        # for line in details_file:
        #     print(line + "\n")

file_manager.closeAllFiles()
