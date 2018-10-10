from math import *
import networkx as nx
from random import random

def preprocessing(G):
    for i in range(G.number_of_nodes()):
        G.nodes[i]["active"] = True
        G.nodes[i]["MIS"] = False


def MIS(G):
    '''G = nx.Graph()'''
    '''je suppose que les noeuds sont dans [|0, n-1|]'''
    
    preprocessing(G)
    
    n = D = G.number_of_nodes()
    
    M = 34#faudrait trouver la vraie valeur
    
    for i in range(int(log(D))+1):
        for j in range(int(M*log(n))+1):
            
            
            v = [0 for _ in range(n)]
            received = [False for _ in range(n)]
            
            #Exchange 1 : emission            
            for u in range(n):
                if G.nodes[u]["active"]:
                    p = random()
                    if p <= 1./ (2**(log(D)-i)):
                        for voisin in G.adj[u]:
                            received[voisin] = True
                        v[u] = 1
                
            #reception
            for u in range(n):
                if G.nodes[u]["active"]:
                    if received[u]:
                        v[u] = 0
            
            received = [False for _ in range(n)]
            
            #Exchange 2 : emission
            for u in range(n):
                if G.nodes[u]["active"]:
                    if v[u] == 1:
                        for voisin in G.adj[u]:
                            received[voisin] = True
                        G.nodes[u]["active"] = False
                        G.nodes[u]["MIS"] = True 
                    
            #reception
            for u in range(n):
                if G.nodes[u]["active"]:
                    if received[u]:
                        G.nodes[u]["active"] = False

    return [G.nodes[i]["MIS"] for i in range(n)]


def test_1():
    G = nx.Graph()
    G.add_nodes_from([0, 1, 2])
    G.add_edges_from([(0, 1), (0, 2), (1, 2)])
    L = MIS(G)
    print(L)
    assert(L == [True, False, False] or L == [False, True, False] or L == [False, False, True])
    