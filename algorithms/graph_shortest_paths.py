import heapq
from math import inf


# T: O(2V+E+E*logV+V*logV) ~ O(E*logV+V*logV) ~~ O(E*logV), S: O(E+V)
# If the priority queue allows for duplicate nodes: T: O(E*logE), S: O(2E) ~ O(E)
def network_delay_time_dijkstra(n, k, times):
    distances = n * [inf]
    distances[k - 1] = 0
    heap = []
    heapq.heappush(heap, k - 1)
    graph = [[] for _ in range(n)]
    for i, j, w in times:
        graph[i - 1].append([j - 1, w])
    while heap:
        current_vertex = heapq.heappop(heap)
        for neighbour, weight in graph[current_vertex]:
            if distances[current_vertex] + weight < distances[neighbour]:
                distances[neighbour] = distances[current_vertex] + weight
                heapq.heappush(heap, neighbour)
    return -1 if (answer := max(distances)) == inf else answer


# T: O(V+V*E) ~ O(V*E), S: O(V)
def network_delay_time_bellman_ford(n, k, times):
    distances = n * [inf]
    distances[k - 1] = 0
    for _ in range(n - 1):
        count = 0
        for src, dst, weight in times:
            if distances[src - 1] + weight < distances[dst - 1]:
                distances[dst - 1] = distances[src - 1] + weight
                count += 1
        if count == 0:
            break
    return -1 if (answer := max(distances)) == inf else answer


def main() -> None:
    inputs = [
        (5, 1, [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]),  # 14
        (3, 2, [[2, 3, 4]]),  # -1
        (3, 1, [[1, 2, 8], [3, 2, 3]]),  # -1
    ]
    for n, k, times in inputs:
        print(network_delay_time_dijkstra(n, k, times))
        print(network_delay_time_bellman_ford(n, k, times))


if __name__ == "__main__":
    main()
