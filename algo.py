from math import *
import networkx as nx


def preprocessing(G):
    for i in range(G.number_of_nodes()):
        G.nodes[i]["active"] = True



def MIS(G):
    '''G = nx.Graph()'''
    
    preprocessing(G)
    
    n = len(V)
    D = max(len(V[i]) for i in range(n))
    
    M = 34#faudrait trouver la vraie valeur
    
    for i in range(log(D)):
        for j in range(M*log(n)):
            
            #Exchange 1
            v = 0
            
            
    
#  he algorithm, presentedin Table 1, is synchronously executed by all nodes
    
# 1. Algorithm: MIS (n, D) at node u
# 2. For i = 0: log D
# 3. For j = 0: M log n // M is constant derived below
# 4. * exchange 1*
# 5. v = 0
# 6. With probability 1
# 2logD−i broadcast B to neighbors and set v = 1 // B is one bit
# 7. If received message from neighbor, then v = 0
# 8. * exchange 2 *
# 9. If v = 1 then
# 10. Broadcast B; join MIS; exit the algorithm
# 11. Else
# 12. If received message B in this exchange, then mark node u inactive; exit the algorithm
# 13. End
# 14. End
# 15. End