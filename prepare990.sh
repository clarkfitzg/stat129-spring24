#for filename in /stat129/990/20*_TEOS_XML_*.zip; do
#	unzip "$filename" -d /stat129/all990files/
#done

# Drop all the namespaces from the xml files
# parallel sed -E 's/<Return xmlns=.*>/<Return>/g' --in-place ::: /stat129/all990files/*
# Fails:
# prepare990.sh: line 6: /usr/bin/parallel: Argument list too long
for filename in /stat129/all990files/*; do
	sed -E 's/<Return xmlns=.*>/<Return>/g' --in-place "$filename"
done
