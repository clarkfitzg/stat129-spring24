
# Pretty print
#xmllint --format /stat129/tax/b.xml

xmllint -xpath "//ActivityOrMissionDesc" /stat129/tax/b.xml

xmllint -xpath "//ActivityOrMissionDesc/text()" /stat129/tax/b.xml
