# $1 refers to the first command line argument, $2 to the second, ...
zcat $1 | grep "TMAX" | head
