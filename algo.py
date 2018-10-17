from math import log
import networkx as nx
from random import random
from copy import deepcopy

def preprocessing(G):
    for i in range(G.number_of_nodes()):
        G.nodes[i]["active"] = True
        G.nodes[i]["MIS"] = False


def MIS(G):
    '''G = nx.Graph()'''
    '''je suppose que les noeuds sont dans [|0, n-1|]'''
    
    G.add_nodes_from(G.nodes, active = True, MIS = False)
    history = []
    history.append(deepcopy(G))

    n = D = G.number_of_nodes()
    
    M = 34#faudrait trouver la vraie valeur
    
    for i in range(int(log(D))+1):
        for j in range(int(M*log(n))+1):
            
            G.add_nodes_from(G.nodes, v = 0, received = False)
            
            
            #Exchange 1 : emission            
            for u in G.nodes:
                if G.nodes[u]["active"]:
                    p = random()
                    if p <= 1./ (2**(log(D)-i)):
                        for voisin in G.adj[u]:
                            G.nodes[voisin]["received"] = True
                        G.nodes[u]["v"] = 1
                
            #reception
            for u in G.nodes:
                if G.nodes[u]["active"]:
                    if G.nodes[u]["received"]:
                        G.nodes[u]["v"] = 0
            
            G.add_nodes_from(G.nodes, received = False)
            
            #Exchange 2 : emission
            for u in G.nodes:
                if G.nodes[u]["active"]:
                    if G.nodes[u]['v'] == 1:
                        for voisin in G.adj[u]:
                            G.nodes[voisin]['received'] = True
                        G.nodes[u]["active"] = False
                        G.nodes[u]["MIS"] = True 
                    
            #reception
            for u in G.nodes:
                if G.nodes[u]["active"]:
                    if G.nodes[u]["received"]:
                        G.nodes[u]["active"] = False
            
            history.append(deepcopy(G))

    return (G, history)

def colors(G):
    colors = []
    for node in G.nodes:
        if G.nodes[node]["MIS"] == True:
            colors.append("green")

        elif G.nodes[node]["active"] == True:
            colors.append("red")
    
        else:
            colors.append("black")
    return colors



def test_1():
    G = nx.Graph()
    G.add_nodes_from([0, 1, 2])
    G.add_edges_from([(0, 1), (0, 2), (1, 2)])
    L = MIS(G)[0]
    mis = [L.nodes[node]["MIS"] for node in L.nodes]
    assert(mis == [True, False, False] or mis == [False, True, False] or mis == [False, False, True])


    G = nx.Graph()
    G.add_nodes_from([0, 1, 2])
    G.add_edges_from([(0, 1), (0, 2)])
    L = MIS(G)[0]
    mis = [L.nodes[node]["MIS"] for node in L.nodes]
    assert(mis == [True, False, False] or mis == [False, True, True])
    