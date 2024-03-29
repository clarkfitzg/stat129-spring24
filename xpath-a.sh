
# Pretty print
#xmllint --format /stat129/tax/a.xml

# So ugly having to deal with this local-name()= to ignore the namespace.
xmllint -xpath "//*[local-name()='ActivityOrMissionDesc']/text()" /stat129/tax/a.xml
