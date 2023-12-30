# Data-Centric Consensus code artifacts

This repository contains the code and data in order to reproduce the results, including figures, of the article: [Decentralised Data Quality Control in Ground Truth Production for Autonomic Decisions](https://ieeexplore.ieee.org/document/9681269), by P. Gkikopoulos (Zurich University of Applied Sciences and University of Neuchâtel), J. Spillner (Zurich University of Applied Sciences) and V. Schiavoni (University of Neuchâtel), published in IEEE TPDS - Transactions on Parallel and Distributed Systems, vol. 3, issue 10, October 2022. In particular, it contains a reference implementation for the Data-Centric Consensus (DCC) protocol that aims to raise confidence in data-driven decision making as well as data-centric AI.

The code is collaboratively maintained through Git by Zurich University of Applied Sciences and University of Neuchâtel, with future improvements to the voting/DCC algorithm expected, while the snapshot relevant for the article is also long-term archived on Zenodo.

The archived version on Zenodo is available at: https://doi.org/10.5281/zenodo.5835875
The collaboratively maintained code repository is at: https://github.com/serviceprototypinglab/dcc

## Abstract

Autonomic decision-making based on rules and metrics is inevitably on the rise in distributed software systems. Often, the metrics are acquired from system observations such as static checks and runtime traces. To avoid bias propagation and hence reduce wrong decisions in increasingly autonomous systems due to poor observation data quality, multiple independent observers can exchange their findings and produce a majority-accepted, complete and outlier-cleaned ground truth in the form of consensus-supported metrics.

This repository contains the code, data and scripts to produce ground truth with data-centric consensus voting for more reliable decision making processes. It can be used to computationally reproduce the two key results, the multi-plot figures 6 and 7 of the TPDS article. While the article puts these results into a broader context, this repository contains all technical information to verify the correctness and performance of the proposed and implemented algorithms.

## Artifacts Overview

All artifact code is contained in the following two independent directories, each of which contains a detailed sub-README file for further information:

- Performance evaluation (directory [performance_evaluation](performance_evaluation)): Includes the prototype DCC tool and associated packaging and documentation used in our performance evaluation. It also contains a reference to the test dataset that can be used to measure performance, and to a synthetic dataset generator. This generator approximates the infrastructure used to obtain the performance data presented in the paper (Fig. 6). The performance evaluation is conducted in containerised form.

- Error injection experiment (directory [error_injection_experiment](error_injection_experiment)): Includes a standalone script that compares 3 voting algorithms in different error injection configurations. A plotting script used to plot the results and documentation is included (Fig. 7). The error injection runs through a Python virtual environment without containers.

Hence, Fig. 7 can be precisely reproduced, whereas Fig. 6 can be approximately reproduced. The differences for Fig. 6 are the absence of networked invocations (which require a custom infrastructure setup), the omission of averaging across 10-fold computation (to save compute time), and the 'natural' performance differences due to different CPU architectures.

## Requirements and Dependencies

In total, around 1 GB of disk space is needed to set up the container image and the Python virtual environment. The additional capacity required by data and experiments is negligible. The experiments can execute on a researcher notebook or workstation; any single-core machine with approximately 3 GHz core and at least 4 GB of memory should be fine. All experiments run local, whereas a network connection is required for the initial setup.

The assumption is that Linux environment from around 2020-23 is used. The code has been tested in particular on Ubuntu 20.10 (groovy; although the containerised performance experiment uses an older base image) and on Debian 12 (bookworm). All Python packages are installed through Pip so that only few system packages are required (python3-pip python3-virtualenv docker.io).

Other than the software setup, no further dependencies exist. All required data files are included or synthetically generated. However, for the full experiment as described in the paper, a networked environment with distributed Git repositories across SSH accounts would have to be set up manually.

## Setup and Cleanup

The setup of the experiments is explained for both parts separately in the sub-README files. If the reproduction script mentioned below is used, no separate setup needs to be conducted. Ensure that the requirements especially concerning disk space are fulfilled and just run `./reproduce-article-figures.sh`!

The generated CSV files, PDF plots, Docker image and Python virtual environment directory can be safely removed after conducting the experiment. Detailed instructions are given in the sub-README files. The reproduction script automates the cleanup as well.

## Results Reproduction

To reproduce the TPDS article figures, a convenience script is provided: `reproduce-article-figures.sh`. It combined both artifacts, performance evaluation and error injection, and ensures the setup and cleanup are fully automated. Just running this script (and waiting around 10 minutes) is sufficient to obtain two PDF files which correspond to figures 6 and 7 of the published article. The script is mostly self-explaining but also contains some inline documentation on what it does. Eventually, two files are produced: `fig6-plot.pdf` and `fig7-plot.pdf`.
