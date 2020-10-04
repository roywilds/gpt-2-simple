"""
Roy Wilds
2020-09-07

Simple utility to extract payload from downloaded resources. See NLP-3 ticket for info about resources.
File can be downloaded from https://www.kaggle.com/hsankesara/medium-articles

Example usage:
    python extractor.py --input-file /data/NLP/articles.csv

Known Limitations:
- Very limited error handling.
- In medium_articles() function could do a more Pythonic handling of stdout vs file output

"""

import csv
import sys


def medium_articles(in_file, out_file):
    if out_file is not None:
        output_file_handler = open(out_file, 'w')
    with open(in_file, 'r') as input_file_handler:
        reader = csv.reader(input_file_handler, delimiter=',', quotechar='"')
        for row in reader:
            if out_file is None:
                print(row[-1])  # Last column has content of article
            else:
                output_file_handler.write(row[-1] + '\n')
    if output_file is not None:
        output_file_handler.close()
    return


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Stitch together multiple responses into one.')
    parser.add_argument('--input-file', type=str, action='store', default=None)
    parser.add_argument('--output-file', type=str, action='store', default=None)

    args = parser.parse_args()
    if args.input_file is None:
        sys.stderr.write('You must provide the --input-file option that has the path to the articles.csv file.')
        sys.exit(1)
    input_file = args.input_file
    output_file = args.output_file
    medium_articles(input_file, output_file)
