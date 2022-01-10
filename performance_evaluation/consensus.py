import collect
import verify
import subprocess
from pathlib import Path
from distutils.dir_util import copy_tree
import os



# Gather the files + meta from the branches
# -> Replacement code for temp retrieve from syncer.py
def branch_retrieve(dataset, branches):
    print(dataset, branches)

    for branch in branches:
        subprocess.run(f"git clone --single-branch --branch {branch} {dataset} work/{branch}", shell=True)
    collect.consensus('work')
    subprocess.run(f"git clone {dataset} main", shell=True)
    copy_tree('result', 'main')
    old_wd = os.getcwd()
    os.chdir(f'{old_wd}/main')
    subprocess.run(f"git add .", shell=True)
    subprocess.run(f'git commit -m "test"', shell=True)
    subprocess.run(f"git push", shell=True)
    os.chdir(old_wd)

# Commit the new master

# Interactive input for testing
if __name__ == '__main__':
    dataset = input("Set name of dataset: ")
    branches = [item for item in input("Enter the branch names: ").split()]
    #dataset = "git@github.com:EcePanos/ref_2.git"
    #branches = ['node1', 'node2', 'node3']
    branch_retrieve(dataset, branches)
