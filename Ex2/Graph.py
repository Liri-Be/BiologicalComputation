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

    def __eq__(self, other):  # check if two graphs are equal
        for node in self.nodes:
            if node not in other.get_nodes():
                return False
        for edge in self.edges:
            if edge not in other.get_edges():
                return False
        return True

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


def createConnectedGraphs(size):
    count = 0
    done = False
    graphs = []
    while not done:
        pass


def main():
    graph1 = Graph()
    for i in range(3):
        graph1.add_node(i + 1)
    edges = [(1, 2), (3, 2), (1, 3)]
    for source, target in edges:
        graph1.add_edge(Edge(source, target))
    print(graph1)
    graph2 = Graph()
    for i in range(3):
        graph2.add_node(i + 1)
    edges = [(1, 2), (3, 2), (1, 3)]
    for source, target in edges:
        graph2.add_edge(Edge(target, source))
    print(graph2)
    print(graph1 == graph2)


if __name__ == '__main__':
    main()
