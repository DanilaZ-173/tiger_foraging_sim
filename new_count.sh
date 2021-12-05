#!/bin/bash

read -p "Enter the number of times to run the script: " runs
n=0
until [ "$n" -eq "$runs" ] ; do
	python ./probabiltiy.py
	cat f_prob.txt | grep 1 | wc -l | tee count_result.txt
	rm f_prob.txt
	n=$((n+1))
done

result=$(cat count_result.txt)
sr=$(echo "$result/($n*1000)" | bc -l)
echo "The success rate is: $sr"

