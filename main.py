import zipfile
from tqdm import tqdm
import time
import argparse

argp = argparse.ArgumentParser(usage= "zipBRUTE.py -f FILE -w WORDLIST")
argp.add_argument("-f","--file", required=True)
argp.add_argument("-w","--wordlist",required=True)

parser = argp.parse_args()

zip_file = parser.file
wordlist = parser.wordlist

from algorithm.zipBRUTE import BruteForce

this = BruteForce(zip_file, wordlist)
this.zip_brute()

