# Calculate the median of numbers from stdin
# test with:
# echo "20
# 10
# 30" | python3 median.py

import sys
from statistics import median

x = [float(line) for line in sys.stdin]

print(median(x))
