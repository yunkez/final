from graph.graph_builder import BLOCK_SIZE, GRAPH_FILE_NAME
from graph.file_util import *


class GraphManager:

    def __init__(self, graph_id):
        self.graph_id = graph_id
        self.io_count = 0

    def retrieve_neighbour(self, node):
        index = int(node/BLOCK_SIZE)
        subgraph = read_file(GRAPH_FILE_NAME % (self.graph_id, index))
        return subgraph[node]

# g = GraphManager(1)
# print(g.retrieve_neighbour(514))