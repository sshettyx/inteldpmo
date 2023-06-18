#!/bin/bash
s0ix_b=$(echo Linux@123 | sudo -S cat /sys/kernel/debug/pmc_core/slp_s0_residency_usec)
echo Linux@123 | sudo -S rtcwake -m freeze -s 5
s0ix_a=$(echo Linux@123 | sudo -S cat /sys/kernel/debug/pmc_core/slp_s0_residency_usec)

if [ $s0ix_a -gt $s0ix_b ]  
then	
	echo "Pass -- System Has succesfully entered S0ix" 
else 
	echo "Fail -- System did NOT enter S0ix, Exiting the program"
	exit
fi 	



