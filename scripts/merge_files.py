'''
This script takes as input the 6 previously merged TSV files (politics and conservative posts for each of the 3 dates over which they were collected) and merges them into one big TSV file containing 2000 posts (each associated to either a topic or the "Non-candidate" category) in order to make the computation of tf-idf scores easier.

Usage: python3 merge_files.py ../data/tf-ifd_tsv/20201120_conservative.tsv ../data/tf-ifd_tsv/20201120_politics.tsv ../data/tf-ifd_tsv/20201121_conservative.tsv ../data/tf-ifd_tsv/20201121_politics.tsv ../data/tf-ifd_tsv/20201122_conservative.tsv ../data/tf-ifd_tsv/20201122_politics.tsv  
'''

import argparse
import csv

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file1')
	parser.add_argument('file2')
	parser.add_argument('file3')
	parser.add_argument('file4')
	parser.add_argument('file5')
	parser.add_argument('file6')

	args = parser.parse_args()

	with open('../data/tf-ifd_tsv/all_posts.tsv','w') as output_file:
		tsv_writer = csv.writer(output_file, delimiter='\t')
		
		with open(args.file1,'r') as file1:
			for line in file1:
				lst = line.rstrip().split('\t',2)
				tsv_writer.writerow(lst)
		with open(args.file2,'r') as file2:
			for line in file2:
				lst = line.rstrip().split('\t',2)
				if lst == ['Name', 'title', 'coding']:
					pass
				else:
					tsv_writer.writerow(lst)
		with open(args.file3,'r') as file3:
			for line in file3:
				lst = line.rstrip().split('\t',2)
				if lst == ['Name', 'title', 'coding']:
					pass
				else:
					tsv_writer.writerow(lst)
		with open(args.file4,'r') as file4:
			for line in file4:
				lst = line.rstrip().split('\t',2)
				if lst == ['Name', 'title', 'coding']:
					pass
				else:
					tsv_writer.writerow(lst)
		with open(args.file5,'r') as file5:
			for line in file5:
				lst = line.rstrip().split('\t',2)
				if lst == ['Name', 'title', 'coding']:
					pass
				else:
					tsv_writer.writerow(lst)
		with open(args.file6,'r') as file6:
			for line in file6:
				lst = line.rstrip().split('\t',2)
				if lst == ['Name', 'title', 'coding']:
					pass
				else:
					tsv_writer.writerow(lst)


if __name__ == '__main__':
	main()
