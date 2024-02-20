# Reproduce Fig. 7 (precise reproduction)
# Sets up the Python virtual environment and runs the main script test.py
# followed by results plotting and cleanup.

cd error_injection_experiment
python -m venv experiment
source experiment/bin/activate
pip install -r requirements.txt
python test.py
python plot.py
cp plot.pdf ../fig7-plot.pdf
rm *.csv *.pdf
# rm -rf experiment/
cd ..

# Reproduce Fig. 6 (approximate reproduction)
# Builds the container image around the DCC first, then synthetically
# creates local Git repositories with data files across branches,
# and for each repository invokes the DCC container while measuring
# the execution time. Again, the results are plotted and cleaned up.

cd performance_evaluation
docker build -t dockerssh .
cd generator
python gen.py
python plot_entry.py
cp plot.pdf ../../fig6-plot.pdf
rm *.csv *.pdf
docker rmi dockerssh
cd ..
