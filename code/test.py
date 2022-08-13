from follow_network import FollowNetwork
from random_graph import RandomDirectedGraph
from typing import Set, List, Tuple
from user import User


# test case 1
# a=User(0)
# b=User(1)
# c=User(2)
# d=User(3)
# e=User(4)
#
# d.followOne(a)
# e.followOne(d)
# a.followOne(b)
# b.followOne(c)
# c.followOne(a)

# s=scc([a, b, c, d, e])
#
# print(s.solve())
#
#
# huaxing=User(0)
# sisi=User(1)
# yuxiao=User(2)
# yufei=User(3)
#
# huaxing.followOne(sisi)
# sisi.followOne(yuxiao)
# yuxiao.followOne(yufei)

# v=scc([huaxing, sisi, yuxiao, yufei])
# print(v.solve())

# start dfs from all the influencer the advi
# if all the nodes visited without

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


result_file_path = "erdos_renyi_results_2.csv"
parameter_sets = [
    (i, j) for i in (10, 20, 50, 100, 200, 500)
    for j in (1E-4, 1E-3, 2E-3, 5E-3, 0.01, 0.02, 0.05, 0.1)
] + [
    (i, j) for i in (1000, 2000, 5000, 10000)
    for j in (1E-6, 1E-5, 1E-4, 2E-4, 5E-4, 1E-3)
]

n_folds = 100


import sys
sys.setrecursionlimit(1000000000)

# for i in range(100):
#     n = 1000
#     p = 0.002
#     graph_1 = RandomDirectedGraph(n, p)
#     graph_1.generate_erdos_renyi_graph()
#     s = FollowNetwork([i for i in graph_1.erdos_graph.values()])
#     influencers = s.solve()
#     valid_1, valid_2 = [int(x) for x in validate_solution([graph_1.erdos_graph[i] for i in influencers], n)]
#     num_edges, mean_degree, std_num_follower, std_num_following = graph_1.num_edges(), graph_1.mean_degree(), graph_1.std_num_follower(), graph_1.std_num_following()
#     print(f"{len(influencers)},{valid_1},{valid_2},{n},{p},{num_edges},{mean_degree},{std_num_follower},{std_num_following}")

with open(result_file_path, "a") as file: # MUST USE append mode!
    file.write("n_influencers,valid_1,valid_2,n,p,num_edges,mean_degrees,std_num_followers,std_num_followings\n")
    for (idx, (n, p)) in enumerate(parameter_sets):
        for fold in range(n_folds):
            print(f"param {idx}, fold {fold}: {n}, {p}" + " "*50, end='\r')
            graph_1 = RandomDirectedGraph(n, p)
            graph_1.generate_erdos_renyi_graph()
            s = FollowNetwork([i for i in graph_1.erdos_graph.values()])
            influencers = set(s.solve())
            valid_1, valid_2 = [int(x) for x in validate_solution([graph_1.erdos_graph[i] for i in influencers], n)]
            num_edges, mean_degree, std_num_follower, std_num_following = graph_1.num_edges(), graph_1.mean_degree(), graph_1.std_num_follower(), graph_1.std_num_following()
            file.write(
                f"{len(influencers)},{valid_1},{valid_2},{n},{p},{num_edges},{mean_degree},{std_num_follower},{std_num_following}\n",
            )
            file.flush()