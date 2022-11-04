from distutils.dir_util import copy_tree

# copy subdirectory example
fromDirectory = "test"
toDirectory = "main"

copy_tree(fromDirectory, toDirectory)
