'''
For the purpose of computing the tf-idf scores of words, this script is intended to merge the posts contained in our filtered and annotated TSV files (coded_file) with the non-Trump and non-Biden posts that were initially discarded (taken from json_file).
All non-Trump and non-Biden posts are coded under the category "Non-candidate" to differentiate them from our other topics. 

Usage: python3 merge_posts.py -o ../data/tf-ifd_tsv/20201120_conservative.tsv ../data/20201120_conservative.json ../data/filtered_tsv_coded/20201120_conservative_c.tsv 
'''

import argparse
import pandas as pd
import json
import random
import csv
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--output_file')
    parser.add_argument('json_file')
    parser.add_argument('coded_file')    

    args = parser.parse_args()
    output_file = args.output_file
    json_file = args.json_file
    coded_file = args.coded_file
    
    data = []   
    with open(json_file) as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.decoder.JSONDecodeError as j:
                pass

    cleaned_data = []
    for line in data:
        post_title = line['data']['title']
        if not re.search(r'\bTrump\b', post_title) and not re.search(r'\bBiden\b', post_title):
            cleaned_data.append(line)
    
    with open(output_file,'w') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(['Name', 'title', 'coding'])
        for p in cleaned_data:
            post_title = p['data']['title']
            post_id = p['data']['name']
            coding = "Non-candidate"
            tsv_writer.writerow([post_id, post_title, coding])

        with open(coded_file,'r') as cod_file:
            for line in cod_file:
                lst = line.rstrip().split('\t',2)
                if lst == ['Name', 'title', 'coding']:
                    pass
                else:
                    tsv_writer.writerow(lst)
            

if __name__ == '__main__':
    main()
