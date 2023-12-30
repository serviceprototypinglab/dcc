import json
import os
import shutil
import time

def buildrepo(nentries, npop, nprops, sprops):
    reponame = f"repo-{nentries}"
    if os.path.isdir(reponame):
        shutil.rmtree(reponame)
    os.makedirs(reponame)
    os.chdir(reponame)
    os.system("git init -b main")
    os.system("touch empty")
    os.system("git add empty")
    os.system("git commit -m empty-main")

    branches = []
    for i in range(1, npop+1):
        branch = f"node{i}"
        branches.append(branch)

    props = []
    numprops = []
    strprops = []
    for i in range(nprops):
        prop = f"prop{i}"
        props.append(prop)
        numprops.append(prop)

    for i in range(sprops):
        prop = f"sprop{i}"
        props.append(prop)
        strprops.append(prop)

    for branch in branches:
        os.system(f"git branch -c main '{branch}'")
        os.system(f"git checkout '{branch}'")

        meta = [{
            "prefix": "sample",
            "index": "artifact",
            "metrics": [],
            "props": props
        }]

        f = open("meta.json", "w")
        json.dump(meta, f)
        f.close()

        plist = ""
        if props:
            plist = "," + ",".join(props)

        f = open("sample.csv", "w")
        print(f"artifact{plist}", file=f)
        for i in range(nentries):
            pval = ""
            if numprops:
                pval = "," + ",".join(f"{i+300}" for prop in numprops)
            if strprops:
                pval = "," + ",".join(chr(65 + i % 26) for prop in strprops)
            print(f"artifact{i}{pval}", file=f)
        f.close()

        os.system("git add meta.json sample.csv")
        os.system(f"git commit -m auto-{branch}")

    os.system("git branch -c main checkout-dummy")
    os.system("git checkout checkout-dummy")
    os.system("touch dummy")
    os.system("git add dummy")
    os.system("git commit -m dummy-dummy")

    os.system("git config receive.denyCurrentBranch ignore")

    repodir = os.getcwd()
    branches = " ".join(branches)

    t0 = time.time()
    os.system(f"docker run -it -v {repodir}:/tmp/repo -e dsname=/tmp/repo -e dsbranches='{branches}' dockerssh")
    tdiff = round(time.time() - t0, 2)

    os.system("git restore --staged .")
    os.system("git restore .")

    return tdiff

f = open("entry.csv", "w")
print("Entries,Local,Network", file=f)
origdir = os.getcwd()
for nentries in range(200, 2000+1, 200):
    os.chdir(origdir)
    tdiff = buildrepo(nentries, 3, 1, 0)
    print(f"{nentries},{tdiff},0", file=f)
f.close()

os.chdir(origdir)
f = open("pop.csv", "w")
print("Pop,Local,Network", file=f)
origdir = os.getcwd()
for npop in range(3, 21+1, 2):
    os.chdir(origdir)
    tdiff = buildrepo(2000, npop, 1, 0)
    print(f"{npop},{tdiff},0", file=f)
f.close()

os.chdir(origdir)
f = open("nprop.csv", "w")
print("Nprop,Local", file=f)
origdir = os.getcwd()
for nprops in range(1, 10+1):
    os.chdir(origdir)
    tdiff = buildrepo(2000, 3, nprops, 0)
    print(f"{nprops},{tdiff}", file=f)
f.close()

os.chdir(origdir)
f = open("proptype.csv", "w")
print("Proptype,Local", file=f)
origdir = os.getcwd()
for nprops in range(0, 10+1):
    os.chdir(origdir)
    tdiff = buildrepo(2000, 3, nprops, 10 - nprops)
    print(f"{nprops},{tdiff}", file=f)
f.close()
