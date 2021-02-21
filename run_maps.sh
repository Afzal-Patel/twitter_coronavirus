#!/bin/bash

#map step 

for item in /data-fast/twitter2020/*.zip; do
    nohup ./src/map.py --input_path=$item &
done
