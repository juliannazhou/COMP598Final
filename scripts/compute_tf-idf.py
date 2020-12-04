'''
This script takes as input a JSON file containing the word counts of all words within each category/topic (i.e. the output file from compile_word_counts.py) and prints the 10 words in each category with the highest tf-idf scores to stdout, or to a file if redirected using ">".

Usage: python3 compute_tf-idf.py ../data/tf-ifd_tsv/word_counts.json > ../data/tf-ifd_tsv/top10_words.txt
'''

import pandas as pd
import argparse
import json
import math


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('json_file')
	args = parser.parse_args()

	word_list = []
	with open(args.json_file,'r') as json_file:
		wc_dict = json.load(json_file)
	for (topic, word_dict) in wc_dict.items():
		for (word, count) in word_dict.items():
			if word.isalpha() == False:
				pass
			else:
				word_list.append(word)
	GR_tfidf = dict()
	SE_tfidf = dict()
	TI_tfidf = dict()
	WA_tfidf = dict()
	FR_tfidf = dict()
	GI_tfidf = dict()
	O_tfidf = dict()	

	for (topic, word_dict) in wc_dict.items():
		if topic == "Georgia recount":
			for (word, count) in word_dict.items():
				if word.isalpha() == False:
					pass
				else:	
					score = count * math.log(len(wc_dict.keys()) / word_list.count(word))
					GR_tfidf.update({word: score})
		
		if topic == "Subvert election":
			for (word, count) in word_dict.items():
				if word.isalpha() == False:
					pass
				else:
					score = count * math.log(len(wc_dict.keys()) / word_list.count(word))
					SE_tfidf.update({word: score})

		if topic == "Tax investigation":
			for (word, count) in word_dict.items():
				if word.isalpha() == False:
					pass
				else:
					score = count * math.log(len(wc_dict.keys()) / word_list.count(word))
					TI_tfidf.update({word: score})

		if topic == "Win & Aftermath":
			for (word, count) in word_dict.items():
				if word.isalpha() == False:
					pass
				else:
					score = count * math.log(len(wc_dict.keys()) / word_list.count(word))
					WA_tfidf.update({word: score})

		if topic == "Foreign relations":
			for (word, count) in word_dict.items():
				if word.isalpha() == False:
					pass
				else:
					score = count * math.log(len(wc_dict.keys()) / word_list.count(word))
					FR_tfidf.update({word: score})

		if topic == "Group interest":
			for (word, count) in word_dict.items():
				if word.isalpha() == False:
					pass
				else:
					score = count * math.log(len(wc_dict.keys()) / word_list.count(word))
					GI_tfidf.update({word: score})

		if topic == "Others":
			for (word, count) in word_dict.items():
				if word.isalpha() == False:
					pass
				else:
					score = count * math.log(len(wc_dict.keys()) / word_list.count(word))
					O_tfidf.update({word: score})

	tfidf_dict = {"Georgia recount": sorted(GR_tfidf, key=GR_tfidf.get, reverse=True)[:10], "Subvert election": sorted(SE_tfidf, key=SE_tfidf.get, reverse=True)[:10], "Tax investigation": sorted(TI_tfidf, key=TI_tfidf.get, reverse=True)[:10], "Win & Aftermath": sorted(WA_tfidf, key=WA_tfidf.get, reverse=True)[:10], "Foreign relations": sorted(FR_tfidf, key=FR_tfidf.get, reverse=True)[:10], "Group interest": sorted(GI_tfidf, key=GI_tfidf.get, reverse=True)[:10], "Others": sorted(O_tfidf, key=O_tfidf.get, reverse=True)[:10]}
	#print(json.dumps(tfidf_dict, indent=1))
	for (topic, lst) in tfidf_dict.items():
		print(f"{topic}: {lst}")


if __name__ == '__main__':
	main()
