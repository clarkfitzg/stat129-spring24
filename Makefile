# Testing
temp_histogram.pdf: uniq_to_hist.R temp_counts.txt
	Rscript $<

temp_counts.txt: 
	seq -50 200 | sed "p;p;p;" |uniq --count > $@
