import pickle

def save(d, name):
    with open('{}.pickle'.format(str(name)), 'wb') as handle:
        pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load(name):
    with open('{}.pickle'.format(str(name)), 'rb') as handle:
        b = pickle.load(handle)
        return b

data = load('phys-soc.arxiv')
idx = {}
c = 0

inv = {}
h = {}

count = 0
for paper in data:
    authors = paper['authors_parsed']
    ids = []
    for a in authors:
        a = ' '.join(a)
        if a in idx:
            ids.append(idx[a])
        else:
            idx[a] = c
            ids.append(idx[a])
            c += 1
    ids = tuple(sorted(ids))
    if ids not in h:
        h[ids] = 0
    h[ids]+=1
    count += 1
    print(count)

inv_map = {v: k for k, v in idx.items()}

save(h, 'hypergraph_physics_society')
save(inv_map, 'meta_physics_society')