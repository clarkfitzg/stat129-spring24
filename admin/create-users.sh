# First, create users.txt containing all the users.

ALL=users-newuser.txt
while read USER; do
	echo $USER:$USER::::/home/$USER:/bin/bash
done < users.txt > $ALL
sudo chmod 0600 $ALL
sudo newusers $ALL
