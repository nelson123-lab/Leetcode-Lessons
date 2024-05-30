Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly useful for optimization problems where the solution can be constructed efficiently from the solutions of overlapping subproblems.

### Key Concepts in Dynamic Programming

1. **Optimal Substructure**: A problem exhibits optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. This means that you can solve the overall problem optimally by solving its subproblems optimally.

2. **Overlapping Subproblems**: This occurs when the problem can be broken down into subproblems which are reused several times. Dynamic programming takes advantage of this property by solving each subproblem only once and storing the results for future reference, rather than solving the same subproblem multiple times.

### Steps in Dynamic Programming

1. **Characterize the Structure of an Optimal Solution**: Determine how an optimal solution to the problem can be constructed from optimal solutions to subproblems.
   
2. **Define the Value of an Optimal Solution Recursively**: Write down a recursive formula that describes the value of the optimal solution in terms of the values of smaller subproblems.

3. **Compute the Value of an Optimal Solution (Memoization or Tabulation)**:
   - **Memoization**: This is a top-down approach where you solve the problem recursively and store the results of subproblems in a table to avoid redundant calculations.
   - **Tabulation**: This is a bottom-up approach where you solve all subproblems in an iterative manner and store their results in a table. 

4. **Construct the Optimal Solution from Computed Values**: If required, use the information stored in the table to reconstruct the optimal solution.

### Examples of Dynamic Programming

1. **Fibonacci Sequence**: The classic example where the nth Fibonacci number can be found efficiently using dynamic programming by storing previously computed values.

2. **Knapsack Problem**: Given a set of items with specific weights and values, determine the maximum value that can be obtained by selecting items without exceeding the weight limit.

3. **Shortest Path Problems**: Algorithms like Floyd-Warshall for finding shortest paths in a graph can be solved using dynamic programming.

4. **Longest Common Subsequence**: Given two sequences, find the longest subsequence present in both of them. This problem can be efficiently solved using dynamic programming.

### Example: Fibonacci Sequence

The Fibonacci sequence is defined as:
\[ F(n) = F(n-1) + F(n-2) \]
with base cases:
\[ F(0) = 0, F(1) = 1 \]

Using dynamic programming, you can avoid redundant calculations as follows:

#### Memoization (Top-Down Approach)

```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

print(fibonacci_memo(10))  # Output: 55
```

#### Tabulation (Bottom-Up Approach)

```python
def fibonacci_tab(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

print(fibonacci_tab(10))  # Output: 55
```
