# DRIP -  Directed feedback vertex set computation using Reductions and Integer Programming

This repository contains an **exact solution** to the Directed Feedback Vertex Set problem.

The program is submitted to the [PACE Challenge 2022](https://pacechallenge.org/2022/) in the **exact track**.

The **Directed Feedback Vertex Set** problem is defined as follows:

**Input**: A directed graph $G = (V, E)$

**Output**: Find a minimum subset $X \subseteq V$ such that, when all vertices of $X$ and their adjacent edges are deleted from $G$, the remainder is acyclic

Thus, a feedback vertex set of a graph is a set of vertices whose deletion leaves a graph **acyclic**.

## Requirements

-   A 64-bit Linux operating system
-   Python 3
-   PuLP Library

## Build Application

1. Clone the repository:

    `git clone git@github.com:Amanj2000/PACE_2022_Directed_Feedback_Vertex_Set.git`

2. Install PuLP library: `pip install pulp`

## Run Application

The program reads a directed graph instance from stdin and print the FVS to stdout.
For the input and output format, please refer the [PACE challenge - Exact Track](https://pacechallenge.org/2022/tracks/#exact-track) page.

A usage example would be:

    cat input_graph | python3 drip.py > fvs.txt

Please keep all the 5 files: `input.txt`, `mfvs.txt`, `reduced_graph.txt`, `reductions`, `drip.py` in the same folder and run the above command

This exact solver runs until an optimal solution is found
