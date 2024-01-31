def traversal_bfs(graph):
    queue = [0]
    values, seen = [], set()
    while queue:
        vertex = queue.pop(0)
        values.append(vertex)
        seen.add(vertex)
        for connection in graph[vertex]:
            if connection not in seen:
                queue.append(connection)
    return values


def traversal_dfs(vertex, graph, values, seen):
    values.append(vertex)
    seen.add(vertex)
    for connection in graph[vertex]:
        if connection not in seen:
            traversal_dfs(connection, graph, values, seen)


if __name__ == "__main__":
    inputs = [[[1, 3], [0], [3, 8], [0, 2, 4, 5], [3, 6], [3], [4, 7], [6], [2]]]
    for graph in inputs:
        print(traversal_bfs(graph))
        values = []
        print(traversal_dfs(0, graph, values, set()))
        print(values)
