# Google Question : Find all ways in Binary Search Tree by removing leaf nodes

def findAllTopologicalOrdering(edges):
    indegree, graph = defaultdict(int), defaultdict(list) 
    result, ans = [], set()

    for i,j in edges:
        # All topological ordering
        graph[i].append(j)
        indegree[j] += 1 
        
        # Find all ways to remove nodes from leaf (Binary Tree)
        # graph[j].append(i)
        # indegree[i] += 1 
        ans.add(i)
        ans.add(j)

    n = len(ans)
    def backtrack(path, visited):
        if len(path) == n:
            result.append(list(path))   # add new copy of list

        for node in range(1, n+1):
            if indegree[node] == 0 and node not in visited:

                for neighbor in graph[node]:
                    indegree[neighbor] -= 1 

                path.append(node)
                visited.add(node)

                backtrack(path, visited)

                for neighbor in graph[node]:
                    indegree[neighbor] += 1 

                path.pop()
                visited.remove(node)

    backtrack([], set())

    return result 

edges = [[1,2],[1,3],[2,4]]
print(*findAllTopologicalOrdering(edges), sep="\n")

edges = [[1,2],[1,3],[2,4],[2,5]]
print(*findAllTopologicalOrdering(edges), sep="\n")
