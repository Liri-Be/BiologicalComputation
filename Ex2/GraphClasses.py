import itertools


# Creating edge class to help with implementation of the Graph class
class Edge:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def __repr__(self):  # "toString"
        return str(self.source) + ' ' + str(self.target)

    def __eq__(self, other):  # check if two edges are equal
        return (self.source, self.target) == (other.get_source(), other.get_target())

    # getters
    def get_source(self):
        return self.source

    def get_target(self):
        return self.target


# Graph class for each of our sub-graphs :)
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def __repr__(self):  # "toString"
        str_graph = ""
        for edge in self.edges:
            str_graph += str(edge) + "\n"
        return str_graph

    def __eq__(self, other):
        """
        Check if two graphs are equal.
        We consider two graphs equal if they have the same nodes and edges (not necessarily in the same order).
        :param other: other graph to compare to
        :type other: Graph
        :return: True if the graphs are equal, False otherwise
        """
        if len(self.nodes) != len(other.get_nodes()) or len(self.edges) != len(other.get_edges()):  # different size
            return False
        for permutation in other.permute_graph():  # check all the permutations of the other graph
            flag = True
            for node in self.nodes:
                if node not in permutation.get_nodes():
                    flag = False
            for edge in self.edges:
                if edge not in permutation.get_edges():
                    flag = False
            if flag:  # if we found a permutation that is equal to self
                return True
        return False

    def permute_graph(self):
        """
        return all the possible permutations of the graph
        :return: list of all the permutations of our graph
        """
        permutations = []
        for permutation in itertools.permutations(self.nodes, len(self.nodes)):
            new_graph = Graph()
            new_graph.nodes = list(permutation)
            # fix the edges according to the permutation
            for edge in self.edges:
                new_edge = Edge(permutation[edge.get_source() - 1], permutation[edge.get_target() - 1])
                new_graph.add_edge(new_edge)
            permutations.append(new_graph)

        return permutations

    # add nodes and edges
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self, edge):
        if edge not in self.edges and edge.get_target() in self.nodes and edge.get_target() in self.nodes:  # can add
            self.edges.append(edge)

    # getters
    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges
