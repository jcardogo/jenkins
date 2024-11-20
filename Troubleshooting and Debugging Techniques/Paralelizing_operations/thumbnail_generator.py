"""from concurrent import futures
import argparse
import logging
import os
import sys

import PIL 
import PIL.Image

from tqdm import tqdm

def process_options():

    kwargs = {
        'format': '[%(levelname)s] %(message)s',
    }

    parser = argparse.ArgumentParser(
        description = 'Thumbnail Generator'
        fromfile_prefix_chars = '@'
    )
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')

def main():
    peocess_options()
    ##Create the thumbnails directory
    if not os.path.exists('thumbnails'):
        os.mkdir('thumbnails')
    
    executor = futures.ThreadPoolExecutor() ##Using threads for managing the tasks execution
    executor = futures.ProcessPoolExecutor() ##Using process for managing the taskexecutions

    for root, _, files in os.walk('images'):
        for basename in progress_bar(files):
            if not basename.endswith('.jpg'):
                continue
            executor.submit(process_file, root, basename)
    print ('Waiting for all threads to finish')
    executor.shutdown()

    return 0

if __name__  == "__main__":"""
