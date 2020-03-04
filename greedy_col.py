import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_colour(G,i):
    n = len(G.nodes())
    adjColours = []

    
    for m in G[i]:
        colour = G.node[m]['colour']
        if colour not in adjColours:
            adjColours.append(G.node[m]['colour'])
    for j in range(1,n+1):
        if j not in adjColours:
            return j

    







def greedy(G):
    global kmax
    kmax = 0
    usedCols = []

    for j in G.nodes():
        colToUse = find_smallest_colour(G,j)
        if(colToUse not in usedCols):
            kmax += 1
            usedCols.append(colToUse)
        G.node[j]['colour'] = colToUse


    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.node[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)
