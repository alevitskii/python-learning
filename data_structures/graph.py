class Graph:
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def show_connections(self):
        all_nodes = self.adjacent_list.keys()

        for node in all_nodes:
            node_connections = self.adjacent_list[node]
            connections = ""

            for vertex in node_connections:
                connections += vertex + " "

            print(node + " --> " + connections)


def main() -> None:
    graph = Graph()
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_vertex("4")
    graph.add_vertex("5")
    graph.add_vertex("6")
    graph.add_edge("3", "1")
    graph.add_edge("3", "4")
    graph.add_edge("4", "2")
    graph.add_edge("4", "5")
    graph.add_edge("1", "2")
    graph.add_edge("1", "0")
    graph.add_edge("0", "2")
    graph.add_edge("6", "5")

    graph.show_connections()


if __name__ == "__main__":
    main()
