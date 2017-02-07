# Print out a list of subdirectories from a directory/path

# Trying out a solution from stackoverflow using the os module
import os

def print_files():
    # output list
    r = []
    for root, dirs, files in os.walk("."):
        for name in files:
            r.append(os.path.join(root, name))
    print r

print print_files()

# Generate the file names in a directory tree by walking the tree either 
# top-down or bottom-up. For each directory in the tree rooted at directory top 
# (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).

# http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/

def printFolderName(init_indent, rootFolder):
    fname = rootFolder.split(os.sep)[-1]
    root_levels = rootFolder.count(os.sep)
    # os.walk treats dirs breadth-first, but files depth-first (go figure)
    for root, dirs, files in os.walk(rootFolder):
        # print the directories below the root
        levels = root.count(os.sep) - root_levels
        indent = ' '*(levels*2)
        print init_indent + indent + root.split(os.sep)[-1]

def print_files_recursively():
    for dirpath, dirs, files in os.walk("."):    
        path = dirpath.split('/')
        print '|', (len(path))*'---', '[',os.path.basename(dirpath),']'
        for f in files:
            print '|', len(path)*'---', f

print print_files_recursively()