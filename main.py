
from Graph_Types.adjacency_list import AdjacencyList
from Graph_Types.adjacency_matrix import AdjacencyMatrix
from Graph_Types.unweighted_graph import UnweightedGraph
from Graph_Types.weighted_graph import WeightedGraph
from Graph_Algorithms.shortest_paths import ShortestPaths
from Graph_Algorithms.minimum_spanning_trees import MSTs
from Graph_Algorithms.cycles import Cycles
from Graph_Algorithms.traversals import Traversals
from Graph_Algorithms.cuts import Cuts
from Graph_Util.conversions import Conversions
from Graph_Util.util import Util
from copy import deepcopy

import os
import sys

import tkinter as tk

def main():
    base = tk.Tk()

    for row in range(100):
        for col in range(100):
            tk.Label(base).grid()


if __name__ == "__main__":
    main()