from fractions import Fraction
from typing import Any, Callable

import matplotlib.pyplot as plt
import networkx as nx


def richman(val_max, val_min):
    return (val_max + val_min) / 2


def taxman(val_max, val_min):
    return (val_max + val_min - val_min * 0.5) / (2 - (1 + val_min - val_max) * 0.5)


def unfair_richman(val_max, val_min):
    return min(2 / 3 * val_max + 1 / 3 * val_min, (1 + val_min) / 2)


def co_unfair_richman(val_max, val_min):
    return max(1 / 3 * val_max + 2 / 3 * val_min, val_max / 2)


def value_iteration(G: nx.DiGraph, target: Any, calc_val: Callable[[float, float], float], iters: int = 1000) -> dict:
    # initially, each node is assigned 1 except the target, which is assigned 0
    vals = {node: 1.0 for node in G.nodes()}
    vals[target] = 0.0

    for _ in range(iters):
        vals_next = {node: 1.0 for node in G.nodes()}
        vals_next[target] = 0.0

        # update value for each node
        for node in G.nodes:
            neighbors = list(G.neighbors(node))

            # if node has no neighbors, it's value stays the same
            if len(neighbors) == 0:
                continue

            neighbor_vals = {vals[neighbor] for neighbor in neighbors}

            # find neighbors with minimal and maximal values
            val_max = max(neighbor_vals)
            val_min = min(neighbor_vals)

            # calculate updated value for node
            vals_next[node] = calc_val(val_max, val_min)

        vals = vals_next

    return vals


if __name__ == '__main__':
    G = nx.DiGraph()

    # build game graph
    G.add_edges_from([
        ('1', 't'), ('1', 's'),
        ('2', 't'), ('2', '1'),
        ('3', 's'), ('3', '1'),
        ('4', '2'), ('4', '3'),
        ('5', 't'), ('5', '2'),
        ('6', 's'), ('6', '3')
    ])

    # mechanisms to compare
    mechanisms = [unfair_richman, taxman, co_unfair_richman]

    for mechanism in mechanisms:
        plt.figure(mechanism.__name__.replace('_', ' ').title())

        # run value iteration algorithm to find approximated thresholds
        vals = value_iteration(G, target='t', calc_val=mechanism)

        # present (float) values as fractions
        vals_frac = {key: Fraction(value).limit_denominator() for key, value in vals.items()}

        layout = nx.spectral_layout(G)
        nx.draw(G, pos=layout, node_size=1000, node_color='skyblue')
        nx.draw_networkx_labels(G, pos=layout, labels=vals_frac, font_size=10, font_color='black', font_weight='bold')

    plt.show()
