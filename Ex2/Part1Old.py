import itertools
import time

from GraphClasses import Graph, Edge


# old version -> works but (very!!) not efficient
def findPossibleEdges(size, amount, last_node=False):
    """
    find all sets of "amount" possible edges (without duplicates) that contain last node of the graph,
    for a graph of size "size"
    :param size: size of the graph
    :param amount: amount of edges to find
    :param last_node: True if we want only edges with the last_node, False otherwise
    :return: list of sets of edges (each set is a list of edges of size "amount")
    """
    # create all the possible edges to add to the graph
    nodes = [i for i in range(1, size + 1)]
    edges = list(itertools.permutations(nodes, 2))

    if last_node:  # if we want only edges with the last node
        edges = [edge for edge in edges if size in edge]

    # create all the possible sets of edges of size "amount"
    return list(itertools.combinations([Edge(edge[0], edge[1]) for edge in edges], amount))


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
            edge_sets = findPossibleEdges(size, amount, last_node=True)
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


def printAllConnectedGraphs(size, file_name=None):
    """
    driver function for createConnectedGraphs - prints the graphs and their count
    :param size: the size of the graphs we want to create
    :type size: int
    :param file_name: if not None, the function will also write the graphs to a file with the given name
    :type file_name: str
    :return: None
    """
    if size < 1:
        print("Invalid size - must 1 or greater")
        return

    graphs = createConnectedGraphs(size)
    data_str = ""
    data_str += f"Size = {size}\n"
    data_str += f"Count = {len(graphs)}\n"
    for idx, graph in enumerate(graphs):
        data_str += f"#{idx + 1}\n"
        data_str += str(graph)
    if file_name is not None:
        with open(file_name, "a") as file:
            file.write(data_str)
    print(data_str)


def main():
    times = []
    file_name = f"./graphs.txt"
    for size in range(1, 5):
        start_time = time.time()
        printAllConnectedGraphs(size, file_name=file_name)
        times.append(float("{:.5f}".format(time.time() - start_time)))
        with open(file_name, "a") as file:
            file.write(f"Execution time: {times[-1]} seconds\n")


if __name__ == '__main__':
    main()
