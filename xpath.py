
# Run with /opt/anaconda/bin/ipython

from lxml import etree

tree = etree.parse("/stat129/tax/a.xml")

#d = tree.xpath("//ActivityOrMissionDesc/text()")
d = tree.xpath("//ActivityOrMissionDesc")
d2 = tree.xpath("//*[local-name()='ActivityOrMissionDesc']/text()")
