import heapq

def Dijkstra(graph, start):
    n = len(graph)
    
    # initialize all node distances as infinite
    dist = [float("inf")]*n
    dist[start] = 0
    
    # create a list that indicates if a node is visited or not
    visited = [False]*n
    
    # creating a priority queue
    pqueue = [(0, start)]

    while pqueue:
        cur_d, cur_node = heapq.heappop(pqueue)
        
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        
        for next_node, d in graph[cur_node]:
            if (cur_d + d) < dist[next_node]:
                dist[next_node] = (cur_d + d)
                heapq.heappush(pqueue, (dist[next_node], next_node))

    return dist

graph = { 
    0: [(1, 4), (2, 5), (3, 6), (4, 7)],
    1: [(0, 1)],
    2: [(0, 5), (3, 8), (4, 4)],
    3: [(0, 6), (2, 8), (4, 2)],
    4: [(0, 7), (2, 4), (3, 2)]
}
print(Dijkstra(graph, 1))