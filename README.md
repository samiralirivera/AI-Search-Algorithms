# **University of Puerto Rico at Mayagüez**  
### **Department of Electrical and Computer Engineering**  
#### **ICOM5015 - Artificial Intelligence**  

**Project Title:** AI Search Algorithms & Negative Step Costs  
**Assignment:** Programming Homework – Chapter 3 (Problems 3.7 & 3.9)  

**Team:** Group M  
- **Marco Yu** (Undergraduate, Computer Science)  
- **Samir Rivera** (Undergraduate, Software Engineering)  
- **Lex Feliciano** (Undergraduate, Electrical and Computer Engineering)  
- **Shadiel López** (Undergraduate, Computer Engineering)  

**Professor:** J. Fernando Vega Riveros  
**Date:** March 19, 2025  

<p align="center">
  <img src="https://www.uprm.edu/wdt/resources/seal-rum-uprm-1280x1280px.png" alt="UPRM Logo" width="250" height="250">
</p>

---

# **AI Search Algorithms & Negative Step Costs**  
**Implementation and Analysis of Search Algorithms (Problems 3.7 & 3.9)**  
*(Based on Russell & Norvig, *Artificial Intelligence: A Modern Approach*, 3rd Edition, and UC Berkeley AI Repository)*  

---

## 📖 **Overview & Purpose**

This project implements and analyzes **state-space search algorithms** to solve **Problems 3.7 and 3.9** from *Artificial Intelligence: A Modern Approach (3rd Edition)*. The assignment focuses on search strategies in AI, including the impact of **negative step costs** on search algorithms.

**Core AI Concepts Applied:**  
- **Uninformed Search:** Breadth-First Search (BFS), Depth-First Search (DFS), Uniform-Cost Search (UCS)  
- **Informed Search:** A* Algorithm with heuristic functions  
- **Graph Search vs. Tree Search:** Optimizing search efficiency  
- **Negative Weight Handling:** Bellman-Ford Algorithm, Johnson’s Algorithm  

---

## **📂 Assignment Breakdown**

### **Problem 3.7: Search Strategies & State-Space Representation**
- Implement **BFS, DFS, UCS, and A\*** search algorithms.
- Compare **tree search vs. graph search** in efficiency and optimality.
- Evaluate search performance on different problem instances.

### **Problem 3.9: Handling Negative Step Costs**
- Investigate the **impact of negative weights** on search algorithms.
- Implement **Bellman-Ford Algorithm** for shortest paths with negative weights.
- Use **Johnson’s Algorithm** to handle graphs with negative edges efficiently.
- **Detect and handle negative weight cycles** (where no optimal solution exists).

These problems illustrate how search algorithms operate under **different constraints** and how **negative costs introduce challenges** in traditional search strategies.

---

## **📂 Repository Structure**

```
AI-Search-Algorithms/
│── 📄 README.md               # Project Overview & Documentation
│── 📄 LICENSE                 # Open-source license (MIT)
│── 📄 .gitignore               # Ignore unnecessary files
│── 📁 src/                     # Source code for search algorithms
│   │── bfs_dfs.py              # BFS & DFS implementations
│   │── ucs_astar.py            # UCS & A* implementations
│   │── bellman_ford.py         # Bellman-Ford Algorithm for negative weights
│   │── johnson.py              # Johnson's Algorithm for reweighting graphs
│   │── problem.py              # Problem definitions (state-space representation)
│   │── main.py                 # Entry point for running search algorithms
│── 📁 notebooks/               # Jupyter Notebook with analysis
│   │── AI_Search_Report.ipynb  # Report including explanations and code
│── 📁 tests/                   # Unit tests for algorithms
│   │── test_search.py          # Verifies correctness of implemented searches
│── 📁 reports/                 # Assignment analysis and findings
│   │── problem_analysis.md     # Detailed breakdown of Problems 3.7 & 3.9
│   │── experiment_results.md   # Performance evaluation of search methods
│── 📁 presentations/           # Video and slides for assignment
│   │── slides.pptx             # PowerPoint Presentation
│   │── video_link.txt          # Link to recorded video submission
│── 📁 data/                    # Sample problem instances (if applicable)
│── 📁 docs/                    # Additional documentation
```

---

## **🛠️ Installation & Setup**

### **🔹 Prerequisites**
- Python 3.8+
- Jupyter Notebook
- Required Libraries: `numpy`, `matplotlib`, `heapq`

### **🔹 Installation**
1. **Clone or Download the Repository**  
```bash
git clone https://github.com/YOUR_USERNAME/AI-Search-Algorithms.git
cd AI-Search-Algorithms
```
2. **Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## **🚀 Running the Code**
### **1️⃣ Running BFS & DFS**
```bash
python src/bfs_dfs.py
```
### **2️⃣ Running UCS & A\***
```bash
python src/ucs_astar.py
```
### **3️⃣ Running Bellman-Ford Algorithm**
```bash
python src/bellman_ford.py
```
### **4️⃣ Running Johnson’s Algorithm**
```bash
python src/johnson.py
```

### **Running Jupyter Notebook**
```bash
jupyter notebook notebooks/AI_Search_Report.ipynb
```

---

## **📊 Performance Evaluation & Analysis**
### **Search Algorithm Comparisons**
Each algorithm is evaluated based on:
1. **Time Complexity:** Number of node expansions.
2. **Space Complexity:** Memory required for frontier/explored sets.
3. **Optimality:** Whether the algorithm guarantees the shortest path.

### **Handling Negative Step Costs**
- **Bellman-Ford Algorithm** detects and handles negative weights.
- **Johnson’s Algorithm** reweights graphs for efficient shortest path calculations.
- **Performance Comparison:** Time complexity of Bellman-Ford \(O(VE)\) vs. Johnson’s \(O(VE + V\log V)\).

---

## **📖 Grading Criteria & Alignment**
This project meets the grading criteria through:

| **Criterion**          | **How Addressed** |
|----------------------|-----------------------------------------------------|
| **Problem Understanding** | Clearly defines Problems 3.7 & 3.9 with algorithmic solutions. |
| **Implementation Accuracy** | Implements BFS, DFS, UCS, A*, Bellman-Ford, and Johnson’s Algorithm correctly. |
| **Experimentation** | Tests search algorithms with various problem instances. |
| **Analysis & Reporting** | Includes performance comparisons, edge case analysis, and negative weight handling. |
| **Presentation Quality** | Professional README, structured codebase, and detailed Jupyter Notebook. |

---

## **🔹 Challenges, Lessons Learned & Future Work**
### **Challenges Encountered:**
- Handling negative weight cycles efficiently.
- Optimizing graph search to avoid redundant expansions.

### **Lessons Learned:**
- State-space representation is crucial for search efficiency.
- **Graph search significantly improves performance** over tree search.
- **Negative weights require specialized algorithms like Bellman-Ford.**

### **Future Work:**
- Extend A* with **better heuristics** for faster pathfinding.
- Implement **Bidirectional Search** to improve efficiency.
- Explore **hybrid approaches** for solving real-world search problems.

---

## **📖 References and Citations**
- **Textbook:**  
  Russell, S., & Norvig, P. *(2010). Artificial Intelligence: A Modern Approach* (3rd Edition).
- **Code Base:**  
  [UC Berkeley AI Repository](https://github.com/aimacode/aima-python)  
- **Research Papers & Additional Sources:**
  - Bellman-Ford Algorithm: [https://en.wikipedia.org/wiki/Bellman–Ford_algorithm](https://en.wikipedia.org/wiki/Bellman–Ford_algorithm)
  - Johnson’s Algorithm: [https://en.wikipedia.org/wiki/Johnson%27s_algorithm](https://en.wikipedia.org/wiki/Johnson%27s_algorithm)

---

## **🎯 Conclusion**
This project successfully implements and analyzes **search algorithms for AI**, particularly focusing on the **challenges of negative step costs**. By implementing **classical and advanced search methods**, this work provides **a detailed comparison** of their strengths and weaknesses.
