# Hyperlink communities in higher-order networks

This code implements the algorithms and analyses presented in [arxiv link](arxiv link)

## Abstract

Many networks can be characterised by the presence of communities, which are groups of units that are closely linked and can be relevant in understanding the system's overall function. Recently, hypergraphs have emerged as a fundamental tool for modelling systems where interactions are not limited to pairs but may involve an arbitrary number of nodes. Using a dual approach to community detection, in this study we extend the concept of link communities to hypergraphs, allowing us to extract  informative clusters of highly related hyperedges. We analyzed the dendrograms obtained by applying hierarchical clustering to distance matrices among hyperedges on a variety of real-world data, showing that hyperlink communities naturally highlight the hierarchical and multiscale structure of higher-order networks. Moreover, by using hyperlink communities, we were able to extract overlapping memberships from nodes, overcoming the limitations of traditional hard clustering methods. Finally, we introduce higher-order network cartography as a practical tool for categorizing nodes into different structural roles based on their interaction patterns and community participation. This approach helps identify different types of individuals in a variety of real-world social systems. Our work contributes to a better understanding of the structural organization of real-world higher-order systems.

<img src="https://github.com/FraLotito/hyperlink-communities/blob/main/cover.png" data-canonical-src="https://github.com/FraLotito/hyperlink-communities/blob/main/cover.png" width="700" height="300" />

## Code organization
* ```motifs.py``` contains the implementation of the baseline algorithm proposed in the paper
* ```motif2.py``` contains the implementation of the efficient algorithm proposed in the paper
* ```utils.py``` contains some useful functions
* ```loaders.py``` contains the loader for the datasets (see section below)
* ```hypergraph.py``` contains the implementation of a data structure for hypergraphs in Python and the configuration model for hypergraphs proposed by [Phil Chodrow](https://github.com/PhilChodrow)

## Datasets
Please download the datasets [here](https://drive.google.com/file/d/1uFaftX_hqjTiBt2SZ_6fbggYG9ySK3Ss/view?usp=sharing) and extract the archive inside the main directory.

## How to use custom datasets
If you wish to perform hyperlink community analysis on your own datasets, you should implement a custom ```loader``` function. This function should return a set of tuples. Each tuple represents an hyperedge, and will contain the ids of the nodes involved in a group interactions.  

## How to perform higher-order motif analysis
If you wish to experiment with the code, you can run analysis setting up the parameter ```N``` in the code, which specifies the order of the motifs to use for the analysis. At the moment, the only feasible orders are ```N=3``` and ```N=4```. The parameter ```ROUNDS``` specifies the number of samples from the configuration model. Keep in mind that ```ROUNDS``` can heavily affect the performance. A value between 10 and 20 already gives reliable results.


