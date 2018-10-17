# Creator: Duncan Sussfeld
# Created on: 16/10/2018


import networkx as nx


def build_graph(nodes, edges):
    """"builds a graph with nodes and edges given in entry in list/set format"""
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    for i in G.nodes:
        G.nodes[i]['status'] = 'out'  # initially each node is outside the mis
    return G


def arap(G):
    """computes the MIS of graph G using the Arapoglu Algorithm"""
    stop = False
    while not stop:
        stop = True
        for i in G.nodes:  # initialising all the variables needed
            G.nodes[i]['inNbr'] = False
            G.nodes[i]['inNbrAll'] = True
            G.nodes[i]['inNbrLower'] = False
            G.nodes[i]['waitNbr'] = False
            G.nodes[i]['waitNbrLower'] = False
            G.nodes[i]['outNbrLower'] = False
            G.nodes[i]['outNbrAll'] = True

            for j in G.adj[i]:  # updating the values of these variables

                if G.nodes[j]['status'] == 'in':
                    G.nodes[i]['inNbr'] = True  # i has j as 'in' neighbor
                    if j<i:
                        G.nodes[i]['inNbrLower'] = True  # i has j as 'in' neighbor with smaller index
                else:
                    G.nodes[i]['inNbrAll'] = False  # if j is not 'in' then not all neighbors of i are 'in'

                if G.nodes[j]['status'] == 'wait':
                    G.nodes[i]['waitNbr'] = True  # i has j as 'in' neighbor
                    if j<i:
                        G.nodes[i]['waitNbrLower'] = True  # i has j as 'wait' neighbor with smaller index

                if G.nodes[j]['status'] == 'out':
                    if i<j:
                        G.nodes[i]['outNbrLower'] = True  # i has j as 'out' neighbor with smaller index
                else:
                    G.nodes[i]['outNbrAll'] = False  # if j is not 'out' then not all neighbors of i are 'in'

        for i in G.nodes:  # updating the nodes status by applying the 6 rules of the algorithm

            if G.nodes[i]['status'] == 'out':
                if G.nodes[i]['outNbrAll'] and not G.nodes[i]['outNbrLower']:
                    G.nodes[i]['status'] = 'in'
                    stop = False
                if G.nodes[i]['outNbrAll'] and G.nodes[i]['outNbrLower']:
                    G.nodes[i]['status'] = 'wait'
                    stop = False

            if G.nodes[i]['status'] == 'wait':
                if G.nodes[i]['inNbr']:
                    G.nodes[i]['status'] = 'out'
                    stop = False
                if not G.nodes[i]['inNbr'] and not G.nodes[i]['waitNbrLower']:
                    G.nodes[i]['status'] = 'in'
                    stop = False

            if G.nodes[i]['status'] == 'in':
                if G.nodes[i]['inNbrLower'] and not G.nodes[i]['waitNbr']:
                    G.nodes[i]['status'] = 'wait'
                    stop = False
                if G.nodes[i]['inNbrAll'] and not G.nodes[i]['inNbrLower']:
                    G.nodes[i]['status'] = 'out'
                    stop = False


def test1():
    """tests the implementation of the algorithm on the example given in the paper (fig.6)"""
    result_MIS, expected = [], [1, 4, 8]
    graph = build_graph(range(1, 9), {(1, 2), (1, 5), (2, 8), (2, 7), (2, 5), (4, 3), (4, 5), (4, 6), (4, 7)})
    for i in [3, 4, 6, 7]:
        graph.nodes[i]['status'] = 'in'
    arap(graph)
    for i in graph.nodes:
        if graph.nodes[i]['status'] == 'in':
            result_MIS.append(i)
    assert result_MIS == expected


test1()
