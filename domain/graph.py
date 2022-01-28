import copy

from errors.exceptions import GraphError


class Graph:
    def __init__(self, n, m):
        """
        The constructor of a graph with n vertices numbered in a pythonic way from 0 to n-1, and no edges added
        :param n: the number of vertices of type integer
        """
        self.__vertices = n
        self.__edges = m
        self.__edgeOut = {}
        self.__edgeIn = {}
        self.__cost = {}

    def get_nr_vertices(self):
        """
        :return: JUST the number of the vertices
        """
        verts = copy.deepcopy(self.__vertices)
        return verts

    def get_nr_edges(self):
        """
        :return: JUST the number of the edges
        """
        return len(self.__cost.keys())

    def get_vertices(self):
        """
        :return: an iterable with all the vertices of the graph
        """
        return self.__edgeOut.keys()

    def get_n_out(self, v):
        """
        :param v: the vertex of which we want to get all the outbound neighbours
        :return: an iterable with all the outbound neighbours of v
        """
        return copy.deepcopy(self.__edgeOut[v])

    def get_n_in(self, v):
        """
        :param v: the vertex of which we want to get all the inbound neighbours
        :return: an iterable with all the inbound neighbours of v
        """
        return copy.deepcopy(self.__edgeIn[v])

    def get_copy_of_outs(self):
        """:return: a copy of the outbound edge dictionary"""
        return copy.deepcopy(self.__edgeOut)

    def get_copy_of_ins(self):
        """:return: a copy of the inbound edge dictionary"""
        return copy.deepcopy(self.__edgeIn)

    def get_edges(self):
        """
        Method that provides the list of edges in the graph
        :return: an iterable with all the edges
        """
        return copy.deepcopy(self.__cost)

    def get_cost(self, v1, v2):
        """
        Method that returns the cost of the edge from v1 to v2
        :param v1: starting vertex
        :param v2: ending vertex
        :return: the cost from v1 to v2
        """
        pair = (v1, v2)
        return self.__cost[pair]

    def set_cost(self, v1, v2, new_cost):
        """
        Method that sets the NEW cost of the edge from v1 to v2
        :param v1: starting vertex
        :param v2: ending vertex
        :param new_cost: the new cost that will be assigned to edge [v1, v2]
        """
        pair = (v1, v2)
        self.__cost[pair] = new_cost

    def is_edge(self, v1, v2):
        """
        Method that checks if there is an edge from vertex v1 to vertex v2
        :param v1: starting vertex
        :param v2: ending vertex
        :return: True if there is an edge between v1 and v2 or False otherwise
        """
        if v2 in self.__edgeOut[v1]:
            return True
        return False

    def add_double_edge(self, v1, v2, c):
        self.__edges += 1
        pair = (v1, v2)
        self.__edgeOut[v1].append(v2)
        self.__edgeIn[v2].append(v1)
        self.__cost[pair] = c

    def add_edge(self, v1, v2, c):
        """
        Method that adds an edge from vertex v1 to vertex v2 if and only if there is no edge between v1 and v2
        :param v1: starting vertex
        :param v2: ending vertex
        :param c: the cost from v1 to v2
        :return:
                - true: if the adding was successful
                - false: otherwise
        """
        self.__edges += 1
        pair = (v1, v2)
        if pair not in self.__cost.keys():
            self.__edgeOut[v1].append(v2)
            self.__edgeIn[v2].append(v1)
            self.__cost[pair] = c
            if pair in self.__cost.keys() and \
                    v1 in self.__edgeIn[v2] and \
                    v2 in self.__edgeOut[v1]:
                return True
            return False
        else:
            raise GraphError("Edge already exists!")

    def remove_edge(self, v1, v2):
        """
        Method that removes a specific edge that starts in the vertex v1 and ends in v2
        :param v1: starting vertex
        :param v2: ending vertex
        :return:
                - true: if the removing was successful
                - false: otherwise
        """
        self.__edges -= 1
        pair = (v1, v2)
        v1_succs = self.__edgeOut[v1]
        v2_preds = self.__edgeIn[v2]
        v1_succs.remove(v2)
        v2_preds.remove(v1)
        self.__cost.pop(pair)
        if pair not in self.__cost.keys() and \
                v1 not in self.__edgeIn[v2] and \
                v2 not in self.__edgeOut[v1]:
            return True
        return False

    def add_vertex(self, v1):
        """
        Method that adds to the graph a new vertex
        :param v1: the new vertex that will be added
        """
        self.__vertices += 1
        self.__edgeOut[v1] = []
        self.__edgeIn[v1] = []

    def remove_vertex(self, v1):
        """
        Method that removes a vertex along side with all it's connected edges
        :param v1: the to-be-removed vertex
        """
        self.__vertices -= 1
        for out_v in self.__edgeOut[v1]:
            pair = (v1, out_v)
            self.__cost.pop(pair)
        self.__edgeOut.pop(v1)
        for v in self.__edgeIn[v1]:
            pair = (v, v1)
            self.__cost.pop(pair)
            self.__edgeOut[v].remove(v1)
        self.__edgeIn.pop(v1)

    def set_n_out(self, out_neighbours):
        """
        Method that replaces graph's current dictionary of out-bound neighbours with a new one
        :param out_neighbours: the new dictionary of out-neighbours (copied from another graph)
        """
        self.__edgeOut = out_neighbours

    def set_n_in(self, in_neighbours):
        """
        Method that replaces graph's current dictionary of in-bound neighbours with a new one
        :param in_neighbours: the new dictionary of in-neighbours (copied from another graph)
        """
        self.__edgeIn = in_neighbours

    def set_costs(self, new_costs):
        """
        Method that replaces graph's current dictionary of costs with a new one
        :param new_costs: the new dictionary of edge-costs (copied from another graph)
        """
        self.__cost = new_costs

    def set_nr_vertices(self, new_verts):
        """
        Method that replaces graph's current nr of vertices with a new one
        :param new_verts: the new number of vertices (copied from another graph)
        """
        self.__vertices = new_verts

    def set_nr_edges(self, new_edges):
        """
        Method that replaces graph's current nr of edges with a new one
        :param new_edges: the new number of edges (copied from another graph)
        """
        self.__edges = new_edges

    def breadth_first_traversal(self, start, visited):
        """
        Method that simply traverses the graph in a BF manner
        :param start: starting vertex
        :param visited: the already visited nodes, in order to not visit the same vertex twice
        :return: the list of edges of the connected component and the list of vertices
        """
        q = []
        acc = []
        q.append(start)
        visited.append(start)
        acc.append(start)
        cost_fake = {}
        while len(q) > 0:
            x = q.pop(0)
            for i in self.__edgeOut[x]:
                pair1 = (x, i)
                pair2 = (i, x)
                cost_fake[pair1] = self.get_cost(x, i)
                cost_fake[pair2] = self.get_cost(x, i)
                if i not in visited:
                    visited.append(i)
                    acc.append(i)
                    q.append(i)
        return cost_fake, acc

