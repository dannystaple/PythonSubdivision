"""
Convert the old style subdiv class file to the new system.
One is a pickle, the new one is a simpler repr."""
import json

import pickle
import sys


class Node:
    def __init__(self):
        self._subNodes = None

    def subDivide(self):
        self._subNodes = [Node(), Node(), Node(), Node()]

    def subNodes(self):
        return self._subNodes

    def clearSubNodes(self):
        self._subNodes = None


class Tree:
    def __init__(self):
        self._root = Node()

    def getRoot(self):
        """Get the tree root"""
        return self._root


def convert(node):
    sn = node.subNodes()
    if sn:
        return [convert(subnode) for subnode in node.subNodes()]
    else:
        return []


def main():
    input_filename, output_filename = sys.argv[1:]
    with open(input_filename) as fd:
        input_data = pickle.load(fd)
    output_data = convert(input_data.getRoot())
    with open(output_filename, "w") as fd:
        fd.write(json.dumps(output_data))

if __name__=="__main__":
    main()