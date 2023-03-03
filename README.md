# Hyperlink communities in higher-order networks

This code implements the algorithms and analyses presented in [https://arxiv.org/pdf/2303.01385.pdf](https://arxiv.org/pdf/2303.01385.pdf)

## Abstract

Many networks can be characterised by the presence of communities, which are groups of units that are closely linked and can be relevant in understanding the system's overall function. Recently, hypergraphs have emerged as a fundamental tool for modelling systems where interactions are not limited to pairs but may involve an arbitrary number of nodes. Using a dual approach to community detection, in this study we extend the concept of link communities to hypergraphs, allowing us to extract  informative clusters of highly related hyperedges. We analyzed the dendrograms obtained by applying hierarchical clustering to distance matrices among hyperedges on a variety of real-world data, showing that hyperlink communities naturally highlight the hierarchical and multiscale structure of higher-order networks. Moreover, by using hyperlink communities, we were able to extract overlapping memberships from nodes, overcoming the limitations of traditional hard clustering methods. Finally, we introduce higher-order network cartography as a practical tool for categorizing nodes into different structural roles based on their interaction patterns and community participation. This approach helps identify different types of individuals in a variety of real-world social systems. Our work contributes to a better understanding of the structural organization of real-world higher-order systems.

<img src="https://github.com/FraLotito/hyperlink-communities/blob/main/cover.png" data-canonical-src="https://github.com/FraLotito/hyperlink-communities/blob/main/cover.png" width="700" height="300" />

## Code organization
* ```experiments.ipynb``` jupyter notebook to replicate the experiments from the paper
* ```linegraph.py``` implements the computations of distances between hyperlinks
* ```loaders.py``` contains the loader for the datasets (see section below)
* ```extract_from_arxiv.py``` and ```create_hypergraph_physsoc.py``` useful to extract higher-order co-authorship networks from arxiv data
* Pickle files contain precomputed data, such as hyperlink distances 

## Datasets
Please download the datasets [here](https://drive.google.com/drive/folders/1vwdkiEcRoAjazXBI4iaoDlFo5HYUleQ5?usp=sharing) and extract the archive inside the main directory.

## How to use custom datasets
If you wish to perform hyperlink community analysis on your own datasets, you should implement a custom ```loader``` function. This function should return a set of tuples. Each tuple represents an hyperedge, and will contain the ids of the nodes involved in a group interactions.  


