from graph.graph_util import GraphManager
from graph.result_util import ResultManager
from object.external_min_heap import ExternalMinHeap
from object.node import Node
import math
import random
import datetime

def dijkstra(graph_id, s):
    g = GraphManager(graph_id)
    r = {}
    pq = ExternalMinHeap(graph_id)

    pq.insert(Node(s, 0))
    r[s] = 0
    while not pq.is_empty():
        min_node = pq.extract_min()
        current_dist = min_node.key
        for neighbour in g.retrieve_neighbour(min_node.id):
            new_dist = current_dist + neighbour[1]
            old_dist = r[neighbour[0]] if neighbour[0] in r else math.inf
            if old_dist == math.inf:
                pq.insert(Node(neighbour[0], new_dist))
                r[neighbour[0]] = new_dist
            elif old_dist > new_dist:
                pq.decrease_key(neighbour[0], new_dist)
                r[neighbour[0]] = new_dist
    return r


source = random.randint(0, 1000)
start = datetime.datetime.now()
print(start)
print(source)
visited = dijkstra(1, source)
print(visited)
print(datetime.datetime.now() - start)
