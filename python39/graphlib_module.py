from graphlib import TopologicalSorter


def main() -> None:
    graph = {"D": {"B", "C"}, "C": {"A"}, "B": {"A"}}
    ts = TopologicalSorter(graph)
    print(tuple(ts.static_order()))


if __name__ == "__main__":
    main()
