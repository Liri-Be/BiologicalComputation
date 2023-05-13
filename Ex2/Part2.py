from math import factorial

from GraphClasses import Graph, Edge
from Part1 import createConnectedGraphs


def countAppearances(graph, subgraph):
    """
    count how many times subgraph appear in our graph
    :param graph: the full graph
    :type graph: Graph
    :param subgraph: new graph (possible subgraph of graph)
    :type subgraph: Graph
    :return: count the appearances of subgraph in our graph
    """
    permutations = graph.permute_graph()
    count = 0
    for permutation in permutations:  # scan all permutation of the graph
        is_sub_graph = True
        for edge in subgraph.get_edges():
            if edge not in permutation.get_edges():  # subgraph isn't a subgraph of this permutation
                is_sub_graph = False
        if is_sub_graph:  # count++ only if it's a subgraph of some permutation
            count += 1

    return count // factorial(len(graph.get_nodes()) - len(subgraph.get_nodes()))


def findAllMotifs(graph, motif_size):
    """
    find all the motifs of size "motif_size" in our graph
    :param graph: the graph we want to find the motifs in
    :type graph: Graph
    :param motif_size: size of the motifs we want to find
    :type motif_size: int
    :return: list of all the motifs of size "motif_size" in the graph, and their count
    """
    possible_motifs = createConnectedGraphs(motif_size)  # all the possible motifs of size "motif_size"
    graph_motifs = []
    motifs_count = 0
    for motif in possible_motifs:
        count = countAppearances(graph, motif)  # count how many times this motif in the graph
        graph_motifs.append((motif, count))
        motifs_count += count

    graph_motifs.append(motifs_count)
    return graph_motifs


def printAllMotifs(graph, motif_size):
    """
    driver code for the function - findAllMotifs - also print the results
    :param graph: the graph we want to find the motifs in
    :type graph: Graph
    :param motif_size: size of the motifs we want to find
    :type motif_size: int
    :return: None
    """
    if motif_size < 1:
        print("Invalid size - must 1 or greater")

    motifs = findAllMotifs(graph, motif_size)
    motifs_count = motifs.pop(-1)
    print(f"Motif size = {motif_size}")
    print(f"Overall motifs = {motifs_count}")
    for idx, motif in enumerate(motifs):
        print(f"#{idx + 1}")
        print(f"Count = {motif[1]}")
        print(motif[0])


def main():
    graph = Graph()
    for i in range(3):
        graph.add_node(i + 1)
    edges = [(1, 2), (2, 3), (3, 1)]
    for edge in edges:
        graph.add_edge(Edge(*edge))
    printAllMotifs(graph, 3)


if __name__ == '__main__':
    main()
