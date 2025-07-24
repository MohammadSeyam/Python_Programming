# dfs function
def dfs(graph,node,res,visited):
    visited[node]=1
    res.append(node)
    for i in graph[node]:
        if visited[i]!=1:
            dfs(graph,i,res,visited)
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
res = []
number_of_nodes = 7
visited = [0] * number_of_nodes
start = 0

dfs(graph,start,res,visited)
print(res)


# requirements
"""
* One graph
* result array
* visited array
* starting node
"""