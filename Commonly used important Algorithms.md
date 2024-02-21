# Commonly used important Algorithms

1. **Linear Search**:
   - Explanation: Linear search iterates through each element in a list to find the target element.
   - Time Complexity: O(n)
   - Space Complexity: O(1)

2. **Binary Search**:
   - Explanation: Binary search is a divide-and-conquer algorithm that finds the target element in a sorted array by repeatedly dividing the search interval in half.
   - Time Complexity: O(log n)
   - Space Complexity: O(1)

3. **Bubble Sort**:
   - Explanation: Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
   - Time Complexity: O(n^2)
   - Space Complexity: O(1)

4. **Insertion Sort**:
   - Explanation: Insertion sort builds the final sorted array one item at a time by repeatedly taking the next element and inserting it into the proper position in the already sorted part of the array.
   - Time Complexity: O(n^2)
   - Space Complexity: O(1)

5. **Selection Sort**:
   - Explanation: Selection sort divides the input array into two parts: sorted and unsorted. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part.
   - Time Complexity: O(n^2)
   - Space Complexity: O(1)

6. **Heap Sort**:
   - Explanation: Heap sort builds a binary heap from the input array and repeatedly extracts the maximum (for max-heap) element from the heap, maintaining the heap property.
   - Time Complexity: O(n log n)
   - Space Complexity: O(1)

7. **Merge Sort**:
   - Explanation: Merge sort is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts each half, and then merges them to produce a sorted array.
   - Time Complexity: O(n log n)
   - Space Complexity: O(n)

8. **Quick Sort**:
   - Explanation: Quick sort chooses a pivot element and partitions the array around the pivot, such that elements smaller than the pivot are on its left and elements greater than the pivot are on its right. It then recursively sorts the subarrays.
   - Time Complexity: O(n log n) average case, O(n^2) worst case
   - Space Complexity: O(log n) average case, O(n) worst case

9. **Euclid's Algorithm for GCD**:
   - Explanation: Euclid's Algorithm finds the greatest common divisor (GCD) of two integers by repeatedly taking the remainder until the remainder becomes zero.
   - Time Complexity: O(log(min(a, b)))
   - Space Complexity: O(1)

10. **Sieve of Eratosthenes**:
    - Explanation: Sieve of Eratosthenes is an algorithm to find all prime numbers up to a given integer by iteratively marking the multiples of each prime number as composite.
    - Time Complexity: O(n log log n)
    - Space Complexity: O(n)

11. **Bit Manipulations**:
    - Explanation: Bit manipulation involves operations on individual bits of binary numbers, such as shifting, setting, clearing, and toggling bits.
    - Time Complexity: Depends on the specific operation
    - Space Complexity: Depends on the specific operation

12. **Breadth First Search (BFS)**:
    - Explanation: BFS explores all the neighbor nodes at the present depth before moving on to nodes at the next depth level.
    - Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    - Space Complexity: O(V) for storing visited nodes

13. **Depth First Search (DFS)**:
    - Explanation: DFS explores as far as possible along each branch before backtracking. It uses a stack data structure to maintain the search path.
    - Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    - Space Complexity: O(V) for storing visited nodes if using recursion; O(V + E) for an iterative implementation.

14. **Dijkstra's Algorithm**:
    - Explanation: Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a weighted graph by iteratively selecting the node with the shortest distance from the source and updating the distances of its neighbors.
    - Time Complexity: O((V + E) log V) using a binary heap or Fibonacci heap for priority queue.
    - Space Complexity: O(V) for storing distances and visited nodes.

15. **Inorder Traversal**:
    - Explanation: Inorder traversal visits nodes in the order: left subtree, root, right subtree.
    - Time Complexity: O(n)
    - Space Complexity: O(h), where h is the height of the binary tree.

16. **Preorder Traversal**:
    - Explanation: Preorder traversal visits nodes in the order: root, left subtree, right subtree.
    - Time Complexity: O(n)
    - Space Complexity: O(h), where h is the height of the binary tree.

17. **Postorder Traversal**:
    - Explanation: Postorder traversal visits nodes in the order: left subtree, right subtree, root.
    - Time Complexity: O(n)
    - Space Complexity: O(h), where h is the height of the binary tree.

18. **Kruskal's Algorithm**:
    - Explanation: Kruskal's algorithm finds the minimum spanning tree of a connected, undirected graph by repeatedly adding the shortest edge that does not form a cycle.
    - Time Complexity: O(E log E) or O(E log V) using a suitable data structure for edge sorting.
    - Space Complexity: O(V + E) for storing the graph.

19. **Dynamic Programming**:
    - Explanation: Dynamic programming solves problems by breaking them down into smaller overlapping subproblems and storing the results to avoid redundant computation.
    - Time Complexity: Depends on the specific problem and the complexity of the recurrence relation.
    - Space Complexity: Depends on the specific problem and the size of the problem space.

20. **Backtracking Algorithms**:
    - Explanation: Backtracking is a technique for solving problems by recursively trying all possible options and backtracking when the solution fails.
    - Time Complexity: Depends on the specific problem and the search space.
    - Space Complexity: Depends on the specific problem and the depth of the recursion tree.

21. **Huffman Compression Algorithm**:
    - Explanation: Huffman compression algorithm is used for lossless data compression by constructing a variable-length prefix code based on the frequency of occurrence of each character in the data.
    - Time Complexity: O(n log n) for constructing the Huffman tree, where n is the number of distinct characters.
    - Space Complexity: O(n) for storing the Huffman tree.
