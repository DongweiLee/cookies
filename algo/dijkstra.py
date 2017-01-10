import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.id == other.id

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def __hash__(self):
        return hash(self.id)

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        if self.adjacent.has_key(neighbor):
            return self.adjacent[neighbor]
        else:
            return None

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def shortest(self):
        ''' make shortest '''
        if self.previous:
            return self.previous.shortest() + [self.id]
        else:
            return [self.id]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def __str__(self):
        graph_desc=''
        for v in self.vert_dict.values():
            for w in v.get_connections():
                graph_desc+='( %s , %s, %3d)\n'  % ( v.get_id(), w.get_id(), v.get_weight(w))
        return graph_desc

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

    def add_undirected_edge(self, frm, to, cost = 0):
        self.add_edge(frm, to, cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

import heapq

def dijkstra(aGraph, start):
    print '''Dijkstra's shortest path'''
    unvisited_queue = [v for v in aGraph]
    # Set the distance for the start node to zero
    start.set_distance(0)

    while len(unvisited_queue):
        current=heapq.nsmallest(1,unvisited_queue,key= lambda v: v.get_distance())[0]
        current.set_visited()
        unvisited_queue = list(set(unvisited_queue)-set([current]))

        #for next in v.adjacent:
        for next in current.adjacent:
            if not next.visited:
                new_dist = current.get_distance() + current.get_weight(next)
                #print 'current = %s next = %s old_dist=%s new_dist = %s'%(current.get_id(), next.get_id(), next.get_distance(), new_dist)
                if new_dist < next.get_distance():
                    next.set_distance(new_dist)
                    next.set_previous(current)
                    #print 'updated'

if __name__ == '__main__':

    g = Graph()
    g.add_undirected_edge('a','b',6)
    g.add_undirected_edge('a','c',3)
    g.add_undirected_edge('b','c',2)
    g.add_undirected_edge('b','d',5)
    g.add_undirected_edge('c','d',3)
    g.add_undirected_edge('c','e',4)
    g.add_undirected_edge('d','e',2)
    g.add_undirected_edge('d','f',3)
    g.add_undirected_edge('e','f',5)
    print(g)

    dijkstra(g, g.get_vertex('a'))

    for vertex in g:
        print 'The shortest path : %s %d' %(vertex.shortest(), vertex.get_distance())
