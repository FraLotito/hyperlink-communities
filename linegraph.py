import networkx as nx
import pickle

def load(name):
    with open('{}.pickle'.format(str(name)), 'rb') as handle:
        b = pickle.load(handle)
        return b

def save(d, name):
    with open('{}.pickle'.format(str(name)), 'wb') as handle:
        pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)


def jaccard_similarity(sa, sb):
    sa = set(sa)
    sb = set(sb)
    i = sa.intersection(sb)
    u = sa.union(sb)

    return len(i) / len(u)
    #return len(i)

def intersection(sa, sb):
    sa = set(sa)
    sb = set(sb)
    i = sa.intersection(sb)

    return len(i)
    

def build_line_graph(h):
    print("Building line graph: E = {}".format(len(h)))
    h = list(h)

    G = nx.Graph()
    G.add_nodes_from([i for i in range(len(h))])

    for i in range(len(h)-1):
        #print("Done {} of {}".format(i, len(h)))
        for j in range(i+1, len(h)):
            e_i = set(h[i])
            e_j = set(h[j])

            w = jaccard_similarity(e_i, e_j)

            if w > 0:
                G.add_edge(i, j, weight=w)
    
    print("N: {}, E: {}".format(G.number_of_nodes(), G.number_of_edges()))
    #nx.write_gpickle(G, "pacs_line.pickle")
    return G


def build_line_graph_2(h, name):
    try:
        print("Reading pickle")
        out = nx.read_gpickle("datasets_line_graphs/{}.pickle".format(name))
        print("Line graph loaded")
        return out
    except:
        print("Building line graph: E = {}".format(len(h)))
    h = list(h)

    adj = {}
    edge_to_id = {}

    cont = 0
    for e in h:
        e = tuple(sorted(e))
        edge_to_id[e] = cont
        for n in e:
            if n not in adj:
                adj[n] = []
            adj[n].append(e)
        cont += 1

    G = nx.Graph()
    G.add_nodes_from([i for i in range(len(h))])

    vis = {}
    c = 0

    for n in adj:
        print("Done {} of {}".format(c, len(adj)))
        for i in range(len(adj[n])-1):
            for j in range(i+1, len(adj[n])):
                k = tuple(sorted((edge_to_id[adj[n][i]], edge_to_id[adj[n][j]])))
                e_i = set(adj[n][i])
                e_j = set(adj[n][j])
                if k not in vis:
                    w = intersection(e_i, e_j)
                    if w > 0:
                        G.add_edge(edge_to_id[adj[n][i]], edge_to_id[adj[n][j]], weight=w)
                    vis[k] = True
        c+=1      
    
    print("N: {}, E: {}".format(G.number_of_nodes(), G.number_of_edges()))
    largest_cc = max(nx.connected_components(G), key=len)
    out = {}
    out['largest_cc'] = largest_cc
    out['ids'] = edge_to_id

    nx.write_gpickle(out, "datasets_line_graphs/{}.pickle".format(name))
    return out

def get_number_nodes(h):
    nodes = set()
    for e in h:
        for n in e:
            nodes.add(n)
    return nodes

#h = load('hypergraph_physics_society')
#m = load('meta_physics_society')    
