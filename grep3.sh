zcat $1 |
	grep -E 'ITE00100554' |
	grep 'TMAX' |
	cut -d , -f 1,2,4
zcat $1 |
	grep -E 'EZE00100082' |
	grep 'TMAX' |
	cut -d , -f 1,2,4
zcat $1 |
	grep -E 'GM000010962' |
	grep 'TMAX' |
	cut -d , -f 1,2,4
