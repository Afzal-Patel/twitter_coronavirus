#!/bin/bash

hashtags=(
     '#코로나바이러스'  
     '#コロナウイルス'  
      '#冠状病毒'        
     '#covid2019'
     '#covid-2019'
     '#covid19'
      '#covid-19'
     '#coronavirus'
      '#corona'
     '#virus'
     '#flu'
     '#sick'
      '#cough'
    '#sneeze'
      '#hospital'
      '#nurse'
      '#doctor'
     '#lockdown'
'#vaccine'
'#quarantine'
'#pandemic'
'#impfstoff' 
'#quarantäne' 
'#pandemie' 
'#vacuna' 
'#cuarentena' 
'#pandemia' 
'#vaccin' 
'#quarantaine' 
'#pandémie'
'#疫苗'
'#大流行'
'#パンデミック'
'#백신'
'#대유행' )

#reduce step: create reduced files
#./src/reduce.py --input_paths outputs/geoTwitter*.lang --output_path=reduced/reduced.lang
#./src/reduce.py --input_paths outputs/geoTwitter*.country --output_path=reduced/reduced.country

#results:
#compile viz into test_viz_output/country_viz and test_viz_output/lang_viz directories
for ht in ${hashtags[@]}; do
    ./src/visualize.py --input_path=reduced/reduced.country --key=$ht | head > test_viz_output/country_viz/$ht;
    ./src/visualize.py --input_path=reduced/reduced.lang --key=$ht | head > test_viz_output/lang_viz/$ht;
done
