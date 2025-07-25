import heapq

def dijkstra(graph,d,pq):
    while pq:
        curr_dis_of_u,u = heapq.heappop(pq)
        if curr_dis_of_u > d[u]:
            continue
        for v,w in graph[u]:
            if d[u]+w < d[v]:
                d[v] = d[u]+w
                heapq.heappush(pq, ([d[v],v]))

graph={
    1 : [[2,10],[3,5]],   # node : node2, weight / u : [v,w]
    2 : [[4,1]],
    3 : [[2,3],[4,9],[5,2]],
    4 : [],
    5 : [[4,6],[1,2]]
}

#distance array
d = [float("inf")] * 6
d[1]=0
src = 1

#priority_queue
pq = [[0,src]]

dijkstra(graph,d,pq)
print(d[3])

# requirements
"""
* Graph
* distance array
* priority queue
"""
# time complexity = o(ElogV)
