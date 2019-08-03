import sys

import io_main

sys.path.append('../display')
import colors as dclr

sys.path.append('../handler')
import writer as hwriter

def write():
    question = "Do you want to add an entry? [y/n]"
    entries = list()

    while True:
           choice = io_main.query_yes_no(question) 
           
           if choice == "y":
               entry = input()
               entries.append(list(entry))
           else:
               return

    hwriter.write('list.csv', entries)
