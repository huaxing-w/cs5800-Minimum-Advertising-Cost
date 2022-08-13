from follow_network import FollowNetwork
from random_graph import RandomDirectedGraph
from typing import Set, List, Tuple
from user import User

import test
def validate_solution(all_influencers: Set[User], num_users: int) -> Tuple[bool, bool]:
    """
    :param all_influencers:
    :param num_users:
    :return:
    """
    all_influencers = set(all_influencers)

    visited_global = set()
    visited_local = {}

    valid = True

    def dfs(node, start):
        nonlocal valid
        if not valid:
            return
        if node in all_influencers and node != start:
            valid = False
            # print("invalid!!!")
            return
        if node in visited_local[start]:
            return
        visited_local[start].add(node)
        visited_global.add(node)

        for next_node in node.follower:
            dfs(next_node, start)

    for influencer in all_influencers:
        visited_local[influencer] = set()
        dfs(influencer, influencer)

    return valid, num_users == len(visited_global)

dataset_file_path = "out.ego-twitter.txt"

with open(dataset_file_path, "r") as file:
    raw_data = file.readlines()
    raw_data = [line.strip() for line in raw_data]
    raw_data = [line for line in raw_data if not line.startswith(r"%")]
    twitter_data = [line.split('\t') for line in raw_data]
    twitter_data = [[int(i) for i in j] for j in twitter_data]

nodes = set(i for j in twitter_data for i in j)
id_to_user = {
    i: User(i) for i in nodes
}
for (i, j) in twitter_data:
    id_to_user[j].follow_one(id_to_user[i])

import statistics
import scipy.stats

statistics.pstdev(
    [len(i.follower) for i in id_to_user.values()]
)

statistics.pstdev(
    [len(i.following) for i in id_to_user.values()]
)



s = FollowNetwork(list(id_to_user.values()))

res = set(s.solve())

validate_solution(set([id_to_user[i] for i in res]), len(nodes))

statistics.pstdev(
    [len(id_to_user[i].following) for i in res]
)

statistics.pstdev(
    [len(id_to_user[i].follower) for i in res]
)
