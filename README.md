#Coronavirus Twitter Analysis

This repo analyzes the activity of various coronavirus hashtags on twitter.
The dataset used consists of all geotagged tweets sent in 2020 (around 1.1 billion tweets).
The data is split into 365 .zip files, and each .zip file is partitioned by tweets sent within the hour.

The src directory contains three python programs:

1. map.py parses and extracts information from every .zip file, and then saves the data by writing to 
corresponing (named by day) .lang and .country files located in the outputs directory.
2. reduce.py combines all of the outputs from map.py, resulting in the files within the reduced directory: reduced.lang and reduced.country.
3. visualize.py displays the contents of individual or merged .lang or .country files.

The viz directory contains the saved outputs from visualize.py, 
and splits the data by country and language for every hashtag in the map.py program.
The sub-directories in viz groups hashtags that are in different languages.

run_maps.sh is the bash script used to gather all of the data and run map.py on every .zip file in parallel.

nohup.out shows the command line prompts from running run_maps.sh start to finish.

Results: todo


