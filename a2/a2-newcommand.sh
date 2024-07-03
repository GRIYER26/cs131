#!/bin/bash
#CS131-Assignment-2: Bash Program to execute a new linux command to automate tasks.
echo "***********************************************************"
read -p "Enter the date (as mm-dd-yyyy) : " date
read -p "Enter the hours of Deep Sleep (as a float) : " deepsleep
read -p "Enter the hours of Core Sleep (as a float) : " coresleep
read -p "Enter the hours of REM  Sleep (as a float) : " remsleep


echo "$date,$deepsleep,$coresleep,$remsleep,$(bc<<<$deepsleep+$coresleep+$remsleep)" >>sleepdata.csv

##while IFS="," read -r col1 col2 col3 col4 col5
##do
##	echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
##	echo "Sleep data for   : $col1"
##	echo "Deep  Sleep hours: $col2"
##	echo "Core  Sleep hours: $col3"
##	echo "REM   Sleep hours: $col4"
##	echo "Total Sleep hours: $col5"
##done < sleepdata.csv 

count=$(cat sleepdata.csv | wc -l)

SUM_deepsleep=$(cat sleepdata.csv | cut -d ',' -f2 | paste -sd+ | bc)

SUM_coresleep=$(cat sleepdata.csv | cut -d ',' -f3 | paste -sd+ | bc)

SUM_remsleep=$(cat sleepdata.csv | cut -d ',' -f4 | paste -sd+ | bc)

SUM_totalsleep=$(cat sleepdata.csv | cut -d ',' -f5 | paste -sd+ | bc)
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

echo "Average Deep  Sleep hours this month :$(echo "scale = 2; $SUM_deepsleep/$count" | bc -l)"

echo "Average Core  Sleep hours this month :$(echo "scale = 2; $SUM_coresleep/$count" | bc -l)"

echo "Average REM   Sleep hours this month :$(echo "scale = 2; $SUM_remsleep/$count" | bc -l)"

echo "Average Total Sleep hours this month :$(echo "scale = 2; $SUM_totalsleep/$count" | bc -l)"

echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"


