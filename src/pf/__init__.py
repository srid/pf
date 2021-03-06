import os
from os import path
import sys
from fnmatch import fnmatch
import logging
import re

import argparse

LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

IGNORE_LIST = ['.hg', '.git', '.svn',
               '*.pyc', '*~', '*.egg-info',
               '.installed.cfg', 'develop-eggs']


def should_ignore(basename):
    """Should this file/directory be ignored?"""
    assert path.basename(basename) == basename
    
    for ign in IGNORE_LIST:
        if fnmatch(basename, ign):
            return True
    return False
    

def load_pathlist():
    """Traverse the current directory and return the list of filepaths
    
    For each file and directory under current directory, the relative path
    to it is returned
    """
    pathlist = []
    def f(arg, dirname, names):
        names_kept = []
        for idx, name in enumerate(names[:]):
            if not should_ignore(name):
                p = path.join(dirname, name)
                pathlist.append(p)
                names_kept.append(name)
        names[:] = names_kept
    
    path.walk('.', f, None)
    return pathlist
            

def main():
    parser = argparse.ArgumentParser(
        description="Programmer's find; smart file-finding; no more repeated double-tabs."
    )
    
    parser.add_argument(
        'parts', metavar='str', type=str, nargs='+',
        help='Parts of the desired filepath')
    
    args = parser.parse_args()
    
    # File best matching files
    matched_files = []
    for pth in load_pathlist():
        m = re.match('.*' + '.*'.join(args.parts) + '.*', pth)
        if m:
            matched_files.append(pth)
            
    if not len(matched_files):
        LOG.info('no files matched')
    elif len(matched_files) == 1:
        print matched_files[0]
    elif len(matched_files) < 8:
        LOG.info('more than one match; please select one\n%s\nChoose one: ',
                 '\n'.join(['%s. %s' % (idx+1, m) \
                            for idx, m in enumerate(matched_files)]))
        idx = int(raw_input())
        print matched_files[idx-1]
    else:
        LOG.info('a lot of matches; please prune your search')
