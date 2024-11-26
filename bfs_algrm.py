import collections

def bfs(graph, root):
    visited = set()  
    queue = collections.deque([root])  
    visited.add(root)
    
    while queue:  
        vertex = queue.popleft()
        print(str(vertex) + " ", end=" ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {0: [2, 3], 1: [3], 2: [1], 3: [2, 1]}
    print("Following is Breadth First Traversal:")
    bfs(graph, 0)
