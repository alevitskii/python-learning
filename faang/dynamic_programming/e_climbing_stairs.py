# T: O(n), S: O(1)
def min_cost_climbing_stairs_bottom_up(cost):
    cost.append(0)
    for step in range(2, len(cost)):
        cost[step] = min(cost[step - 2], cost[step - 1]) + cost[step]
    return cost[-1]


# T: O(n), S: O(1)
def min_cost_climbing_stairs_bottom_up_2(cost):
    if len(cost) <= 1:
        return 0
    first, second = cost[0], cost[1]
    for step in range(2, len(cost)):
        first, second = second, min(first, second) + cost[step]
    return min(first, second)


# T: O(2**n), S: O(n)
def min_cost_climbing_stairs_top_down(cost):
    def min_cost(i, cost):
        if i < 0:
            return 0
        if i in {0, 1}:
            return cost[i]
        return cost[i] + min(min_cost(i - 1, cost), min_cost(i - 2, cost))

    return min(min_cost(len(cost) - 1, cost), min_cost(len(cost) - 2, cost))


# T: O(n), S: O(n)
def min_cost_climbing_stairs_top_down_memo(cost):
    def min_cost(i, cost, dp):
        if i < 0:
            return 0
        if i in {0, 1}:
            return cost[i]
        if i in dp:
            return dp[i]
        dp[i] = cost[i] + min(min_cost(i - 1, cost, dp), min_cost(i - 2, cost, dp))
        return dp[i]

    dp = {}
    return min(min_cost(len(cost) - 1, cost, dp), min_cost(len(cost) - 2, cost, dp))


if __name__ == "__main__":
    inputs = [[10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], [], [1], [3, 2]]
    for cost in inputs:
        # print(min_cost_climbing_stairs_bottom_up(cost))
        print(min_cost_climbing_stairs_bottom_up_2(cost))
        # print(min_cost_climbing_stairs_top_down(cost))
        # print(min_cost_climbing_stairs_top_down_memo(cost))
