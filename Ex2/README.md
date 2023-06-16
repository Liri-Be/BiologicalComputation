# EX2 - Find motifs in graphs
## Intro.
### Part 1 - find all motifs of a specific size 
In this part, we wanted to find all motifs of a specific size.  
Done by constructing all of the possible connected graphs of size = n, and keeping one of each isometric class (keeping the graphs that they aren't a permutation of any other graph).   
Could be also done by using a recursive method that constructs the motifs of size = n according to the motifs of size = (n-1), where in size = 1, the only motif is a graph with one node and no edges. - much slower but implemented in Part1Old.py    
Prints all the motifs in the end, but can also save them to a file.
### Part 2 - count motifs of a specific size in a graph
In this part, we wanted to count motifs of a specific size in a graph.   
Done by finding all the motifs of said size, and counting how many times each appears in the said graph.

## Files
### GraphClasses.py
Contains all the classes that are related to the graphs (Edge class and Graph class).
### Part*.py (1/2)
Contains all the methods that are related to part* (1/2).
### Part1Old.py
Contains all the methods that are related to part 1 by solving it with recursion - not recommended.
### plotTimes.py
Contains all the methods that are related to plotting the times of the algorithms.   
Used for the report's time complexity analysis of the algorithms of part 1.

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
    write 3 if you are using Linux, else only Python.   
*Note: you can also open the code in your favorite IDE and run it from there :smiley:
