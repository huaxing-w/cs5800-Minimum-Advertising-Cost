from follow_network import FollowNetwork
from random_graph import RandomDirectedGraph
from typing import Set, List, Tuple
from user import User
from synthetic import validate_solution

# import the Twitter data
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

# mean followers
print(statistics.mean(
    [len(i.follower) for i in id_to_user.values()]
))

# standard deviation of follwers
print(statistics.pstdev(
    [len(i.follower) for i in id_to_user.values()]
))

# standard deviation of following
statistics.pstdev(
    [len(i.following) for i in id_to_user.values()]
)

s = FollowNetwork(list(id_to_user.values()))
res = set(s.solve())

# number of influencers
print(len(res))

# certify the optimality
validate_solution(set([id_to_user[i] for i in res]), len(nodes))
