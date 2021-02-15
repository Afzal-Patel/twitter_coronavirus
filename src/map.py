#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--output_folder',default='outputs')
args = parser.parse_args()

# imports
import os
import zipfile
import datetime 
import json
from collections import Counter,defaultdict

# load keywords
hashtags = [
     '#코로나바이러스',  # coronavirus in korean
      '#コロナウイルス',  #coronavirus in japanese
      '#冠状病毒',        # coronavirus chinese
     '#covid2019',
     '#covid-2019',
     '#covid19',
      '#covid-19',
     '#coronavirus',
      '#corona',
     '#virus',
     '#flu',
     '#sick',
      '#cough',
    '#sneeze',
      '#hospital',
      '#nurse',
      '#doctor',
     '#lockdown',
#english
'#vaccine','#quarantine','#pandemic',
#german
'#impfstoff', '#quarantäne', '#pandemie', 
#spanish
'#vacuna', '#cuarentena', '#pandemia', 
#french
'#vaccin', '#quarantaine', '#pandémie'
#arabic
,'اللقاح', '#الحجر الصحي','#الجائحة#'
#urdu
,'واکسین' , '#قرنطین' , '#وبائی#' ,
#chinese
'#疫苗','#檢疫','#大流行',
#japanese
'#ワクチン、', '#検疫、', '#パンデミック',
#korean
'#백신', '#검역', '#대유행', 
#hindi
'#टीका', '#टीका', '#महामारी' ]







# initialize counters
counter_lang = defaultdict(lambda: Counter())
counter_country = defaultdict(lambda: Counter())

# open the zipfile
with zipfile.ZipFile(args.input_path) as archive:

    # loop over every file within the zip file
    for i,filename in enumerate(archive.namelist()):
        print(datetime.datetime.now(),args.input_path,filename)

        # open the inner file
        with archive.open(filename) as f:

            # loop over each line in the inner file
            for line in f:

                # load the tweet as a python dictionary
                tweet = json.loads(line)

                # convert text to lower case
                text = tweet['text'].lower()

                # search hashtags
                for hashtag in hashtags:
                    lang = tweet['lang']
                    # set country code for those with existing country codes 
                    try:
                        country = tweet['place']['country_code']
                    except:
                        try:
                            #set country to name of place not in a country
                            country = tweet['place']['name']
                        except:
                            #getting to this line means place:'null'
                            country = tweet['place']
                    if hashtag in text:
                        counter_country[hashtag][country] +=1
                        counter_lang[hashtag][lang] += 1
                    counter_lang['_all'][lang] += 1
                    counter_country['_all'][country] +=1

# open the outputfile
try:
    os.makedirs(args.output_folder)
except FileExistsError:
    pass
output_path_base = os.path.join(args.output_folder,os.path.basename(args.input_path))

output_path_lang = output_path_base+'.lang'
print('saving',output_path_lang)
with open(output_path_lang,'w') as f:
    f.write(json.dumps(counter_lang))

output_path_country = output_path_base+'.country'
print('saving',output_path_country)
with open(output_path_country,'w') as j:
    j.write(json.dumps(counter_country))
