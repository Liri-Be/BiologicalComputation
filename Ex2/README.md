# EX2 - Find motifs in graphs
## Intro.
### Part 1 - find all motifs of a specific size 
In this part we wanted to find all motifs of a specific size.    
Done by using recursive method which constract the motifs of size = n according to the motifs of size = (n-1), where in size = 1, the only motif is graph with one node and no edges.
### Part 2 - count motifs of a specific size in a graph
In this part we wanted count motifs of a specific size in a graph.   
Done by finding all the motifs of said size, and count how many times each appear in said graph.

## Files
### GraphClasses.py
Contains all the classes that are related to the graphs (Edge class and Graph class).
### Part*.py (1/2)
Contains all the methods that are related to part* (1/2).

## How to run?
There are a few steps -
1. Clone into the project using git bush or terminal with this commend -
    ```
    git clone https://github.com/Liri-Be/BiologicalComputation.git
    ```
    (Or anyway else you'd like)
2. Open the terminal in the code directory.
3. Write this command in the computer's terminal/CMD in order to run Part* (1/2) - 
    ```
    python[3] Part*.py 
    ```
    write 3 if you are using linux, else only python.
