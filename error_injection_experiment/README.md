# Error injection test scripts #

This directory includes our voting algorithm error
injection experiments.

The requirements can be installed via:
```
pip install -r requirements.txt
```

The file `test.py` includes 12 experiments using 3 different
amalgamation voting algorithms.

All experiments are conducted using 10000 voting rounds with different error injection parameters between 11 simulated voters.

The algorithms are as follows:

- Outlier: Simple average with outlier removal
- Weighted: Weighted average
- Byzantine: Value grouping and Byzantine voting among the resulting groups

The experiments conducted are in order of execution:
- Outlier 4: Outlier algorithm, 4% probability of error injection in each value, with the maximum possible error amplitude varying between 0.1 and 1 of the correct value.
- Outlier 40: Same as above with 40% probability
- Outlier 100: Same as above but errors are added to every value.
- Weighted 4, 40, 100: Same as the 3 above but with the weighted algorithm.
- Byzantine 4, 40, 100: Same as above but with the Byzantine algorithm.
- Outlier, Weighted, Byzantine: 1 more experiment with each algorithm, where the error probability is varied between 0% and 100% and the error amplitude is kept at 0.3, a value chosen for illustrative purposes.

The experiment should take under 2 minutes to run.

The file `plot.py` will plot the resulting `.csv` data in the format used in the paper.
