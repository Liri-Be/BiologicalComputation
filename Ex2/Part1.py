import itertools
import time

from GraphClasses import Graph


# find all connected graphs of size "size"
def findAllPossibleEdges(size, amount):
    """
    find all sets of "amount" possible edges (without duplicates) for a graph of size "size"
    :param size: size of the graph
    :param amount: amount of edges to find
    :return: list of sets of edges (each set is a list of edges of size "amount")
    """
    # create all the possible edges to add to the graph
    nodes = [i for i in range(1, size + 1)]
    edges = list(itertools.permutations(nodes, 2))

    # create all the possible sets of edges of size "amount"
    return list(itertools.combinations([(edge[0], edge[1]) for edge in edges], amount))


def dfs(node, edges, visited):
    """
    run dfs on the graph represented by the given edges, starting from the given node, and mark all the visited nodes
    :param node: the current node
    :param edges: the edges of the graph
    :param visited: list of booleans - visited[i] is True if node i+1 was visited, False otherwise
    :return: None
    """
    visited[node - 1] = True
    for edge in edges:
        if edge[0] == node and not visited[edge[1] - 1]:
            dfs(edge[1], edges, visited)
        elif edge[1] == node and not visited[edge[0] - 1]:
            dfs(edge[0], edges, visited)


def isConnected(edges, size):
    """
    check if the graph represented by the given edges is connected or not, using dfs
    :param edges: the edges of the graph
    :param size: the number of nodes in the graph
    :return: Boolean - True if the graph is connected, False otherwise
    """
    visited = [False] * size
    dfs(1, edges, visited)  # run dfs from node 1
    return all(visited)


def minMaxEdgesConnected(size):
    """
    find the min and max amount of edges in a connected graph of size "size"
    :param size: the number of nodes in the graph
    :return: tuple of the min and max amount of edges in a connected graph of size "size"
    """
    # the min and max amount of edges in a connected graph of size "size"
    min_edges = size - 1  # a connected graph of size "size" has at least "size - 1" edges
    max_edges = size * (size - 1)  # a connected graph of size "size" has at most 2 edges for each pair of nodes
    return min_edges, max_edges


def findAllPossibleConnectedGraphs(size):
    """
    find all possible graphs of size "size"
    :param size: the number of nodes in the graphs
    :return: dict of all possible graphs of size "size" - the keys are the number of edges in the graph, and the values
    are lists of all the graphs with that number of edges (each graph here is represented by a list of edges)
    """
    graphs = {}

    min_edges, max_edges = minMaxEdgesConnected(size)  # the min and max amount of edges in a connected graph

    for amount in range(min_edges, max_edges + 1):
        graphs[amount] = []
        edge_sets = findAllPossibleEdges(size, amount)  # all possible sets of edges of size "amount"
        connected_edge_sets = [edge_set for edge_set in edge_sets if isConnected(edge_set, size)]
        graphs[amount] = connected_edge_sets

    return graphs


def permuteEdges(edges, size):
    """
    permute the edges in the given list
    :param edges: list of edges
    :param size: the number of nodes in the graph
    :return: list of all the permutations of the edges in the given list
    """
    nodes = [i for i in range(1, size + 1)]
    permutations = []

    for permutation in list(itertools.permutations(nodes, size)):
        # fix the edges according to the permutation
        new_edges = []
        for edge in edges:
            new_edge = (permutation[edge[0] - 1], permutation[edge[1] - 1])
            new_edges.append(new_edge)
        permutations.append(new_edges)

    return permutations


def findNonIsoConnectedGraphs(size):
    """
    find all connected graphs of size "size" - one graph from each isomorphism class
    :param size: the number of nodes in the graph
    :return: list of all connected graphs of size "size"
    """
    if size < 1:
        print("Invalid size - must 1 or greater")
        return None

    all_graphs = findAllPossibleConnectedGraphs(size)  # find all possible connected graphs of size "size"

    min_edges, max_edges = minMaxEdgesConnected(size)  # the min and max amount of edges in a connected graph

    final_graphs = []

    for amount in range(min_edges, max_edges + 1):
        graphs_edges = all_graphs[amount]  # all graphs with "amount" edges

        if len(graphs_edges) == 0:  # if there are no connected graphs with "amount" edges - continue
            continue

        # remove isomorphic graphs - we want only one graph from each isomorphism class
        if len(graphs_edges) == 1:  # if there is only one connected graph with "amount" edges - add it
            final_graphs.append(Graph(edges=graphs_edges[0], size=size))
            continue

        # else - keep only the non-isomorphic graphs
        non_iso_edges = []
        for edges in graphs_edges:
            added = False
            permutations = permuteEdges(edges, size)  # find all the isomorphism classe of the graph
            for permutation in permutations:
                if set(permutation) in non_iso_edges:  # check if the graph is isomorphic to a graph we already added
                    added = True
                    break
            if not added:  # if the graph is not isomorphic to any graph we already added - add it
                non_iso_edges.append(set(edges))  # add only the graphs that are not isomorphic to any other graph

        for edges in non_iso_edges:  # for each isomorphism class - add the first graph to the final graphs
            # only one graph from each isomorphism class - so we can pop the first
            new_graph = Graph(edges=list(edges), size=size)  # edg.pop
            final_graphs.append(new_graph)

    return final_graphs


def printGraphs(graphs, size, file_name=None):
    """
    prints the given graphs and their index in the list, and writes them to a file if a file name is given
    :param graphs: list of graphs
    :type graphs: list[Graph]
    :param size: the number of nodes in the graphs
    :param file_name: if not None, the function will also write the graphs to a file with the given name
    :return: None
    """
    data_str = ""
    data_str += f"Size = {size}\n"
    data_str += f"Count = {len(graphs)}\n"
    for idx, graph in enumerate(graphs):
        data_str += f"#{idx + 1}\n"
        data_str += str(graph)

    if file_name is not None:  # if a file name is given - write the graphs to a file
        with open(file_name, "a") as file:
            file.write(data_str)

    print(data_str)  # print the graphs


def main():
    times = []
    file_name = f"./graphs.txt"
    for size in range(1, 5):
        start_time = time.time()
        graphs = findNonIsoConnectedGraphs(size)
        times.append(float("{:.5f}".format(time.time() - start_time)))
        printGraphs(graphs, size, file_name)
        with open(file_name, "a") as file:
            file.write(f"Execution time: {times[-1]} seconds\n")


if __name__ == '__main__':
    main()
