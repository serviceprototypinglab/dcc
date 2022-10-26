# Data-Centric Consensus code artifacts

This repository contains the code and data in order to reproduce the results, including figures, of the article: Decentralised Data Quality Control in Ground Truth Production for Autonomic Decisions, by P. Gkikopoulos, J. Spillner and V. Schiavoni, accepted for publication at IEEE TPDS - Transactions on Parallel and Distributed Systems, 2022. In particular, it contains a reference implementation for the Data-Centric Consensus (DCC) protocol that aims to raise confidence in data-driven decision making as well as data-centric AI.

The code is maintained through Git by Zurich University of Applied Sciences and University of Neuchâtel, with future improvements to the voting/DCC algorithm expected, while the snapshot relevant for the article is also long-term archived on Zenodo.

The archived version on Zenodo is available at: https://doi.org/10.5281/zenodo.5835875

All results are contained in the following two directories:

- Performance evaluation: Includes the prototype DCC tool and associated documentation used in our performance evaluation and reference to the test dataset that can be used to measure performance. This dataset, was used to obtain the performance data presented in the papaer.

- Error injection experiment: Includes a standalone script that compares 3 voting algorithms in different error injection configurations. A plotting script used to plot the results and documentation is included.
