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
    
    args = parser.parse_args()
    output_file = args.output_file
    json_file = args.json_file
    
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
        if re.search(r'\bTrump\b', post_title) or re.search(r'\bBiden\b', post_title):
            cleaned_data.append(line)
    
    # print(cleaned_data[0]['data']['title'])
    with open(output_file,'w') as out_file:
        for p in cleaned_data:
            out_file.write(json.dumps(p))
            out_file.write("\n")     
            

if __name__ == '__main__':
    main()