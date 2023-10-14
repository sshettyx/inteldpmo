#!/bin/python3
import os

def coldboot():
    try:
        print ("\nChecking the most recent COLDBOOT iteration.\n\n")
        os.system("ls -td /usr/local/stability_logs/coldboot_Logs_*/ | head -n 1 > /home/intel/count.txt")
        with open("/home/intel/count.txt", "r") as file:
	        readline=file.read().splitlines()
        readline = (readline[0])
        os.system(f"cat {readline}/results.log | tail | grep Iteration_completed")
        print ("\n\n")
    except:
        print(f"Unable to Read the count")


def warmboot():
    try:
        print ("\nChecking the most recent WARMBOOT iteration.\n\n")
        os.system("ls -td /usr/local/stability_logs/warmboot_Logs_*/ | head -n 1 > /home/intel/count.txt")
        with open("/home/intel/count.txt", "r") as file:
            readline=file.read().splitlines()
        readline = (readline[0])
        os.system(f"cat {readline}/results.log | tail | grep Iteration_completed")
        print ("\n\n")
    except:
        print(f"Unable to Read the count")

def S3():
    try:
        print ("\nChecking the most recent S3 iteration.\n\n")
        os.system("ls -td /usr/local/stability_logs/S3_Logs_*/ | head -n 1 > /home/intel/count.txt")
        with open("/home/intel/count.txt", "r") as file:
            readline=file.read().splitlines()
        readline = (readline[0])
        os.system(f"cat {readline}/results.log | tail | grep Iteration")
        print ("\n\n")
    except:
        print(f"Unable to Read the count")

def S4():
    try:
        print ("\nChecking the most recent S4 iteration.\n\n")
        os.system("ls -td /usr/local/stability_logs/S4_Logs_*/ | head -n 1 > /home/intel/count.txt")
        with open("/home/intel/count.txt", "r") as file:
            readline=file.read().splitlines()
        readline = (readline[0])
        os.system(f"cat {readline}/results.log | tail | grep Iteration")
        print ("\n\n")
    except:
        print(f"Unable to Read the count")

def main():
    
    choice=str(input("\nPress 1 for Cold boot \nPress 2 for Warm boot\nPress 3 for S3 \nPress 4 for S4 \n\nEnter the test you want to check the cycles number for:"))
    if choice=='1':
        coldboot()
    elif choice=='2':
        warmboot()
    elif choice=='3':
        S3()
    elif choice=='4':
        S4()
    else:
        print("Wrong Choice.Please Enter the valid Choice")


main()

