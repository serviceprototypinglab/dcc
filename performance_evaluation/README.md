# Data-Centric Consensus git prototype #

This docker image will merge multiple branches of a dataset that is implemented as a git repository into a ground truth branch.

## Instructions ##

#### Pre-requisites ####

- A Linux-based machine (or VM) with Docker installed
- A git repository with one or more `.csv` data files and a metadata file (see relevant section of this README) and three or more branches to merge (recommended odd number to avoid voting ties) and a `main` branch for the results to be merged to.
- SSH access to the above repository

#### Usage ####

Build the container:

```
docker build -t dockerssh .
```

Run the container. You will need to provide the directory where your git SSH key resides and your git credentials.

(Security note: If you do not trust this software, you can put the keys outside of your system's default SSH key directory and/or use an internal git account.)

```
docker run -it -v <ssh key location>:/home/user/.ssh -e gitemail="<git email>" -e gitusername="git username" dockerssh
```

The program will then ask for the SSH link to the repository to be merged and then the names of the branches that will vote (separated by spaces).

The result will be pushed to the `main` branch of the repository once the process finishes.

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
