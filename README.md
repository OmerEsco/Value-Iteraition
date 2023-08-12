# Value-Iteraition

## Omer Escojido and Ido Greenspan

### Introduction

For our B.Sc final year project in Computer Science, we researched the subject of reachability bidding games.

We noticed that the existing games are always between two players, which preserves the zero-sum property. In order to expand these games to three players (or more) and maintain the zero-sum property, we came up with the idea of coalitions - two targets, each target shared by a group of players.

We defined a three-player zero-sum bidding mechanism, and managed to find two-player bidding mechanisms that can be used as upper and lower bounds for it's threshold ratios. In our example, Unfair Richman is the upper bound and Taxman with $\tau$=0.5 is the lower bound.

The code shown here is an implementation of the Value Iteration algorithm. Given a game and a bidding mechanism, this algorithm finds an approximation for the threshold ratio at each vertex. Our goal was to see if in practice the bounds we found are tight enough to say something about the thresholds in three-player zero-sum games.

### Implementation details

We implemented the algorithm in **Python**, and used the external libraries **Matplotlib** and **Networkx**.
