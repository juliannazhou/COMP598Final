'''
collects the 500 hottest posts in the subreddit specified: /r/politics
# python3 collect_hottest.py -o <output_file> <subreddit>
'''
'''
Nov 20 collected around 3:40 pm 333 per json file
'''

import argparse
import requests
import json
import sys
import os

def get_posts(subreddit_name, json_output):
    num_posts = 100

    # first 100 lines
    data = requests.get(f'http://api.reddit.com/r/{subreddit_name}/hot?limit={num_posts}',
                        headers={'User-Agent':'mac:requests (by /u/lfang)'})

    content = data.json()['data']
    posts = content['children'][:100]
    # trying
    after = content['after']
    with open(json_output,'a') as out_file:
        for p in posts:
            out_file.write(json.dumps(p))
            out_file.write("\n") 
    print(after)
    counter = 0
    after1 = after
    # for loop for the rest 900 lines
    for counter in range(3):
        data1 = requests.get(f'http://api.reddit.com/r/{subreddit_name}/hot?limit={num_posts}&after={after1}',
                            headers={'User-Agent':'mac:requests (by /u/lfang)'})
        content1 = data1.json()['data']
        # print(content.keys())
        posts1 = content1['children'][:100]
        after1 = content1['after']
        print(after1)
        with open(json_output,'a') as out_file:
            for p in posts1:
                out_file.write(json.dumps(p))
                out_file.write("\n") 
        counter += 1

def keep_it_under_500(json_output):
    data = []
    with open(json_output) as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.decoder.JSONDecodeError as j:
                pass
    data = data[:500]
    with open(json_output,'w') as out_file:
        json.dump(data, out_file)  

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o',"--output_file", help='json output file name', required = True)
    parser.add_argument('subreddit')
    args = parser.parse_args()
    # print(len(sys.argv))
    if len(sys.argv) == 4:
        
        json_output = args.output_file
        
        # json_output = sys.argv[2]
        
        subreddit_name = args.subreddit
    
        # subreddit_name = sys.argv[3]
        # which should be set to /r/politics
        # print(input_file)
    get_posts(subreddit_name,json_output)
    # keep_it_under_500(json_output)
    
    # posts = [post['data'] for post in posts if not post['data']['stickied']]
    # posts = posts[:200]
    # delete last several items to make it 500 json items


if __name__ == '__main__':
    main()