#!/bin/bash
s3_b=$(echo Linux@123 | sudo -S cat /sys/kernel/debug/suspend_stats | grep success | awk {'print$2'})
echo Linux@123 | sudo -S rtcwake -m mem -s 15
s3_a=$(echo Linux@123 | sudo -S cat /sys/kernel/debug/suspend_stats | grep success | awk {'print$2'})

if [ $s3_a -gt $s3_b ]  
then	
	echo "Pass -- System Has succesfully entered S3" 
else 
	echo "Fail -- System did NOT enter S3, Exiting the program"
	exit
fi 	



