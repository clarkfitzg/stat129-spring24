# /opt/anaconda/bin/ipython

import os
import random
import re

from lxml import etree

datadir = "/stat129/all990files/"

all990 = [datadir + p for p in os.listdir(datadir)]
# Has 2.3 million files

# Working with a small sample is easier
n = 10
random.seed(2089) # Same random sample
s990 = random.sample(all990, n)

# Develop a function by starting with just one.
xmlfile = s990[0]

tree = etree.parse(xmlfile)

tree.xpath("/Return/ReturnData/IRS990/MissionDesc/text()")[0]
tree.xpath("/Return/ReturnData/IRS990/TotalEmployeeCnt/text()")[0]

# We notice the redundancy, so let's take it out.

# Add whatever other elements you want here.
# We certainly need to identify the nonprofit!
fields990 = ["ActivityOrMissionDesc", "MissionDesc", "TotalEmployeeCnt", "TotalAssetsEOYAmt", "TotalContributionsAmt", "CYTotalRevenueAmt"]

# Hold all the results
result = {}
for f in fields990:
    result[f] = tree.xpath("/Return/ReturnData/IRS990/" + f + "/text()")[0]


# Wrap it up into a function
def extract(xmlfile):
    """
    Extract a dictionary containing the elements of interest
    """
    tree = etree.parse(xmlfile)
    fields990 = ["ActivityOrMissionDesc", "MissionDesc", "TotalEmployeeCnt", "TotalAssetsEOYAmt", "TotalContributionsAmt", "CYTotalRevenueAmt"]

    # Hold all the results
    result = {}
    for f in fields990:
        # Won't always be there
        try:
            result[f] = tree.xpath("/Return/ReturnData/IRS990/" + f + "/text()")[0]
        except:
            # didn't work!
            # There are certainly better ways to handle this.
            result[f] = None
    return result

# Test our function
r3 = extract(s990[3])


# Apply our function to many files
rn = map(extract, s990)

# Convert it to a list, because map is lazy
rn = list(rn)

# Now run it on... EVERYTHING ALL AT ONCE IN PARALLEL!
# See https://docs.python.org/3/library/multiprocessing.html
from multiprocessing import Pool

# 10 parallel workers
with Pool(10) as p:
    r = p.map(extract, all990)

# Nice, it was faster than I expected:
#
#    In [57]: %time %run tax.py
#    CPU times: user 14.8 s, sys: 1.31 s, total: 16.1 s
#    Wall time: 1min 42s
