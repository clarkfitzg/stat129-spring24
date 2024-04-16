# /opt/anaconda/bin/ipython

import csv
import os
import multiprocessing
import random
import re

from lxml import etree

datadir = "/stat129/all990files/"
files = os.listdir(datadir)

d23 = [datadir + p for p in files if p.startswith("2023")]

# Working with a small sample is easier
n = 10000
random.seed(240) # Same random sample
s990 = random.sample(d23, n)

regex = re.compile(r'''
    #####################
    \b mental \s+ (health|illness|service)
    |crisis interven
    |\b suicid
    |(psychological) \s+ (counseling)
    #####################
    |(college|university) \s+ (student|academic|prep|faculty|educ)
    #####################
    |\b immigran?t
    |migrant
    |refugee
    |\b deport
    ''', flags=re.IGNORECASE | re.VERBOSE)

# mental matches 51/10K
# education matches 27/10K
# immigrant matches 23/10K
#
# combined matched 101/10K
# 51 + 27 + 23 = 101
# => NO overlap
# Wow, that's surprising

# Check this works as intended
rtests = (
        ("the suicidal tendencies", True),
        ("mental", False),
        ("the college preparation course", True),
        ("university library", False),
        ("board of immigration policy", True),
        ("undeportable", False),
        )

for s, v in rtests:
    found = regex.search(s) is not None
    if found == v:
        print('ok')
    else:
        print('failed test: ', s)


def extract(xmlfile):
    tree = etree.parse(xmlfile)
    mission = tree.xpath("//MissionDesc/text()")
    if not mission:
        return None
    mission = mission[0]

    if not regex.search(mission):
        return None

    result = {}
    result["mission"] = mission
    xp = "/Return/ReturnHeader/Filer/"
    try:
        result["EIN"] = tree.xpath(xp + "EIN/text()")[0]
        result["name"] = tree.xpath(xp + "BusinessName/BusinessNameLine1Txt/text()")[0]
    except:
        return None

    return result


with multiprocessing.Pool(20) as p:
    #results = p.map(extract, s990)  # for testing
    results = p.map(extract, d23)

#    CPU times: user 709 ms, sys: 472 ms, total: 1.18 s
#    Wall time: 10.7 s
# Wow- faster than I expected.


with open('descriptions.csv', 'w', newline='') as csvfile:
    fn = 'EIN name mission'.split()
    writer = csv.DictWriter(csvfile, fieldnames=fn)
    writer.writeheader()
    for row in results:
        if row:
            writer.writerow(row)
