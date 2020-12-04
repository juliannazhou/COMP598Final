'''
This script groups our 2000 posts by topic/category and computes the word counts of all words within each category. It outputs the word counts to the given JSON file as a dictionary.

Usage: python3 compile_word_counts.py -o ../data/tf-ifd_tsv/word_counts.json ../data/tf-ifd_tsv/all_posts.tsv
'''

import pandas as pd
import argparse
import json


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', required = True, help = "Output file in JSON format")
	parser.add_argument('tsv_file')
	args = parser.parse_args()
	
	df = pd.read_csv(args.tsv_file, sep='\t')
	df['title'] = df['title'].str.replace(r'[^0-9a-zA-Z]+', ' ').str.lower()

	georgia_recount = df[df['coding']=="GR"]
	subvert_election = df[df['coding']=="SE"]
	tax_investigation = df[df['coding']=="TI"]
	win_aftermath = df[df['coding']=="WA"]
	foreign_relations = df[df['coding']=="FR"]
	group_interest = df[df['coding']=="GI"]
	others = df[df['coding']=="O"]
	non_candidate = df[df['coding']=="Non-candidate"]

	GR_dict = georgia_recount.title.str.split(expand=True).stack().value_counts().to_dict()
	#GR_count = dict()
	#for (key, value) in GR_dict.items():
	#	if value >= 5:
	#		GR_count[key] = value
	SE_dict = subvert_election.title.str.split(expand=True).stack().value_counts().to_dict()
	TI_dict = tax_investigation.title.str.split(expand=True).stack().value_counts().to_dict()
	WA_dict = win_aftermath.title.str.split(expand=True).stack().value_counts().to_dict()
	FR_dict = foreign_relations.title.str.split(expand=True).stack().value_counts().to_dict()
	GI_dict = group_interest.title.str.split(expand=True).stack().value_counts().to_dict()
	O_dict = others.title.str.split(expand=True).stack().value_counts().to_dict()
	NC_dict = non_candidate.title.str.split(expand=True).stack().value_counts().to_dict()

	word_count = {"Georgia recount": GR_dict, "Subvert election": SE_dict, "Tax investigation": TI_dict, "Win & Aftermath": WA_dict, "Foreign relations": FR_dict, "Group interest": GI_dict, "Others": O_dict, "Non-candidate": NC_dict}
	
	with open(args.o,'w') as out_file:
		json.dump(word_count, out_file, indent=2)


if __name__ == '__main__':
	main()

