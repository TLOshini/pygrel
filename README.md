PyGrel makes generating different types of graphs so much easier! 

Main Features
=============

Here are just a few things PyGrel can do:

  1.  Generates a synthetic Web graph of about one million nodes in a few minutes on a desktop machine. 
  2.  Implements a **threaded** variant of the RMAT algorithm for generating power law graphs. 
  3.  Number of threads used for graph generation can be changed. 
  4.  Computes connected components in a graph using [Tarjan's strongly connected components algorithm](http://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm). 
  5.  Support for both [directed](http://en.wikipedia.org/wiki/Graph_(mathematics)#Directed_graph) and [undirected](http://en.wikipedia.org/wiki/Graph_(mathematics)#Undirected_graph) graphs. 
  6.  A little tweak can produce graphs representing social-networks or community-networks. 

Installation
============

After checking out the repository, run `$python setup.py install` in the command line.

Dependencies
============

- Dependency project 1
- Dependency project 2

Documentation
=============

The exposed API is fairly general and can be used to represent any kind of graph in Python.
The official documentation of the latest release is available in many formats:
API reference
-	HTML [online](http://pywebgraph.sourceforge.net/doc/pywebgraph-2.72-api-html/index.html) | [tgz](putlink) | [zip](putlink)
- 	PDF  [online](http://pywebgraph.sourceforge.net/doc/pywebgraph-2.72-api-html/index.html) | [tgz](putlink) | [zip](putlink)

Click [here](putlink) for earlier versions of pywebgen
  
Some Examples
=============

Getting help
```
./genwebgraph.py --help
```
Generating graph using default settings
```
./genwebgraph.py --threads=1
```
Generating a 1000-vertex and 1000-egde graph using 5 threads and storing it in ~/mygraph.pyg
```
./genwebgraph.py --threads=5 --max-vertices=1000 --max-edges=1000 --output=~/mygraph.pyg
```
Same as above but without self-loops (edges that connect a vertex to itself)
```
./genwebgraph.py --threads=5 --max-vertices=1000 --max-edges=1000 --output=~/mygraph.pyg --no-self-loops
```
Storing in dot compatible output and making a postscript file
```
./genwebgraph.py --output=~/mygraph.pyg --format=dot
dot -Tps ~/mygraph.pyg -o mygraph.ps`
```
Generates a 1000-vertex and 1000-egde graph using 5 threads and stores it in ~/mygraph.pyg. Also, finds connected components in that graph and store them in ~/mycomp.cc. Tarjan's strongly connected components algorithm is used.
```
./genwebgraph.py --threads=5 --max-vertices=1000 --max-edges=1000 --output=~/mygraph.pyg --find-conncomps --file-conncomps=~/mycomp.cc
```
Same as above but only stores the largest component
```
./genwebgraph.py --threads=5 --max-vertices=1000 --max-edges=1000 --output=~/mygraph.pyg --find-conncomps --only-largest --file-conncomps=~/mycomp.cc
```


License
=======

PyGrel is Released under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0) ([FAQ](http://www.apache.org/foundation/license-faq.html))

Developers
==========

Saket Sathe [Website](http://saketsathe.net)