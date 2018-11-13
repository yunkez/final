from graph.file_util import *
from object.node import Node
import os
import glob

PQ_FILE_NAME = 'pq_%s_%s'
BLOCK_SIZE = 1000


class ExternalMinHeap:
    def __init__(self, graph_id):
        self.clean()
        self.count = 0
        self.keys = {}
        self.graph_id = graph_id

    def insert(self, node):
        i = self.count
        self.keys[node.id] = i
        self.store_node(node)
        self.swim(i)

    def is_empty(self):
        return self.count == 0

    def min_heapify(self, parent):
        if not 2 * parent + 1 < self.count:
            return

        if not 2 * parent + 2 < self.count:
            x = 2 * parent + 1
        elif self.retrieve_node(2 * parent + 1).key < self.retrieve_node(2 * parent + 2).key:
            x = 2 * parent + 1
        else:
            x = 2 * parent + 2

        children = self.retrieve_node(x)
        parent = self.retrieve_node(parent)
        if children.key < parent.key:
            self.swap_node(children, parent)
            self.min_heapify(x)

    def extract_min(self):
        min_node = self.retrieve_node(0)
        i = self.count - 1
        last_node = self.retrieve_node(i)
        self.swap_node(min_node, last_node)

        self.keys.pop(min_node.id)
        self.delete_node()

        self.min_heapify(0)
        return min_node

    def swim(self, x):
        while x > 0:
            lower = self.retrieve_node(x)
            upper = self.retrieve_node((x - 1) // 2)
            if not lower.key < upper.key:
                break
            self.swap_node(lower, upper)
            x = (x - 1) // 2

    def decrease_key(self, x, smaller_x):
        i = self.keys[x]
        self.store_node(Node(x, smaller_x), i)
        self.swim(i)

    def swap_node(self, node1, node2):
        index1 = self.keys[node1.id]
        index2 = self.keys[node2.id]
        self.keys[node1.id] = index2
        self.keys[node2.id] = index1
        self.store_node(node1, index2)
        self.store_node(node2, index1)

    def store_node(self, node, pos=None):
        index = int(self.keys[node.id] / BLOCK_SIZE)
        result = read_file(PQ_FILE_NAME % (self.graph_id, index)) or []
        if pos is not None:
            result[pos % BLOCK_SIZE] = node
        else:
            result += [node]
            self.count += 1
        with open('../data/' + PQ_FILE_NAME % (self.graph_id, index), 'wb') as f:
            pickle.dump(result, f)

    def retrieve_node(self, i):
        index = int(i/BLOCK_SIZE)
        node_list = read_file('../data/' + PQ_FILE_NAME % (self.graph_id, index))
        return node_list[i % BLOCK_SIZE]

    def delete_node(self):
        index = int((self.count-1)/BLOCK_SIZE)
        node_list = read_file(PQ_FILE_NAME % (self.graph_id, index))
        node_list.pop()
        self.count -= 1
        with open('../data/' + PQ_FILE_NAME % (self.graph_id, index), 'wb') as f:
            pickle.dump(node_list, f)

    def clean(self):
        for i in sorted(glob.glob("../data/pq_*_*")):
            os.remove(i)
