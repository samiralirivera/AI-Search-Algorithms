"""
polygon_search.py

This module implements the search problem for Problem 3.7 parts (c) and (d):
  - It defines a PolygonProblem class that models a search problem over polygon vertices.
  - The ACTIONS function returns valid vectors (moves) from the current vertex to all reachable neighbors,
    including adjacent vertices on the same polygon.
  - The heuristic function is the straight-line (Euclidean) distance to the goal.
  - The module applies A* search and BFS graph search from the Berkeley code to solve an example problem,
    and visualizes the results using matplotlib.
"""

import math
import matplotlib.pyplot as plt
from berkeley_ai.search import Problem, astar_search, breadth_first_graph_search

# --- Helper Function for Geometry ---

def segments_intersect(p1, q1, p2, q2):
    """Return True if line segments p1q1 and p2q2 intersect."""
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if abs(val) < 1e-9:
            return 0
        return 1 if val > 0 else 2

    def on_segment(p, q, r):
        return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True
    return False

# --- Polygon Search Problem Implementation ---

class PolygonProblem(Problem):
    """
    A search problem for finding a path from a start vertex to a goal vertex in a plane
    with polygonal obstacles.

    States are vertices represented as (x, y) tuples.
    Actions are vectors (dx, dy) that map the current vertex to a reachable neighbor.
    The heuristic is the Euclidean distance to the goal.
    """

    def __init__(self, start, goal, vertices, polygons):
        """
        :param start: Starting vertex (x, y)
        :param goal: Goal vertex (x, y)
        :param vertices: List of all vertices (x, y) in the scene.
        :param polygons: List of polygons, each polygon is a list of vertices (subset of vertices).
        """
        super().__init__(start, goal)
        self.vertices = vertices
        self.polygons = polygons
        self.graph = self.build_graph()

    def build_graph(self):
        """
        Build a graph (as a dict) mapping each vertex to its set of reachable neighbors.
        Neighbors are:
          - Adjacent vertices on the same polygon.
          - Other vertices reachable in a straight line (with no intersecting obstacle).
        """
        graph = {v: set() for v in self.vertices}
        # Connect neighbors on the same polygon.
        for poly in self.polygons:
            n = len(poly)
            for i in range(n):
                v1 = poly[i]
                v2 = poly[(i + 1) % n]
                graph[v1].add(v2)
                graph[v2].add(v1)
        # Connect vertices across polygons if the line is clear.
        for i, v in enumerate(self.vertices):
            for j, u in enumerate(self.vertices):
                if i == j:
                    continue
                if u in graph[v]:
                    continue  # Already connected as polygon neighbors.
                if self.line_clear(v, u):
                    graph[v].add(u)
        return graph

    def line_clear(self, v, u):
        """
        Return True if the straight-line segment from v to u does not intersect any polygon edge.
        Endpoints that coincide with v or u are ignored.
        """
        for poly in self.polygons:
            n = len(poly)
            for i in range(n):
                p1 = poly[i]
                p2 = poly[(i + 1) % n]
                # Skip if the edge is incident to v or u.
                if p1 == v or p1 == u or p2 == v or p2 == u:
                    continue
                if segments_intersect(v, u, p1, p2):
                    return False
        return True

    def actions(self, state):
        """
        Given a state (vertex), return a set of actions.
        Each action is a vector (dx, dy) that maps the state to a reachable neighbor.
        """
        neighbors = self.graph.get(state, set())
        return {(nb[0] - state[0], nb[1] - state[1]) for nb in neighbors}

    def result(self, state, action):
        """
        Apply the action (a vector) to the state and return the new state.
        """
        dx, dy = action
        return (state[0] + dx, state[1] + dy)

    def path_cost(self, c, state1, action, state2):
        """
        Increment the path cost by the Euclidean distance corresponding to the action.
        """
        dx, dy = action
        return c + math.hypot(dx, dy)

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        """
        Heuristic: straight-line distance from the current state to the goal.
        Accepts either a state tuple or a Node (in which case, use node.state).
        """
        # If node has an attribute 'state', extract it; otherwise assume node is a state.
        if hasattr(node, 'state'):
            state = node.state
        else:
            state = node
        return math.hypot(self.goal[0] - state[0], self.goal[1] - state[1])

# --- Visualization Function ---

def visualize_polygon_problem(problem, path, title="Polygon Search Solution"):
    """
    Visualize the polygon problem by plotting:
      - The polygons (obstacles)
      - All vertices (blue dots)
      - Start (green) and goal (red)
      - The solution path (red dashed line)
    """
    plt.figure(figsize=(8, 6))
    # Plot each polygon.
    for poly in problem.polygons:
        xs = [v[0] for v in poly] + [poly[0][0]]
        ys = [v[1] for v in poly] + [poly[0][1]]
        plt.plot(xs, ys, 'k-', linewidth=2)
    # Plot all vertices.
    xs_all = [v[0] for v in problem.vertices]
    ys_all = [v[1] for v in problem.vertices]
    plt.scatter(xs_all, ys_all, c='blue', s=50, label="Vertices")
    # Mark start and goal.
    plt.scatter(problem.initial[0], problem.initial[1], c='green', s=100, label="Start")
    plt.scatter(problem.goal[0], problem.goal[1], c='red', s=100, label="Goal")
    # Plot the solution path.
    if path:
        path_x = [v[0] for v in path]
        path_y = [v[1] for v in path]
        plt.plot(path_x, path_y, 'r--', linewidth=3, label="Solution Path")
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()

# --- Main Function for Testing and Performance Analysis ---

def main():
    """
    Create a sample PolygonProblem instance, solve it using A* search and BFS graph search,
    and visualize the solutions.
    """
    # Define two simple polygons (as obstacles).
    poly1 = [(2, 2), (4, 2), (4, 4), (2, 4)]
    poly2 = [(6, 6), (8, 6), (8, 8), (6, 8)]
    # Define the overall set of vertices: union of polygon vertices plus start and goal.
    vertices = set(poly1 + poly2)
    start = (0, 0)
    goal = (10, 10)
    vertices.add(start)
    vertices.add(goal)
    vertices = list(vertices)
    polygons = [poly1, poly2]

    # Create the problem instance.
    problem = PolygonProblem(start, goal, vertices, polygons)

    # Solve with A* search.
    solution_node_astar = astar_search(problem, problem.h)
    if solution_node_astar:
        path_astar = [node.state for node in solution_node_astar.path()]
        print("A* Search Solution Path:")
        for state in path_astar:
            print(state)
        print("Total Path Cost:", solution_node_astar.path_cost)
        visualize_polygon_problem(problem, path_astar, "A* Search Solution")
    else:
        print("No solution found using A* search.")

    # Solve with Breadth-First Graph Search.
    solution_node_bfs = breadth_first_graph_search(problem)
    if solution_node_bfs:
        path_bfs = [node.state for node in solution_node_bfs.path()]
        print("BFS Graph Search Solution Path:")
        for state in path_bfs:
            print(state)
        print("Total Path Cost:", solution_node_bfs.path_cost)
        visualize_polygon_problem(problem, path_bfs, "BFS Graph Search Solution")
    else:
        print("No solution found using BFS graph search.")

if __name__ == "__main__":
    main()
