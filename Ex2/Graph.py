import itertools
import time


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


# find all connected graphs of size "size"
def printAllConnectedGraphs(size):
    """
    driver function for createConnectedGraphs - prints the graphs and their count
    :param size: the size of the graphs we want to create
    :return: None
    """
    graphs = createConnectedGraphs(size)
    print(f"Size = {size}")
    print(f"Count = {len(graphs)}")
    for idx, graph in enumerate(graphs):
        print(f"#{idx + 1}")
        print(graph)


def createConnectedGraphs(size):
    """
    create all connected graphs of size "size"
    :param size: the size of the graphs we want to create
    :return: list of all the connected graphs of size "size"
    """
    if size == 1:  # base case - create a graph with one node
        graph = Graph()
        graph.add_node(1)
        return [graph]

    graphs = createConnectedGraphs(size - 1)  # recursive call - we can build our graph from a smaller graph

    # add to our graphs all the possible graphs of size "size" that we can build from the graphs of size "size - 1"
    final_graphs = []
    max_edges = size * (size - 1)  # not /2 because it's a directed graph, so we can have 2 edges between 2 nodes
    for graph in graphs:
        for amount in range(1, max_edges + 1):  # we can add 1 to max_edges (including max_edges) edges to our graph
            # add "amount" edges to our new graph
            edge_sets = findPossibleEdges(size, amount)
            for edge_set in edge_sets:
                # create a new graph with the same nodes and edges as the current graph
                new_graph = Graph()
                new_graph.nodes = graph.nodes.copy()
                new_graph.edges = graph.edges.copy()
                # add the new node and edges to the new graph
                new_graph.add_node(size)
                for edge in edge_set:
                    new_graph.add_edge(edge)
                if new_graph not in final_graphs:
                    final_graphs.append(new_graph)

    return final_graphs


def findPossibleEdges(size, amount):
    """
    find all sets of "amount" possible edges (without duplicates) that contain last node of the graph,
    for a graph of size "size"
    :param size: size of the graph
    :param amount: amount of edges to find
    :return: list of sets of edges (each set is a list of edges of size "amount")
    """
    nodes = [i for i in range(1, size + 1)]
    edges = list(itertools.permutations(nodes, 2))
    return list(itertools.combinations([Edge(edge[0], edge[1]) for edge in edges if size in edge], amount))


def main():
    times = []
    for size in range(1, 4):
        start_time = time.time()
        printAllConnectedGraphs(size)
        times.append(time.time() - start_time)


if __name__ == '__main__':
    main()
