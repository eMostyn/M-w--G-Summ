import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
##    global visited_counter
    options = [] 
    if len(visited_counter) == 0:
        return 1
    else:
        for node in visited_counter:
            neighbours = G[node]
            for neighbour in neighbours:
                if(neighbour not in visited_counter):
                    options.append(neighbour)
        options.sort()
        return options[0]
    








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
    n = len(G.nodes())
    global kmax
    global visited_counter
    visited_counter = []
    kmax = 0
    usedCols = []
    while(len(visited_counter) != n):
        nextVert = find_next_vertex(G)
        visited_counter.append(nextVert)
        colToUse = find_smallest_colour(G,nextVert)
        if(colToUse not in usedCols):
            kmax += 1
            usedCols.append(colToUse)
        G.node[nextVert]['colour'] = colToUse







    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)
    print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)
