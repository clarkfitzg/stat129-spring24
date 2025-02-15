
cd ~
cp /stat129/stat129-spring24/simple-page.html .

# all "li" nodes
xmllint --html -xpath "//li" simple-page.html

# "a" nodes under "li" nodes
xmllint --html -xpath "//li/a" simple-page.html

# href attributes on "a" nodes under "li" nodes
xmllint --html -xpath "//li/a/@href" simple-page.html

# only those "a" nodes that have an href attribute that contains ".zip"
xmllint --html -xpath "//li/a[contains(@href, '.zip')]/@href" simple-page.html

# I can't figure out how to chop out href= ...  :(
# so I'll just resort to the command line 	:)
#xmllint --html -xpath "string(//li/a/@href)" simple-page.html
xmllint --html -xpath "//li/a[contains(@href, '.zip')]/@href" simple-page.html |
	sed "s/ href=//" | tr --delete '"'

#
#xmllint --html -xpath "//li" simple-page.html
