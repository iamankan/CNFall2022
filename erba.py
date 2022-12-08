
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

def length_of_graph(g: nx.classes.graph.Graph) -> int:
    return len(list(g.nodes))

def generate_er(n: int, p: float) -> any:
    return nx.erdos_renyi_graph(n, p, seed=0)

def generate_ba(n: int, c: int) -> any:
    return nx.barabasi_albert_graph(n, c, seed=0)

def plot_nx(G, n):
    pos = nx.circular_layout(G)
    nx.draw(G, pos, node_color=range(n), node_size=40, cmap=plt.cm.Blues)
    plt.show()

def plot_graph_gc(gclist_er: list, gclist_ba: list):
    plt.figure()
    xeruar=[]
    yeruar=[]
    for i in gclist_er:
        yeruar.append(len(list(i[0].nodes)))
        xeruar.append(i[2])
    plt.plot(xeruar,yeruar, color='r', label='Size of GC for ER with UAR')
    

    xertar=[]
    yertar=[]
    for i in gclist_er:
        yertar.append(len(list(i[1].nodes)))
        xertar.append(i[2])
    plt.plot(xertar,yertar, color='b', label='Size of GC for ER with Targeted')
    
    xbauar=[]
    ybauar=[]
    for i in gclist_ba:
        ybauar.append(len(list(i[0].nodes)))
        xbauar.append(i[2])
    plt.plot(xbauar,ybauar, color='g', label='Size of GC for BA with UAR')
    

    xbatar=[]
    ybatar=[]
    for i in gclist_ba:
        ybatar.append(len(list(i[1].nodes)))
        xbatar.append(i[2])
    plt.plot(xbatar,ybatar, color='y', label='Size of GC for BA with Targeted')

    plt.xlabel('B')
    plt.ylabel('Size of GC')

    plt.legend()

    plt.savefig("Residual_Giant_Component.png")
    

def plot_graph_avsp(gclist_er: list, gclist_ba: list):
    plt.figure()
    xeruar=[]
    yeruar=[]
    for i in gclist_er:
        yeruar.append(nx.average_shortest_path_length(i[0]))
        xeruar.append(i[2])
    plt.plot(xeruar,yeruar, color='r', label='Size of avg sp for ER with UAR')
    

    xertar=[]
    yertar=[]
    for i in gclist_er:
        yertar.append(nx.average_shortest_path_length(i[1]))
        xertar.append(i[2])
    plt.plot(xertar,yertar, color='b', label='Size of avg sp for ER with Targeted')

    xbauar=[]
    ybauar=[]
    for i in gclist_ba:
        ybauar.append(nx.average_shortest_path_length(i[0]))
        xbauar.append(i[2])
    plt.plot(xbauar,ybauar, color='g', label='Size of avg sp for BA with UAR')

    xbatar=[]
    ybatar=[]
    for i in gclist_ba:
        ybatar.append(nx.average_shortest_path_length(i[1]))
        xbatar.append(i[2])
    plt.plot(xbatar,ybatar, color='y', label='Size of avg sp for BA with Targeted')


    plt.xlabel('B')
    plt.ylabel('Size of Average shortest path')

    plt.legend()

    plt.savefig("Average_Shortest_Path.png")

def plot_graph_gc_against_p_er(gclist_er: list):
    plt.figure()
    xeruar=[]
    yeruar=[]
    for i in gclist_er:
        yeruar.append(length_of_graph(i[0]))
        xeruar.append(i[2])
    plt.plot(xeruar,yeruar, color='r', label='Size of GC for ER with UAR')
    

    xertar=[]
    yertar=[]
    for i in gclist_er:
        yertar.append(length_of_graph(i[1]))
        xertar.append(i[2])
    plt.plot(xertar,yertar, color='b', label='Size of GC for ER with Targeted')


    plt.xlabel('p')
    plt.ylabel('Size of Residual GC')

    plt.legend()

    plt.savefig("ResidualGC_ER_against_p.png")

def plot_graph_gc_against_c_ba(gclist_ba: list):
    plt.figure()
    xbauar=[]
    ybauar=[]
    for i in gclist_ba:
        ybauar.append(length_of_graph(i[0]))
        xbauar.append(i[2])
    plt.plot(xbauar,ybauar, color='r', label='Size of GC for BA with UAR')
    

    xbatar=[]
    ybatar=[]
    for i in gclist_ba:
        ybatar.append(length_of_graph(i[1]))
        xbatar.append(i[2])
    plt.plot(xbatar,ybatar, color='b', label='Size of GC for BA with Targeted')


    plt.xlabel('c')
    plt.ylabel('Size of Residual GC')

    plt.legend()

    plt.savefig("ResidualGC_BA_against_c.png")

def plot_graph_avsp_against_p_er(gclist_er: list):
    plt.figure()
    xeruar=[]
    yeruar=[]
    for i in gclist_er:
        yeruar.append(nx.average_shortest_path_length(i[0]))
        xeruar.append(i[2])
    plt.plot(xeruar,yeruar, color='r', label='Size of avg sp for ER with UAR')
    

    xertar=[]
    yertar=[]
    for i in gclist_er:
        yertar.append(nx.average_shortest_path_length(i[1]))
        xertar.append(i[2])
    plt.plot(xertar,yertar, color='b', label='Size of avg sp for ER with Targeted')


    plt.xlabel('p')
    plt.ylabel('Size of Residual GC')

    plt.legend()

    plt.savefig("AvgSP_ER_against_p.png")

def plot_graph_avsp_against_c_ba(gclist_ba: list):
    plt.figure()
    xbauar=[]
    ybauar=[]
    for i in gclist_ba:
        ybauar.append(nx.average_shortest_path_length(i[0]))
        xbauar.append(i[2])
    plt.plot(xbauar,ybauar, color='r', label='Size of GC for BA with UAR')
    

    xbatar=[]
    ybatar=[]
    for i in gclist_ba:
        ybatar.append(nx.average_shortest_path_length(i[1]))
        xbatar.append(i[2])
    plt.plot(xbatar,ybatar, color='b', label='Size of GC for BA with Targeted')


    plt.xlabel('c')
    plt.ylabel('Size of Residual GC')

    plt.legend()

    plt.savefig("AvgSP_BA_against_c.png")

def giant_component(G):
    conn_sorted = sorted(nx.connected_components(G), key=len)
    giant = G.subgraph(conn_sorted[-1])
    return giant


def uar(frozen_graph: nx.classes.graph.Graph, B: int):
    g = frozen_graph.copy()
    nodes2del = random.sample(list(g.nodes), B)
    g.remove_nodes_from(nodes2del)
    gc = giant_component(g)
    return gc

def targeted(frozen_graph: nx.classes.graph.Graph, B: int):
    g = frozen_graph.copy()
    degrees = list(g.degree)
    sorted_deg = sorted(degrees, key=lambda x: x[1], reverse=True)
    nodes2del = [node[0] for node in sorted_deg[:B]]
    g.remove_nodes_from(nodes2del)
    gc = giant_component(g)
    return gc


def perform_aa_er(n:int, p:float, B: int):
    G_er = generate_er(n,p)
    # plot_nx(G_er, len(list(G_er.nodes)))
    gclist = []
    for i in range(0,B):
        gclist.append((uar(G_er, i), targeted(G_er, i), i))
    return gclist



def perform_aa_ba(n:int, c:int, B: int):
    G_ba = generate_ba(n,c)
    # plot_nx(G_ba, len(list(G_ba.nodes)))
    gclist = []
    for i in range(0,B):
        gclist.append((uar(G_ba, i), targeted(G_ba, i), i))
    return gclist


def perform_ba_er(n:int, B: int=20):
    plist = np.linspace(0, 1, 10)
    gclist=[]
    for p in plist:
        G_er = generate_er(n, p)
        gclist.append((uar(G_er, B), targeted(G_er, B), p))
    return gclist

def perform_ba_ba(n:int, B: int=20):
    clist = [i+1 for i in range(10)]
    gclist=[]
    for c in clist:
        G_ba = generate_ba(n, c)
        gclist.append((uar(G_ba, B), targeted(G_ba, B), c))
    return gclist


gclist_er = perform_aa_er(50, 0.5, 50)
gclist_ba = perform_aa_ba(50, 5, 50)
plot_graph_gc(gclist_ba=gclist_ba, gclist_er=gclist_er)
plot_graph_avsp(gclist_ba=gclist_ba, gclist_er=gclist_er)

gclist_er_p = perform_ba_er(50)
plot_graph_gc_against_p_er(gclist_er=gclist_er_p)
plot_graph_avsp_against_p_er(gclist_er=gclist_er_p)

gclist_ba_c = perform_ba_ba(50)
plot_graph_gc_against_c_ba(gclist_ba=gclist_ba_c)
plot_graph_avsp_against_c_ba(gclist_ba=gclist_ba_c)

