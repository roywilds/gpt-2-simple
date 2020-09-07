"""
Roy Wilds
2020-09-07

Simple utility to extract payload from downloaded resources. See NLP-3 ticket for info about resources.
"""

import csv


def medium_articles():
    with open('/data/NLP/articles.csv', 'r') as file_handler:
        reader = csv.reader(file_handler, delimiter=',', quotechar='"')
        for row in reader:
            print(row[-1])  # Last column has content of article
    return


if __name__ == "__main__":
    medium_articles()
