## BREADTH-FIRST-SEARCH

Breadth First Search (BFS) algorithm traverses a graph in a breadthward motion
and uses a queue to remember to get the next vertex to start a search, when a dead end
occurs in any iteration.
As in the example given above, BFS algorithm
traverses from A to B to E to F first then to C and
G lastly to D. It employs the following rules.

- Rule 1 − Visit the adjacent unvisited vertex.
Mark it as visited. Display it. Insert it in a queue.
- Rule 2 − If no adjacent vertex is found, remove
the first vertex from the queue.
- Rule 3 − Repeat Rule 1 and Rule 2 until the
queue is empty
