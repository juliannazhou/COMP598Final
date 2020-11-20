'''
accepts one of the files you collected from Reddit and outputs a random
selection of posts from that file to a tsv (tab separated value) file.
'''
import argparse
import pandas as pd
import json
import random
import linecache
import csv
def random_lines(json_file):
    idxs = random.sample(range(500),2)
    return [linecache.getline(json_file,i) for i in idxs]
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--output_file')
    parser.add_argument('json_file')
    # parser.add_argument('num_posts_to_output')
    
    args = parser.parse_args()
    output_file = args.output_file
    json_file = args.json_file
    # num_posts = args.num_posts_to_output
    
    data = []
    # with open(json_file) as f:
    #     file_len = len(f.readlines())
    with open(json_file) as f:
        # print(file_len)
        for line in f:
            data.append(json.loads(line))
    # if file_len < int(num_posts):
    #     samples = random.sample(data,int(num_posts))
    # else:
    #     samples = random.sample(data,int(num_posts))
    # print(sampling)
        
    with open(output_file,'w') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(['Name', 'title', 'coding'])
        for d in data:
            post_title = d['data']['title']
            post_id = d['data']['name']
            coding = None
            tsv_writer.writerow([post_id, post_title, coding])
    

if __name__ == '__main__':
    main()