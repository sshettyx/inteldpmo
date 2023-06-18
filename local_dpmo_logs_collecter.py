#!/bin/python3
import os
import sys

def coldboot():
    try:
        print ("\nChecking the most recent COLDBOOT iteration.\n\n")
        os.system("ls -td /usr/local/stability_logs/coldboot_Logs_*/ | head -n 1 > /home/intel/count.txt")
        with open("/home/intel/count.txt", "r") as file:
	        readline=file.read().splitlines()
        readline = (readline[0])
        global file_name
        os.system(f"mkdir log_dpmo && cp -rf {readline} log_dpmo")
        file_name = str(input("Enter the name for the zip file you want to create(without extention): "))
        os.system(f"zip -r {file_name}.zip log_dpmo")
        print ("\n\n")
    except:
        print(f"Unable to Read the directory")


def warmboot():
    try:
        print ("\nChecking the most recent WARMBOOT iteration.\n\n")
        os.system("ls -td /usr/local/stability_logs/warmboot_Logs_*/ | head -n 1 > /home/intel/count.txt")
        with open("/home/intel/count.txt", "r") as file:
            readline=file.read().splitlines()    
        readline = (readline[0])
        global file_name
        os.system(f"mkdir log_dpmo && cp -rf {readline} log_dpmo")
        file_name = str(input("Enter the name for the zip file you want to create (Without extention): "))
        os.system(f"zip -r {file_name}.zip log_dpmo")
        print ("\n\n")
        print ("Log has been collected")
    except:
        print(f"Unable to Read the directory")


def s0ix():
    try:
        print ("\nChecking the most recent s0ix iteration.\n\n")
        os.system("ls -td /usr/local/stability_logs/S0ix_Logs_*/ | head -n 1 > /home/intel/count.txt")
        with open("/home/intel/count.txt", "r") as file:
            readline=file.read().splitlines()
        readline = (readline[0])
        global file_name
        os.system(f"mkdir log_dpmo && cp -rf {readline} log_dpmo")
        file_name = str(input("Enter the name for the zip file you want to create(Without extention): "))
        os.system(f"zip -r {file_name}.zip log_dpmo")

        print ("\n\n")
    except:
        print(f"Unable to Read the directory")

def main():
    
    choice=str(input("\nPress 1 for Cold boot \nPress 2 for Warm boot \nPress 3 for s0ix\nEnter the test you want to check the cycles number for:"))
    if choice=='1':
        coldboot()
    elif choice=='2':
        warmboot()
    elif choice=='3':
        s0ix()
    else:
        print("Wrong Choice.Please Enter the valid Choice")

def debug():
    try:
        print ("\nCollecting debug logs.\n\n")
        os.system("cd /usr/bin/ && ./debug_log_collector.sh")
        os.system("ls -td /usr/bin/log-* | head -n 1 > /home/intel/dbg.txt")
        with open("/home/intel/dbg.txt", "r") as file:
            dbg=file.read().splitlines()
        dbg = (dbg[0])
        os.system(f"mkdir log_debug && cp -rf {dbg} log_debug")
        os.system(f"zip -u {file_name}.zip log_debug/*")
    except:
        print(f"Unable to Read the file")


def dg():
    sel=str(input("Do you want to collect the debug logs? \nPress y or n: ").lower())
    if sel== 'y':
        debug()
    else: 
        sel=='n'
        print("done")

main()
dg()
os.system("rm -rf log_debug log_dpmo")


