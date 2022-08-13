import networkx
from user import User
import statistics

class RandomDirectedGraph:
    def __init__(self, num_nodes: int, probability: float) -> None:
        self.num_nodes = num_nodes
        self.probability = probability
        self.erdos_graph = dict()

    def generate_erdos_renyi_graph(self) -> None:
        erdos = networkx.erdos_renyi_graph(n=self.num_nodes, p=self.probability, directed=True)
        id_to_user = {
            i: User(i) for i in erdos.nodes
        }
        for edge in erdos.edges:
            id_to_user[edge[0]].follow_one(id_to_user[edge[1]])

        self.erdos_graph = id_to_user

    def num_edges(self):
        return sum(len(i.following) for i in self.erdos_graph.values())

    def mean_degree(self):
        return 1. * self.num_edges() / self.num_nodes

    def std_num_following(self):
        return statistics.pstdev(
            [len(i.following) for i in self.erdos_graph.values()]
        )

    def std_num_follower(self):
        return statistics.pstdev(
            [len(i.follower) for i in self.erdos_graph.values()]
        )