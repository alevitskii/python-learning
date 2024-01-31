def find_followers(vertex, graph, followers):
    for neighbour in graph[vertex]:
        if neighbour not in followers:
            followers.add(neighbour)
            find_followers(neighbour, graph, followers)


def can_finish_dfs(n, prerequisites):
    graph = [[] for _ in range(n)]
    for main, prerequisite in prerequisites:
        graph[prerequisite].append(main)
    for vertex in range(n):
        followers = set()
        find_followers(vertex, graph, followers)
        if vertex in followers:
            return False
    return True


# T: O(p+n**3), S: O(n**2)
def can_finish_bfs(n, prerequisites):
    graph = [[] for _ in range(n)]
    for main, prerequisite in prerequisites:
        graph[prerequisite].append(main)
    for vertex in range(n):
        queue, seen = graph[vertex], set()
        while queue:
            current = queue.pop()
            seen.add(current)
            if current == vertex:
                return False
            for next in graph[current]:
                if next not in seen:
                    queue.append(next)
    return True


def can_finish_top_sort(n, prerequisites):
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for main, prerequisite in prerequisites:
        graph[prerequisite].append(main)
        indegree[main] += 1
    while True:
        for vertex in range(n):
            if indegree[vertex] == 0:
                for neighbour in graph[vertex]:
                    indegree[neighbour] -= 1
                indegree[vertex] = -1
                break
        else:
            break
    return all([i <= 0 for i in indegree])


# T: O(p+E) (E - number of edges) ~ O(p+n**2), S: O(n**2)
def can_finish_top_sort_2(n, prerequisites):
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for main, prerequisite in prerequisites:
        graph[prerequisite].append(main)
        indegree[main] += 1
    stack = []
    for i in range(n):
        if indegree[i] == 0:
            stack.append(i)
    count = 0
    while stack:
        current = stack.pop()
        count += 1
        for neighbour in graph[current]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                stack.append(neighbour)
    return count == n


if __name__ == "__main__":
    inputs = [
        # (6, [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]),
        # (7, [[0, 3], [1, 0], [2, 1], [4, 5], [6, 4], [5, 6]]),
        # (0, []),
    ]
    for n, prerequisites in inputs:
        # print(can_finish_dfs(n, prerequisites))
        # print(can_finish_bfs(n, prerequisites))
        print(can_finish_top_sort(n, prerequisites))
        # print(can_finish_top_sort_2(n, prerequisites))
