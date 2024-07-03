******************************************************************************************************
CS131-Assignment 2
Rajshri Ganesh Iyer

SLEEP HEALTH TRACKER

Command: ./a2-newcommand.sh

WHAT THIS COMMAND (SCRIPT) DOES?
This program is designed to automatically collect sleep data from the user every day of the month 
and then generate the Average Deep Sleep, Average Core Sleep and Average REM Sleep data for the month. 
It appends the sleep data into a csv file called sleepdata.csv, which is saved in the a2 directory. 

WHY IS THIS COMMAND (SCRIPT) USEFUL?
We can use crontab -e to schedule this bash script to run every monring at a specified time, and 
serves as a reminder for the user to input the sleep data from their sleep monitors and track 
their sleep health data for improved sleep quality over time.  
 
HOW THIS COMMAND (SCRIPT) CAN BE USED IN REAL LIFE?
Currently the bash script only uses sleep duration as inputs, but in future, this script will be designed 
to collect several other inputs from the user such as sleep timings, stress levels, sleep quality rating, dream event,
hours before last food intake, duration of workout etc. to really provide a comprehensive outlook of factors 
affecting sleep. The script will also calculate the correlation between sleep quality and other parameters collected.
 
TERMINAL EXAMPLE

[iyersu24@sjsu a2]$ ./a2-newcommand.sh 
***********************************************************
Enter the date (as mm-dd-yyyy) : 07-11-2024
Enter the hours of Deep Sleep (as a float) : 2.3
Enter the hours of Core Sleep (as a float) : 1.7
Enter the hours of REM  Sleep (as a float) : 3.2
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Average Deep  Sleep hours this month :1.64
Average Core  Sleep hours this month :2.77
Average REM   Sleep hours this month :3.31
Average Total Sleep hours this month :7.73
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[iyersu24@sjsu a2]$ cat sleepdata.csv 
07-01-2024,1,2,3,6
07-02-2024,2,3,4,9
07-03-2024,1.1,2.2,3.3,6.6
07-04-2024,1.22,3.22,2.3,6.74
07-05-2024,1.3,3.4,2.33,7.03
07-06-2024,2.3,1.11,5.2,8.61
07-07-2024,2,3,4,9
07-08-2024,2.3,4.3,2.3,8.9
07-09-2024,1.3,2.3,4.5,8.1
07-10-2024,1.3,4.33,2.3,7.93
07-11-2024,2.3,1.7,3.2,7.2

***********************************************************
