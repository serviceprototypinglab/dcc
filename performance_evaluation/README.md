# Data-Centric Consensus over Git Datasets #

This containerised consensus implementation will merge multiple branches of an input dataset that is implemented as a distributed Git repository into a ground truth branch. The input branches could represent independent observations, not directly suitable for follow-up decision making, whereas the ground truth would allow for simplified follow-up activities as part of a larger data-centric acquisition and decision pipeline.

Of primary interest is the performance of the implementation. The subdirectory `generator` is dedicated to that but requires the container image to be available at first.

## Instructions ##

#### Pre-requisites ####

- A Linux-based machine (or VM) with Docker installed; Docker version 20.10 is known to work
- A Git repository with one or more `.csv` data files and a metadata file (see relevant section of this README) and three or more branches to merge (recommended odd number to avoid voting ties) and a `main` branch for the results to be merged to.
- Write access to the above repository, commonly through SSH keys

#### Usage ####

Build the container, based on an Ubuntu 18.10 base image:

```
docker build -t dockerssh .
```

Build time should be around 1-3 minutes on a contemporary researcher notebook or workstation, depending on the network bandwidth required for package downloads during the build process. No special hardware or infrastructure is necessary. The resulting image requires around 700 MB disk space.

Run the container through automated performance experiments. If this is desired, stop reading here and proceed into the `generator` subdirectory which has two scripts, `python gen.py` to run the experiment in an automated way and `python plot_entry.py` to visualise the results.

Run the container manually. The parameterisation can be a mix of environment variables and interactive inputs. You will need to provide upfront either the directory where your remote Git SSH key resides or a local Git repository path. Moreover, you should specify the desired Git identity for producing the ground truth branch, although a reasonable default value (dcc@none) is used by default.

(Security note: If you do not trust this software, you can put the keys outside of your system's default SSH key directory and/or use an internal Git account.)

```
docker run --rm -it \
  [-v <ssh key location>:/home/user/.ssh] \
  [-v <localrepository>:<containerrepopath>] \
  [-e gitemail="<git email>" -e gitusername="git username"] \
  [-e dsname="..." -e dsbranches="b1 b2 b3"] \
  dockerssh
```

Unless $dsname and $dsbranches are given, the program will then ask for the URL to the Git repository to be merged through voting, and then the names of the branches that will participate in the vote.

* Set name of dataset? URL to the Git repository. Equivalent of $dsname. Can be a local repository mapped as volume into the container starting with /, a user@host:... SSH URL, a HTTP(S) URL or anonymous (read-only) git:// URL.
* Branch names? Names of the branches to consider in the voting, separated by spaces. Equivalent of $dsbranches.

The result will be pushed to the `main` branch of the repository once the process finishes. This part will only work for SSH/HTTP(S) and file-based repositories, not for anonymous Git.

#### Metadata ####

The tool expects a `meta.json` file existing in each of the branches that describes the files to be merged:

```
[
  {
    "prefix": <pattern>,
    "index": <name-of-index-column>,
    "metrics": [<list-of-numeric-columns>],
    "props": [<list-of-non-numeric-columns>]
  }
]
```
If multiple files should be merged, add them to the top level list. The fields are as follows:

- prefix: Partial filename. All matches will be merged. Useful for datasets where a date is appended to the filename.
- index: The name of the column to be used as the index. This column will be used as the unique identifier for each row and as such will not be voted on.
- metrics/props: Lists of numeric/non-numeric columns. The tool detects these automatically for voting but needs them explicitly for effective de-duplication post-merge.

#### Sample repository ####

You can fork [this public repository](https://github.com/EcePanos/bench2000) as an example to test this without setting up a dataset. It contains our dummy performance test data. Our experiments used various permutations of this dataset to test the performance of the tool in realistic network conditions.

Depending on network conditions and whether the git repositories are local or remote, the process for datasets of similar size to the sample should take around 1 minute to complete.

For the paper we used local or remote forks of the repository, as well as a varying number of branches. Each branch contained identical data.

* Set name of dataset? https://github.com/EcePanos/bench2000.git
* Branch names? node1 node2 node3

In case this repository becomes unavailable in the future, as it is a crucial input dataset with modest size, a safety replica is included here as `bench2000.git.zip`. It was produced through the following commands:

```
git clone --mirror https://github.com/EcePanos/bench2000
zip -r bench2000.git.zip bench2000.git/
```

A local repository can be produced from this safety replica and used for exemplary voting as follows:

```
unzip bench2000.git.zip
docker run -it -v $PWD/bench2000.git:/tmp/bench -e gitemail=x -e gitusername=y dockerssh
```
