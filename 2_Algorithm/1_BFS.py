from collections import deque

#bfs function
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])
# end

graph = {
    0 : [1,2],
    1 : [3,4],
    2 : [5],
    4 : [5,6],
    3 : [],
    5 : [],
    6 : []
}

bfs(graph,0)

# Requirements
"""
* One Graph
* A starting point
* One visited set
* One Queue 
"""