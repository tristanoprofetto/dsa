"""
Minimum Waiting Time - Easy

Given a non-empty array of positive integers, where each number represents the time for a query to execute
Write a function that returns the minimum waiting time

Optimal Time Complexity: O(n logN)
Optimal Space Complexity: O(n)
"""

def min_wait_time(queries):
    queries.sort()
    time = 0
    for q, n in zip(range(len(queries)), reversed(range(len(queries)))):
        time += n * queries[q]
    
    return time


if __name__ == "__main__":
    queries = []
    min_wait_time(queries)