#!/bin/bash

for ((n=0;n<1000;n++))
do
	rm out* &> /dev/null
	rm data* &> /dev/null
	rm blah* &> /dev/null
	./concorde -d -k50 &> /dev/null
	python makedata.py
	mv data* ../../dataset/
done