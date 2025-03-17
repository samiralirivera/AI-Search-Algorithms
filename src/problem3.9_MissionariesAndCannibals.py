"""
Description:
This code implements a solution to the Missionaries and Cannibals problem using Breadth-First Search (BFS).
The goal is to move three missionaries and three cannibals across a river using a boat that can hold up to two people,
while ensuring that at no point are the missionaries outnumbered by the cannibals on either side of the river.

Key Features:
- Uses BFS to find the shortest path from the initial state (3,3,1) to the goal state (0,0,0).
- Ensures valid state transitions to avoid failure states.
- Outputs the sequence of moves needed to solve the problem optimally.
"""
from collections import deque

class MissionariesAndCannibals:
    def __init__(self):
        self.initial_state = (3, 3, 1)  # (Missionaries on left, Cannibals on left, Boat position)
        self.goal_state = (0, 0, 0)     # (All on the right side)

    def is_valid(self, state):
        m, c, _ = state
        if not (0 <= m <= 3 and 0 <= c <= 3):
            return False
        if (m > 0 and m < c) or (3 - m > 0 and 3 - m < 3 - c):
            return False
        return True
    
    def get_successors(self, state):
        missionaries, cannibals, boat = state
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        successors = []
        
        for m, c in moves:
            new_state = (missionaries - m * boat, cannibals - c * boat, 1 - boat)
            if self.is_valid(new_state):
                successors.append((new_state, (m, c)))
        
        return successors
    
    def breadth_first_search(self):
        queue = deque([(self.initial_state, [])])
        visited = set()
        
        while queue:
            state, path = queue.popleft()
            if state == self.goal_state:
                return path
            
            if state not in visited:
                visited.add(state)
                for successor, action in self.get_successors(state):
                    queue.append((successor, path + [action]))
        
        return None

# Solve the problem
problem = MissionariesAndCannibals()
solution = problem.breadth_first_search()
print("Solution:", solution)
