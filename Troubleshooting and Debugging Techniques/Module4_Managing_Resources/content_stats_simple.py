#!/usr/bin/env python3

'''import heapq

import zimply
import zimply.zimply

from bs4 import BeautifulSoup
from tqdm import tqdm
from memory_profiler import profile

def html_text(content):
    soup = BeautifulSoup(content, features="html.parser")

    #Kill all script and style alements
    for script in soup(["script", "style"]):
        script.extract() # rip it out
    
    #get text
    text = soup.get_text()

    return text

def generate_stats(words):
    heap = [
        (- amount, word, refs) for word, (amount, refs) in words.items()
    ]
    heap.heapify(heap)

    for n_amount, word, refs in heapq.nsmallest(50, heap):
        amount = - n_amount
        print(f'{word} with {amount}')

@profile #We've added this @profile label before the main function definition to tell the profiler that we wanted to analyze the memory consumption of it.
def main():
    zim = zimply.zimply.ZIMFile('data.zim', 'utf-8')
    words = {}

    limit = 50
    for i, content in tqdm(enumerate(zim), total=limit):
        if (i > limit):
            break

        idx = content [2]
        try:
            article = zim._get_article_by_index(idx)
            html_data = article.data
        except Exception:
            print(f'ERROR: in idx={idx}')
            continue
        if not html_data:
            continue

        text = html_text(html_data)
        for word in text.split():
            word = word.lower()
            #if the word is not in the dictionary, initialize an empty value
'''
