import itertools
import time
import matplotlib.pyplot as plt
import numpy
import scipy

from GraphClasses import Graph, Edge


# find all connected graphs of size "size"
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


def printAllConnectedGraphs(size):
    """
    driver function for createConnectedGraphs - prints the graphs and their count
    :param size: the size of the graphs we want to create
    :return: None
    """
    if size < 1:
        print("Invalid size - must 1 or greater")
        return

    graphs = createConnectedGraphs(size)
    print(f"Size = {size}")
    print(f"Count = {len(graphs)}")
    for idx, graph in enumerate(graphs):
        print(f"#{idx + 1}")
        print(graph)


def plotExecutionTimes(times):
    # plot the data
    x = numpy.array(range(1, len(times) + 1))
    y = numpy.array(times)
    plt.scatter(x, y, label='Times', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Size')
    plt.title('Execution times')
    popt = scipy.optimize.curve_fit(lambda t, a, b: a * numpy.exp(b * t) - 1, x, y, p0=(4, 0.1))
    plt.plot(x, popt[0][0] * numpy.exp(popt[0][1] * x), label='fit: %.5f*e^( %.5ft)' % tuple(popt[0]), color='red')
    plt.legend()
    plt.show()


def main():
    times = []
    for size in range(1, 5):
        start_time = time.time()
        printAllConnectedGraphs(size)
        times.append(float("{:.5f}".format(time.time() - start_time)))

    # plot the times
    plotExecutionTimes(times)


if __name__ == '__main__':
    main()
