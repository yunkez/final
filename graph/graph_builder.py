from collections import defaultdict
import random
import os
import pickle

BLOCK_SIZE = 1000
GRAPH_FILE_NAME = 'graph_%s_%s'


def generate_random_graph(n=10000, degree=4, max_weight=10):
    file = open('../data/random_weighted_graph.txt', 'w')
    file.truncate()
    m = 0
    for i in range(n):
        for d in range(degree-random.randint(-degree/2, degree/2)):
            neighbour = random.randint(0, n-1)
            file.write('%s %s %s\n' % (i, neighbour, random.randint(1, max_weight)))
            m += 1
    file.close()
    filename = '../data/random_weighted_graph_n%s_m%s.txt' % (n, m)
    os.rename('../data/random_weighted_graph.txt', filename)
    return filename


def build_graph(filename='graph_1.txt'):
    g = defaultdict(list)
    file = open('../data/' + filename, 'r')
    for line in file:
        pair_and_weights = line.split()
        g[int(pair_and_weights[0])].append((int(pair_and_weights[1]),int(pair_and_weights[2])))
    return g


def preprocess(filename=None):
    graph = build_graph(filename)
    graph_node = sorted(graph.keys(), key=lambda x: int(x))
    index = 0
    while (index * BLOCK_SIZE) < len(graph_node):
        subgraph = defaultdict(list)
        for node in graph_node[index * BLOCK_SIZE : (index + 1) * BLOCK_SIZE]:
            subgraph[node] = graph[node]
        with open('../data/' + GRAPH_FILE_NAME % (1, index), 'wb') as f:
            pickle.dump(subgraph, f)
        index += 1

# filename = generate_random_graph()
# preprocess('random_weighted_graph_n10000_m40001.txt')
# preprocess(filename)
# print(filename)