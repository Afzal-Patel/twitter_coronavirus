#Coronavirus Analysis

This repo analyzes the activity of various coronavirus hashtags on twitter.
The dataset used consists of all geotagged tweets sent in 2020 (around 1.1 billion tweets),
and is split into 365 .zip files. Each .zip file is partitioned by tweets sent within the hour.

The src directory contains three python programs:
1. map.py parses and extracts information from every .zip file, and then saves the data by writing to 
corresponing (named by day) .lang and .country files located in the outputs directory.
2. reduce.py combines all of the outputs from map.py, resulting in the files found within the reduced directory: reduced.lang and reduced.country.
3. visualize.py displays the contents of individual or merged .lang or .country files.

run_maps.sh is the bash script used to run map.py on every .zip file in parallel.
nohup.out.txt shows the command line prompts while running run_maps.sh from start to finish.

The viz directory contains all of the saved outputs from visualize.py,
split by country and language for every hashtag in the map.py program.
The results depict the frequency of tweet country/language that used the hashtag.
Each file is named after the hashtag it represents. 
The sub-directories in viz groups hashtags that are in different languages.




