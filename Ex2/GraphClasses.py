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

    def __hash__(self):
        return hash((self.source, self.target))

    # getters
    def get_source(self):
        return self.source

    def get_target(self):
        return self.target


# Graph class for each of our sub-graphs :)
class Graph:
    def __init__(self, edges=None, size=None):
        if edges is None or size is None:
            self.nodes = []
            self.edges = []
        elif size is not None and edges is None:
            self.nodes = [i for i in range(1, size + 1)]
            self.edges = []
        else:
            self.nodes = [i for i in range(1, size + 1)]
            self.edges = []
            for source, target in edges:
                self.add_edge(Edge(source, target))
        # self.edges = []
        # self.nodes = []

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

        permutations = other.permute_graph()
        for permutation in permutations:  # check all the permutations of the other graph
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
        for permutation in list(itertools.permutations(self.nodes, len(self.nodes))):
            new_graph = Graph()
            new_graph.nodes = list(permutation)
            # fix the edges according to the permutation
            for edge in self.edges:
                new_edge = Edge(permutation[edge.get_source() - 1], permutation[edge.get_target() - 1])
                new_graph.add_edge(new_edge)
            permutations.append(new_graph)

        return permutations

    def is_connected(self):
        visited = [False for _ in range(len(self.nodes))]
        node = self.nodes[0]
        self.dfs(node, visited)
        return all(visited)

    def dfs(self, node, visited):
        visited[node - 1] = True
        for edge in self.edges:
            if edge.get_source() == node and not visited[edge.get_target() - 1]:
                self.dfs(edge.get_target(), visited)
            elif edge.get_target() == node and not visited[edge.get_source() - 1]:
                self.dfs(edge.get_source(), visited)

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
