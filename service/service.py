from copy import deepcopy

from domain.PriorityQueue import PriorityQueue
from domain.graph import Graph


class Service:
    def __init__(self):
        """
        The constructor for the service class which initialises an empty list representing the list of all graphs in the
        memory at run-time
        """
        self.__graph_list = []

    def get_nr_graphs(self):
        """ Method that returns the number of graph currently in memory"""
        return len(self.__graph_list)

    def add_graph(self, graph):
        """ Method that adds a new graph in the memory - the added graph is a copy of an existing one"""
        self.__graph_list.append(graph)

    def get_nr_vertices(self, gi):
        """ Method that returns the total number of vertices in the graph
        :param gi: the index of the graph that we perform operations on
        """
        return self.__graph_list[gi].get_nr_vertices()

    def get_vertices(self, gi):
        """ Method that returns the vertices in the graph
        :param gi: the index of the graph that we perform operations on
        """
        return self.__graph_list[gi].get_vertices()

    def check_if_edge(self, v1, v2, gi):
        """ Method that checks if between 2 vertices is an edge or not
        :param v1: starting vertex
        :param v2: ending vertex
        :param gi: the index of the graph that we perform operations on
        :return: true if there is the edge [v1, v2] or false otherwise
        """
        return self.__graph_list[gi].is_edge(v1, v2)

    def get_cost_of_edge(self, v1, v2, gi):
        """ Method that gets the cost of an edge
        :param v1: starting vertex
        :param v2: ending vertex
        :param gi: the index of the graph that we perform operations on
        :return: the cost of the edge [v1, v2]
        """
        return self.__graph_list[gi].get_cost(v1, v2)

    def set_cost_of_edge(self, v1, v2, new_cost, gi):
        """ Method that sets the cost of an edge
        :param v1: starting vertex
        :param v2: ending vertex
        :param new_cost: the new cost of the edge [v1, v2]
        :param gi: the index of the graph that we perform operations on
        """
        self.__graph_list[gi].set_cost(v1, v2, new_cost)

    def get_in_degree(self, v1, gi):
        """ Method that gets the degree of IN-bound edges of a vertex
        :param v1: the vertex from which we need the degree IN
        :param gi: the index of the graph that we perform operations on
        :return: the degree of IN-bound edges of vertex v1
        """
        return len(self.__graph_list[gi].get_n_in(v1))

    def get_out_degree(self, v1, gi):
        """ Method that gets the degree of OUT-bound edges of a vertex
        :param v1: the vertex from which we need the degree OUT
        :param gi: the index of the graph that we perform operations on
        :return: the degree of OUT-bound edges of vertex v1
        """
        return len(self.__graph_list[gi].get_n_out(v1))

    def get_n_out(self, v1, gi):  #
        """ Method that gets the OUT-bound edges of a vertex
        :param v1: the vertex from which we need the OUT edges
        :param gi: the index of the graph that we perform operations on
        :return: the list of OUT-bound edges of vertex v1
        """
        return self.__graph_list[gi].get_n_out(v1)

    def get_outbound_edges(self, v1, gi):
        """ Method that gets the OUT-bound edges of a vertex
        :param v1: the vertex from which we need the OUT edges
        :param gi: the index of the graph that we perform operations on
        :return: the list of OUT-bound edges of vertex v1 along with the cost
        """
        out_neighs = self.__graph_list[gi].get_n_out(v1)
        edges = self.__graph_list[gi].get_edges()
        out_edges = {}
        for v in out_neighs:
            pair = (v1, v)
            if pair in edges:
                out_edges[pair] = edges[pair]
        return out_edges

    def get_inbound_edges(self, v1, gi):
        """ Method that gets the IN-bound edges of a vertex
        :param v1: the vertex from which we need the IN edges
        :param gi: the index of the graph that we perform operations on
        :return: the list of IN-bound edges of vertex v1 along with the cost
        """
        in_neighs = self.__graph_list[gi].get_n_in(v1)
        edges = self.__graph_list[gi].get_edges()
        in_edges = {}
        for v in in_neighs:
            pair = (v, v1)
            if pair in edges:
                in_edges[pair] = edges[pair]
        return in_edges

    def add_new_edge(self, v1, v2, cost, gi):
        """ Method that adds a new edge in the graph
        :param v1: the starting vertex
        :param v2: the ending vertex
        :param cost: the cost of the vertex [v1, v2]
        :param gi: the index of the graph that we perform operations on
        """
        return self.__graph_list[gi].add_edge(v1, v2, cost)

    def remove_an_edge(self, v1, v2, gi):
        """ Method that removes an edge from the graph
        :param v1: the starting vertex
        :param v2: the ending vertex
        :param gi: the index of the graph that we perform operations on
        """
        return self.__graph_list[gi].remove_edge(v1, v2)

    def add_new_vertex(self, v1, gi):
        """ Method that adds a new vertex in the graph
        :param v1: the to be added vertex
        :param gi: the index of the graph that we perform operations on
        """
        self.__graph_list[gi].add_vertex(v1)

    def remove_vertex(self, v1, gi):
        """ Method that removes a vertex from the graph
        :param v1: the to be removed vertex
        :param gi: the index of the graph that we perform operations on
        """
        self.__graph_list[gi].remove_vertex(v1)

    def create_copy(self, gi):
        """ Method that copies the current graph represented by its index 'gi'
        :param gi: the index of the graph that we perform operations on
        :return: graph_list' = graph_list + {copied graph}
        """
        copy_nr_verts = self.__graph_list[gi].get_nr_vertices()
        copy_nr_edges = self.__graph_list[gi].get_nr_edges()

        copy_graph = Graph(copy_nr_verts, copy_nr_edges)

        copy_outs = self.__graph_list[gi].get_copy_of_outs()
        copy_ins = self.__graph_list[gi].get_copy_of_ins()
        copy_costs = self.__graph_list[gi].get_edges()

        copy_graph.set_n_out(copy_outs)
        copy_graph.set_n_in(copy_ins)
        copy_graph.set_costs(copy_costs)

        self.__graph_list.append(copy_graph)

    def overwrite_main_graph(self, gi):
        """ Method that overwrites the original graph with the current graph represented by its index 'gi'
        :param gi: the index of the graph that we perform operations on
        :return: main graph' (pos 0) = current graph (pos gi)
        """
        copy_nr_verts = self.__graph_list[gi].get_nr_vertices()
        copy_nr_edges = self.__graph_list[gi].get_nr_edges()
        copy_outs = self.__graph_list[gi].get_copy_of_outs()
        copy_ins = self.__graph_list[gi].get_copy_of_ins()
        copy_costs = self.__graph_list[gi].get_edges()

        self.__graph_list[0].set_nr_vertices(copy_nr_verts)
        self.__graph_list[0].set_nr_edges(copy_nr_edges)
        self.__graph_list[0].set_n_out(copy_outs)
        self.__graph_list[0].set_n_in(copy_ins)
        self.__graph_list[0].set_costs(copy_costs)

    def create_graph_from_list(self, edges, ngi):
        """Method that creates a new editable MST from the list of edges"""
        new_graph = Graph(0, 0)
        self.__graph_list.append(new_graph)
        for edge in edges:
            vertex1 = edge[0]
            vertex2 = edge[1]
            cost = self.get_cost_of_edge(vertex1, vertex2, ngi-1)
            if vertex1 not in self.get_vertices(ngi):
                self.__graph_list[ngi].add_vertex(vertex1)
            if vertex2 not in self.get_vertices(ngi):
                self.__graph_list[ngi].add_vertex(vertex2)
            self.__graph_list[ngi].add_edge(vertex1, vertex2, cost)       # since we apply the Double-tree approximation
            self.__graph_list[ngi].add_edge(vertex2, vertex1, cost)       # algorithm we have to double our edges and it
            self.__graph_list[ngi].add_double_edge(vertex1, vertex2, cost)  # results in having an Eulerian multi-graph
            self.__graph_list[ngi].add_double_edge(vertex2, vertex1, cost)  # since we have 0 vertices with odd degrees
                                                                            # and it's connected
            # since the edges are duplicated from the minimum spanning tree, the Eulerian tour has cost at most 2, OPT
            # where OPT is the value of the optimal solution

    def find_eluer_tour(self, start_vertex, gi):
        """Method that creates an Eulerian path starting from a given vertex"""
        st = [start_vertex]
        answer = set()
        vertices_grades = {}
        for vert in self.__graph_list[gi].get_vertices():
            vertices_grades[vert] = int(len(self.__graph_list[gi].get_n_out(vert)) / 2)     # we have to keep track of
                                                                                            # how many vertices the
        visited = []                                                                        # original graph had
        # we are iterating through the vertices and start removing edge by edge until we are left with
        while st:
            some_vertex = st.pop()
            if self.get_out_degree(some_vertex, gi) == vertices_grades[some_vertex]:
                answer.add(some_vertex)
            else:
                # here we start shortcutting
                # By the triangle inequality, the cost of the shortcut tour is at most the cost of the Eulerian tour,
                # which is not greater than 2,OPT
                for v in self.__graph_list[gi].get_n_out(some_vertex):
                    if v not in visited:
                        removed_vertex = deepcopy(v)
                        self.__graph_list[gi].remove_edge(some_vertex, removed_vertex)
                        self.__graph_list[gi].remove_edge(removed_vertex, some_vertex)
                        st.append(removed_vertex)
                        visited.append(removed_vertex)
        return list(answer)

    def bfs_components(self, gi):
        """ Method that traverses the current graph represented by its index 'gi' in a breadth first manner
        :param gi: the index of the graph that we perform the traversal on
        The Method will create new instances of the class Graph which will be appended to the graph list
        with every new instance being a connected component
        """
        index = gi + 1

        new_graph = Graph(0, 0)
        self.__graph_list.append(new_graph)

        vertices = self.__graph_list[gi].get_vertices()
        visited = []
        for vertex in vertices:
            if vertex not in visited:
                # creating the connected component
                edges, acc = self.__graph_list[gi].breadth_first_traversal(vertex, visited)
                print("Component number " + str(index) + ":\n{ ", end=" ")
                # adding the vertices
                for v in acc:
                    self.__graph_list[index].add_vertex(v)
                    print(str(v) + " ", end=" ")
                # adding the edges
                print("}; \nWith the edges { ", end=" ")
                for k in edges:
                    self.__graph_list[index].add_edge(k[0], k[1], edges[k])
                    print(str(k) + " ", end=" ")
                print("}\n")

                # making room for a new component if necessary
                if len(edges) != 0:
                    index += 1
                    new_graph = Graph(0, 0)
                    self.__graph_list.append(new_graph)

    def dijkstra_algorithm(self, gi, end_v, start_v):
        """
        Method that computes the shortest path between the starting vertex and the
        ending vertex in an oriented weighted graph using the 'Greedy Algorithm' of Edsger Dijkstra
        but is applied in reverse (we start at the end and make our way through until the start
        using the IN-bound neighbours)
        :param gi: the index of the graph that we perform the search on
        :param end_v: the ending vertex (the starting one in our case because of the reverse)
        :param start_v: the starting vertex (the ending one in our case because of the reverse)
        :return: 2 dictionaries containing:
                - dist = {the dictionary with the minimal distance from the vertex end_v to that specific vertex}
                - next_vertices = {the dictionary with the next-neighbour from the vertex end_v to that specific vertex}
        """
        found = False
        next_vertices = {}  # the dictionary containing the vertices that follow a specific vertex
        q = PriorityQueue()
        q.add(end_v, 0)     # we define the priority of the 1st vertex as being 0, since it starts the parsing
        dist = {end_v: 0}   # a dictionary containing the vertices and the shortest length path that leads to them
        visited = set()     # a set holding the already visited vertices
        visited.add(end_v)
        while not q.is_empty() and not found:
            x = q.pop()
            for y in self.__graph_list[gi].get_n_in(x):     # since it is reversed-dijkstra we parse the IN-neighbours
                # check the shortest cost
                if y not in visited or dist[x] + self.__graph_list[gi].get_cost(y, x) < dist[y]:
                    dist[y] = dist[x] + self.__graph_list[gi].get_cost(y, x)
                    visited.add(y)
                    q.add(y, dist[y])
                    next_vertices[y] = x
            if x == start_v:        # stopping the algorithm once we arrive on the destination vertex because we are
                found = True        # guaranteed to have found the best path to get here, from the end vertex
        return dist, next_vertices  # return the dictionaries with the distance between end_v and all the vertices and
                                    # the "linked" vertices

    def prim_algorithm(self, gi, start_vertex):
        """
            Method that computes and creates a minimum spanning tree using Prim's algorithm in a greedy manner
            based on an undirected weighted graph in O(E*logV) where E = total nr of edges, V = total number of vertices
        :param gi: the index of the graph that we perform the search on
        :param start_vertex: the starting vertex
        :return:
                - edges: a list of all the edges of the MST in the finding order
                - total_cost: the total cost of the MST (the sum of the edge's costs)
        """
        q = PriorityQueue()
        total_cost = 0
        prev = {}
        dist = {}  #the dictionary which holds on position i the total distance from the starting vertex to the vertex i
        edges = set()   #the set that holds the edges of the MST
        s = start_vertex    #the starting vertex
        visited = set()     #the set which holds the already visited vertices
        visited.add(s)      #the tree is initially just the starting vertex
        for vertex in self.__graph_list[gi].get_n_out(s):               #we add to the priority queue all the neighbours
            dist[vertex] = self.__graph_list[gi].get_cost(vertex, s)    #of the starting vertex in order to get the
            prev[vertex] = s                                            #algorithm started
            q.add(vertex, dist[vertex])

        while not q.is_empty():             #while we got vertices to check
            x = q.pop()                     #we extract one by one
            if x not in visited:            #and if we have not visited it before
                edges.add((prev[x], x))     #we add to the tree the edge from it to its previous
                total_cost = total_cost + self.__graph_list[gi].get_cost(x, prev[x])    #compute the total cost
                visited.add(x)              #we mark the vertex as being visited
                for y in self.__graph_list[gi].get_n_out(x):    #we check now for its neighbours
                    if y not in dist.keys() or self.__graph_list[gi].get_cost(x, y) < dist[y]:
                        dist[y] = self.__graph_list[gi].get_cost(x, y)      #and take the minimum cost edge
                        q.add(y, dist[y])                                   #and add it to the MST
                        prev[y] = x

        return edges, total_cost

    def find_euler_tour(self, start_vertex, gi):
        answer = {start_vertex: []}
        stack = [start_vertex]
        while len(stack) > 0:
            x = stack.pop()
            for y in self.__graph_list[gi].get_n_out(x):
                if y not in answer.keys():
                    answer[x].append(y)
                    answer[y] = []
                    stack.append(y)
        return answer

    def delete_graph(self, gi):
        self.__graph_list.pop()