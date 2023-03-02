import json
import pickle

def save(d, name):
    with open('{}.pickle'.format(str(name)), 'wb') as handle:
        pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load(name):
    with open('{}.pickle'.format(str(name)), 'rb') as handle:
        b = pickle.load(handle)
        return b

data  = []
lines = 0

diff_authors = set()

categories = set()
with open("arxiv.json", 'r') as f:
    count = 0
    for line in f:
        a = json.loads(line)
        count += 1
        authors = a['authors'].split(',')
        for aa in authors:
            diff_authors.add(aa)
        
        date = int(a['update_date'][:4])
        cat = a['categories']
        categories.add(cat)
        
        if 'physics.soc-ph' in cat:
            data.append(a)
            count += 1
            print(count)
        
save(data, 'phys-soc.arxiv')