zcat $1 |
	grep -E 'ITE00100554|EZE00100082|GM000010962' |
	grep 'TMAX' |
	cut -d , -f 1,2,4

