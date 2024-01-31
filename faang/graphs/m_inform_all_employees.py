def dfs(graph, idx, inform_time, time):
    times = [dfs(graph, subord, inform_time, time + inform_time[idx]) for subord in graph[idx]]
    return max(times) if times else time


def number_of_minutes(n, head_id, managers, inform_time):
    graph = [[] for _ in range(n)]
    for employee_idx in range(len(managers)):
        if managers[employee_idx] != -1:
            graph[managers[employee_idx]].append(employee_idx)
    return dfs(graph, head_id, inform_time, 0)


def dfs_2(idx, graph, inform_time):
    if len(graph[idx]) == 0:
        return 0
    max_time = 0
    for subord in graph[idx]:
        max_time = max(max_time, dfs_2(subord, graph, inform_time))
    return max_time + inform_time[idx]


# T: O(3n) ~ O(n), S: O(3n) ~ O(n)
def number_of_minutes_2(n, head_id, managers, inform_time):
    graph = [[] for _ in range(n)]
    for employee_idx in range(len(managers)):
        if managers[employee_idx] != -1:
            graph[managers[employee_idx]].append(employee_idx)
    return dfs_2(head_id, graph, inform_time)


if __name__ == "__main__":
    inputs = [
        (8, 4, [2, 2, 4, 6, -1, 4, 4, 5], [0, 0, 4, 0, 7, 3, 6, 0]),  # 13
        (1, 0, [-1], [0]),  # 0
        (7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]),  # 21
    ]
    for n, head_id, managers, inform_time in inputs:
        print(number_of_minutes(n, head_id, managers, inform_time))
        print(number_of_minutes_2(n, head_id, managers, inform_time))
