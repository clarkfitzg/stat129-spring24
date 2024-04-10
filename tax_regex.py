# /opt/anaconda/bin/ipython

# If you're using this script, please clean it up and delete whatever is not essential.

import os
import random
import re

from lxml import etree

datadir = "/stat129/all990files/"

all990 = [datadir + p for p in os.listdir(datadir)]
# Has 2.3 million files

# Working with a small sample is easier
n = 8000
random.seed(2089) # Same random sample
#random.seed(1380) # Same random sample
s990 = random.sample(all990, n)

# Develop a function by starting with just one.
xmlfile = s990[0]

# Pull out all the mission descriptions
def mission(xmlfile):
    tree = etree.parse(xmlfile)
    mission = tree.xpath("//MissionDesc/text()")
    if mission:
        return mission[0]
    else:
        return ""

#sm = [mission(f) for f in s990]

# clean water
# Regex:
pattern = r"clean water"
# More ambitious
#pattern = r"clean water|river|ocean|lake"

# Gives me all descriptions that match the pattern
#water = [x for x in sm if re.search(pattern, x, flags=re.IGNORECASE)]

# Let's combine the filtering with extracting what we want
def extract(xmlfile):
    tree = etree.parse(xmlfile)
    mission = tree.xpath("//MissionDesc/text()")
    if not mission:
        return None
    mission = mission[0]

    pattern = r"clean water"
    if not re.search(pattern, mission, flags=re.IGNORECASE):
        return None

    result = {}
    result["mission"] = mission
    result["employee"] = tree.xpath("/Return/ReturnData/IRS990/TotalEmployeeCnt/text()")
    return result

w2 = [extract(x) for x in s990]
# Clean up all these Nones
w3 = [x for x in w2 if x is not None]

