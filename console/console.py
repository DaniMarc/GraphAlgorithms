from errors.exceptions import GraphError


class Console:
    def __init__(self, service):
        self.__srv = service
        self.__command_list = {1: self.__get_vertices_ui,
                               2: self.__parse_vertices_ui,
                               3: self.__check_if_edge_ui,
                               4: self.__get_degrees_ui,
                               5: self.__get_outbound_edges_ui,
                               6: self.__get_inbound_edges_ui,
                               7: self.__get_cost_edge_ui,
                               8: self.__set_cost_edge_ui,
                               9: self.__add_edge_ui,
                               10: self.__remove_edge_ui,
                               11: self.__add_vertex_ui,
                               12: self.__remove_vertex_ui,
                               13: self.__create_copy_ui,
                               14: self.__overwrite_main_graph_ui,
                               15: self.__find_connected_components_ui,
                               16: self.__find_shortest_path_ui,
                               17: self.__find_minimum_spanning_tree_ui,
                               18: self.__find_hamiltonian_path_ui,
                               }

    def __find_hamiltonian_path_ui(self, gi):
        start_vertex = int(input("Introduce the starting vertex:\n"))
        # Applying Prim's algorithm to find the MST
        edges, total_cost = self.__srv.prim_algorithm(gi, start_vertex)
        edges = list(edges)
        # Creating a 100% Eulerian graph
        self.__srv.create_graph_from_list(edges, gi+1)
        # Applying the algorithm to find an Eulerian tour
        euler_path = self.__srv.find_euler_tour(start_vertex, gi+1)
        # Printing the result
        for v in euler_path:
            print(str(v)+" ", end="")
        print(start_vertex, end="")
        self.__srv.delete_graph(gi+1)

    def __find_minimum_spanning_tree_ui(self, gi):
        start_vertex = int(input("Introduce the starting vertex:\n"))
        edges, total_cost = self.__srv.prim_algorithm(gi, start_vertex)
        if len(edges) != 0:
            print("The minimum spanning tree starting from vertex "+str(start_vertex)+" is the following:")
            print(sorted(edges), end=" ")
            print(" and has the cost of "+str(total_cost)+".\n")
        else:
            print("Could not build such a tree!\n")

    def __find_shortest_path_ui(self, gi):
        start_vertex = int(input("Introduce the starting vertex:"))
        end_vertex = int(input("Introduce the ending vertex:"))
        dist, next_verticies = self.__srv.dijkstra_algorithm(gi, end_vertex, start_vertex)
        if len(dist) != 1:
            print("\n>>>The cost from the vertex "+str(start_vertex)+" and the vertex "+str(end_vertex)+" is "+str(dist[start_vertex])+".")
            print("•A path between these two vertices is the following:")
            print("•Starting from vertex "+str(start_vertex)+"...")
            current_vertex = start_vertex
            while current_vertex != end_vertex:
                print("\tnext["+str(current_vertex)+"] = "+str(next_verticies[current_vertex])+";", end="")
                current_vertex = next_verticies[current_vertex]
            print("...and here, we end our journey, in vertex "+str(end_vertex)+".")
        else:
            print("There could not be found any walk from vertex "+str(start_vertex)+" to vertex "+str(end_vertex)+"!\n")

    def __find_connected_components_ui(self, gi):
        print("Starting the traversal...\n")
        self.__srv.bfs_components(gi)
        print("Traversal completed. You may now see the connected components as separate graphs!\n")

    def __overwrite_main_graph_ui(self, gi):
        while True:
            choice = input("Are you SURE you want to overwrite the main graph? This will change all its data with the "
                           "current graph's data!(Y/N)\n")
            if choice.lower() == "y":
                self.__srv.overwrite_main_graph(gi)
                print("Overwritten completed successfully!\n")
                return
            elif choice.lower() == "n":
                print("No changes will be done!\n")
                return
            else:
                print("That ain't an option!")

    def __create_copy_ui(self, gi):
        print("Creating a copy for the " + str(gi) + " graph...\n")
        self.__srv.create_copy(gi)

    def __remove_vertex_ui(self, gi):
        v1 = int(input("\n>>>Introduce the desired vertex: "))
        keys = self.__srv.get_vertices(gi)
        if v1 in keys:
            self.__srv.remove_vertex(v1, gi)
            print("Vertex removed successfully\n")
        else:
            raise GraphError("Nonexistent vertex!")

    def __add_vertex_ui(self, gi):
        v1 = int(input("\n>>>Introduce the desired vertex: "))
        keys = self.__srv.get_vertices(gi)
        if v1 not in keys:
            self.__srv.add_new_vertex(v1, gi)
            print("Vertex added successfully\n")
        else:
            raise GraphError("Vertex already exists!")

    def __remove_edge_ui(self, gi):
        v1 = int(input("\n>>>Introduce the starting vertex: "))
        v2 = int(input("\n>>>Introduce the ending vertex: "))
        keys = self.__srv.get_vertices(gi)
        if v1 in keys and v2 in keys:
            if self.__srv.check_if_edge(v1, v2, gi):
                status = self.__srv.remove_an_edge(v1, v2, gi)
                if status:
                    print("\nEdge removed successfully!")
                else:
                    print("\nFailed removing the edge!")
            else:
                raise GraphError("Nonexistent edge!\n")
        else:
            raise GraphError("Nonexistent vertex!\n")

    def __add_edge_ui(self, gi):
        v1 = int(input("\n>>>Introduce the starting vertex: "))
        v2 = int(input("\n>>>Introduce the ending vertex: "))
        cost = int(input("\n>>>Introduce the cost of the edge: "))
        keys = self.__srv.get_vertices(gi)
        if v1 in keys and v2 in keys:
            if not self.__srv.check_if_edge(v1, v2, gi):
                status = self.__srv.add_new_edge(v1, v2, cost, gi)
                if status:
                    print("\nEdge added successfully!")
                else:
                    print("\nFailed adding the edge!")
            else:
                raise GraphError("Already existing edge!")
        else:
            raise GraphError("Nonexistent vertex!")

    def __set_cost_edge_ui(self, gi):
        v1 = int(input("\n>>>Introduce the first desired vertex: "))
        v2 = int(input("\n>>>Introduce the second desired vertex: "))
        new_cost = int(input("\n>>>Introduce the new cost of the edge: "))
        keys = self.__srv.get_vertices(gi)
        if v1 in keys and v2 in keys:
            if self.__srv.check_if_edge(v1, v2, gi):
                self.__srv.set_cost_of_edge(v1, v2, new_cost, gi)
                print("The cost of the edge [" + str(v1) + ", " + str(v2) + "] " + "is now: " + str(new_cost))
            else:
                GraphError("Nonexistent edge! You need to add it first to the graph!")
        else:
            raise GraphError("Nonexistent vertex!")

    def __get_cost_edge_ui(self, gi):
        v1 = int(input("\n>>>Introduce the first desired vertex: "))
        v2 = int(input("\n>>>Introduce the second desired vertex: "))
        keys = self.__srv.get_vertices(gi)
        if v1 in keys and v2 in keys:
            if self.__srv.check_if_edge(v1, v2, gi):
                cost = self.__srv.get_cost_of_edge(v1, v2, gi)
                print("The cost of the edge [" + str(v1) + ", " + str(v2) + "] " + "is: " + str(cost))
            else:
                raise GraphError("Nonexistent edge!")
        else:
            raise GraphError("Nonexistent vertex!")

    def __get_inbound_edges_ui(self, gi):
        v1 = int(input("\n>>>Introduce the desired vertex: "))
        keys = self.__srv.get_vertices(gi)
        if v1 in keys:
            edges = self.__srv.get_inbound_edges(v1, gi)
            if len(edges) > 0:
                for e in edges:
                    print("The edge from vertex " + str(e[0]) + " to vertex " + str(e[1]) + " has the cost " + str(
                        edges[e]))
            else:
                print("No inbound edges to this vertex!")
        else:
            raise GraphError("Nonexistent vertex!")

    def __get_outbound_edges_ui(self, gi):
        v1 = int(input("\n>>>Introduce the desired vertex: "))
        keys = self.__srv.get_vertices(gi)
        if v1 in keys:
            edges = self.__srv.get_outbound_edges(v1, gi)
            if len(edges) > 0:
                for e in edges:
                    print("The edge from vertex " + str(e[0]) + " to vertex " + str(e[1]) + " has the cost " + str(
                        edges[e]))
            else:
                print("No outbound edges from this vertex!")
        else:
            raise GraphError("Nonexistent vertex!")

    def __get_degrees_ui(self, gi):
        v1 = int(input("\n>>>Introduce the desired vertex: "))
        keys = self.__srv.get_vertices(gi)
        if v1 in keys:
            in_degree = self.__srv.get_in_degree(v1, gi)
            out_degree = self.__srv.get_out_degree(v1, gi)
            print("The vertex " + str(v1) + " has an IN degree of " + str(in_degree) + " and an OUT degree of " + str(
                out_degree))
        else:
            raise GraphError("Nonexistent vertex!")

    def __check_if_edge_ui(self, gi):
        v1 = int(input("\n>>>Introduce the first vertex: "))
        v2 = int(input("\n>>>Introduce the second vertex: "))
        keys = self.__srv.get_vertices(gi)
        if v1 in keys and v2 in keys:
            edge = self.__srv.check_if_edge(v1, v2, gi)
            if edge:
                cost = self.__srv.get_cost_of_edge(v1, v2, gi)
                print("\nThere is an edge between " + str(v1) + " and " + str(v2) + " and has the cost of " + str(cost))
            else:
                print("\nThere is no edge between " + str(v1) + " and " + str(v2) + "!")
        else:
            raise GraphError("Nonexistent vertices!")

    def __parse_vertices_ui(self, gi):
        keys = self.__srv.get_vertices(gi)
        print("\n>>>The vertices are as it follows: ")
        index = 0
        for k in sorted(keys):
            if index == 35:
                print("\n")
                index = 0
            index += 1
            print(str(k) + ";", end=" ")
        print("\n")

    def __get_vertices_ui(self, gi):
        print("\n>>>The number of vertices in the program is: " + str(self.__srv.get_nr_vertices(gi)) + "\n")

    def __print_menu(self):
        commands = ["\n"
                    "1.  Print the number of vertices.",
                    "2.  Parse the set of vertices.",
                    "3.  Check if between two vertices is an edge or not.",
                    "4.  Get the IN degree and the OUT degree of a vertex.",
                    "5.  Get the set of OUT-bound edges of a specified vertex.",
                    "6.  Get the set of IN-bound edges of a specified vertex.",
                    "7.  Get the cost of an edge.",
                    "8.  Change the cost of an edge.",
                    "9.  Add a new edge.",
                    "10. Remove an edge.",
                    "11. Add a new vertex.",
                    "12. Remove a vertex.",
                    "13. Create a new copy.",
                    "14. Overwrite the main graph",
                    "15. Find the connected components (Breath First Traversal)",
                    "16. Find the shortest path between two vertices (Reverse Dijkstra Algorithm - must be DIRECTED)",
                    "17. Find the minimum spanning tree (Prim's Algorithm - must be UNDIRECTED)",
                    "18. Find a Hamiltonian cycle of no more than twice the minimum cost",
                    "0. Exit the current graph.",
                    "\n"]
        for com in commands:
            print(com)

    def __read_graph_index(self):
        command = input("\n>>>Choose the index of the graph you want to perform operations on: ")
        if command != "exit":
            graph_index = int(command)
            return graph_index
        return command

    def __new_graph_menu(self):
        nr_graphs = self.__srv.get_nr_graphs()
        while True:
            print(">>>Currently you have " + str(nr_graphs) + " graphs in the application.")
            print(">>>In order to exit the app just type: exit")
            for i in range(nr_graphs):
                print(str(i) + ";", end=" ")
            graph_index = self.__read_graph_index()
            if type(graph_index) == int and graph_index >= nr_graphs:
                print("Bad input! Choose a displayed number!")
            else:
                return graph_index

    def run(self):
        done = False
        while not done:
            graph_index = self.__new_graph_menu()
            if graph_index == "exit":
                return
            else:
                while not done:
                    self.__print_menu()
                    try:
                        command = int(input("Your command (pick a number): "))
                        if command == 0:
                            print("\nExiting current graph ...")
                            break
                        else:
                            self.__command_list[command](graph_index)
                    except ValueError as ve:
                        print("\t\n***Invalid command! Pick a number!***\n")
                    except KeyError as ke:
                        print("\t\n***" + str(ke) + "***\n")
                    except GraphError as ge:
                        print("\t\n***" + str(ge) + "***\n")
