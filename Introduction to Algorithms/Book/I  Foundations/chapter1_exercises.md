# Solutions to Chapter 1: The Role of Algorithms in Computing
Introduction to Algorithms
<!-- vscode-markdown-toc -->
* [1.1 Algorithms](#Algorithms)
	* [1.1-1](#)
		* [Sorting](#Sorting)
		* [Convex Hull](#ConvexHull)
	* [1.1-2](#-1)
	* [1.1-3](#-1)
		* [Arrays](#Arrays)
	* [1.1-4](#-1)
	* [1.1-5](#-1)
* [1.2 Algorithms as a technology](#Algorithmsasatechnology)
	* [1.2-1](#-1)
* [1.2-2](#-1)
* [1.2-3](#-1)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->
## <a name='Algorithms'></a>1.1 Algorithms
### <a name=''></a>1.1-1
#### <a name='Sorting'></a>Sorting
Sorting the inventory of a library in alphabetical order.
#### <a name='ConvexHull'></a>Convex Hull
Clustering

### <a name='-1'></a>1.1-2
Besides speed, memory and use of computational power are also important

### <a name='-1'></a>1.1-3
#### <a name='Arrays'></a>Arrays
##### Pros
- easy access (O(1))
##### Coms
- hard to inser elements (O(n))
- after declaration only expandable if it would be copied into a bigger array

### <a name='-1'></a>1.1-4
The shortest path between two junctions, as well as the traveling salesman problem work on graphs and both try to minimize the route traveled.  
However, the shortest path problem travels from one junction to another, where as in tsp a roundtrip is planed. Moreover, TSP tries to visit all nodes in the graph at least once, where as the shortest path, just tries to find the shortest path between to nodes.

### <a name='-1'></a>1.1-5
In medical testing, only the best and proper solution will do, since we neither want false positive nor true negatives.  
However, when it comes to planning a route for a package delivery company, the best solution will do (Since the extra computational cost, would not be worth it from a commercial standpoint)


## <a name='Algorithmsasatechnology'></a>1.2 Algorithms as a technology
### <a name='-1'></a>1.2-1
For example a spell checker, would on a base level require an algorithm to check whether the input of the user is present in a (sorted) dictionary of all English words. (binary search)  
Moreover, we could make the spell checker even smarter. If a word does not appear inside the dictionary, we could give the user the "closest" word we know, to his input. (String difference)  
Going even deaper into NLP our spell checker could also check for grammar mistake or make style recommendations.

## <a name='-1'></a>1.2-2
Table \o/  
Elements to sort| Insertion Sort | Merge Sort
-|-|-|
n | 8n^2 | 64n*lg(n)
8 | 512 | 1536
10 | 800 | 2.126
20 | 3.200 | 5.532
50 | 20.000 | 18.060
40 | 12.800 | 13.624
43 | 14.792 | 14.933
44 | 15.488 | 15.373
After 44 elements to sort Merge Sort is more effective.

## <a name='-1'></a>1.2-3
Elements to sort| Algorithm 1 | Algorithm 2
-|-|-|
n | 100n^2 | 2^n
10 | 10.000 | 1.024
20 | 40.000 | 1.048.576
15 | 22.500 | 32.768
14 | 19.600 | 16.384
After 14 elements the first algorithm has a better performance.