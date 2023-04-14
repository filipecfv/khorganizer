"""
Version: 1.0
Last modified: 2023-IV-13
Description: a simple script that organizes kindle highlights
Author: github.com/filipecfv 
License: GPL-3.0
"""

# SUPPORTED LANGUAGES
en = '- Your Highlight'
pt = '- Seu destaque'

import sys
import re

def unique(l):
    u = []
    [u.append(x) for x in l if x not in u]
    return u

def write(name, arq):
    with open(name, 'w') as f:
        f.write(arq)

def final_message(text, name):
    print(len(text), 'lines successfully converted into {}!'.format(name))
    write(name, text)

def to_org(highlights, name):
    org = []
    for i in highlights: 
        if i.startswith('*'):
            org.append(i)
        else:
            org.append('- ' + i)
    org = ''.join(org)        
    final_message(org, name)   

def organize(highlights, name):
    t = open(highlights, "r").read().replace('\ufeff', '')
    t = re.split('(\n)', t)
    t = ['==========', '\n'] + t
    [t.remove(i) for i in t if i.startswith(pt) or i.startswith(en)]
    t = sorted(''.join(t).replace('=\n', '\n=').split('========='))
    t = ''.join(t).replace('\n=', '\n* ')
    t = re.split('(\n)', t)
    t = unique(t)
    t = [i for i in t if i not in {'', '\n', '* '}]
    t = [i + '\n' for i in t]
    to_org(t, name)

def list_books(highlights):
    l = open(highlights, "r").read() 
    l = l.split('\n')
    [print(i) for i in l if i.startswith('*')]

def help():
    with open('help', 'r') as help:
        help = help.read()
        print(help)

def main():
    if len(sys.argv) <= 1: 
        print("Sorry: you haven't provided a function")
    else: 
        if sys.argv[1] == "organize":
            print('Organizing...')
            if len(sys.argv) < 4:
                print("Sorry: you haven't provided enough arguments for the 'organize' function")
            else: 
                organize(sys.argv[2], sys.argv[3])    
        if sys.argv[1] == "list_books": 
            if len(sys.argv) < 3:
                print("Sorry: you haven't provided enough arguments for the 'list_books' function")
            else: 
                list_books(sys.argv[2])
        if sys.argv[1] == "help":
            help() 

if (__name__ == "__main__"):
    main()         
