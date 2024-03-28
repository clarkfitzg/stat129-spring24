# Goal: Demonstrate xpath from the command line

# Download a local copy of the page
# Not necessary, but makes things more convenient
wget https://www.irs.gov/charities-non-profits/form-990-series-downloads

xmllint --html -xpath "" /stat129/form-990-series-downloads
