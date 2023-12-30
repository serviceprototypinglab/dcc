# Error injection in data-centric consensus voting #

This directory includes two scripts for performing voting algorithm error injection experiments, and plotting the results.

The required Python packages can be installed into a virtual environment via the commands:
```
python -m venv experiment
experiment/bin/pip install -r requirements.txt
```

This will require around 275 MB of disk space. The outputs of the experiment itself, in the form of CSV files, will only require a few kBs of additional space. In terms of time, the whole experiment should take under 2 minutes to run on contemporary hardware (i.e. researcher notebook or workstation).

The file `test.py` includes 12 experiments using 3 different amalgamation voting algorithms. Each experiment reports on the correctness (percentage of correct results) and execution time under the influence of synthetic errors.

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

The file `plot.py` will plot the resulting `.csv` data into a row of four diagrams, comparing the correctness results while omitting the execution time. The output figure is saved as `plot.pdf`.

Hence, following the provided setup instructions, the recommended execution order is:

```
experiment/bin/python test.py
experiment/bin/python plot.py
```

After having run the experiment and potentially having saved the output data, the directory can be cleaned up and reset to its initial state via these final commands:

```
rm *.csv *.pdf
rm -rf experiment/
```
