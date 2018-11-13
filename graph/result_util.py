from graph.graph_builder import BLOCK_SIZE
from graph.file_util import *
import math

RESULT_FILE_NAME = 'result_%s_%s'


class ResultManager:

    def __init__(self, graph_id):
        self.graph_id = graph_id
        self.io_count = 0

    def save_result(self, node, value):
        index = int(node / BLOCK_SIZE)
        result = read_file(RESULT_FILE_NAME % (self.graph_id, index))
        if result:
            result[node] = value
        else:
            with open('../data/' + RESULT_FILE_NAME % (self.graph_id, index), 'wb') as f:
                pickle.dump({node: value}, f)

    def retrieve_result(self, node):
        index = int(node/BLOCK_SIZE)
        result = read_file(RESULT_FILE_NAME % (self.graph_id, index))
        if result and node in result:
            return result[node]
        else:
            return math.inf