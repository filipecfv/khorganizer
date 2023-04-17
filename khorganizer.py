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

def organize(txt_input, org_output):
    open_text_file(txt_input, org_output)

def open_text_file(txt_input, org_output):
    t = open(txt_input, "r").read()
    clean_file_from_ufeff(t, org_output)

def clean_file_from_ufeff(t, org_output):
    t = t.replace('\ufeff', '')
    split_into_a_list_by_line_break(t, org_output)

def split_into_a_list_by_line_break(t, org_output): 
    t = re.split('(\n)', t)
    add_top_division(t, org_output)

def add_top_division(t, org_output):
    t = ['==========', '\n'] + t   
    remove_your_highlight_message(t, org_output)

def remove_your_highlight_message(t, org_output): 
    [t.remove(i) for i in t if i.startswith(pt) or i.startswith(en)]
    join_elements_and_replace_headings_identifiers(t, org_output)

def join_elements_and_replace_headings_identifiers(t, org_output):
    t = ''.join(t).replace('=\n', '\n=')
    split_by_division_line(t, org_output) 

def split_by_division_line(t, org_output): 
    t = t.split('=========')
    sort_headings(t, org_output)

def sort_headings(t, org_output): 
    t = sorted(t)
    join_sorted_elements(t, org_output)

def join_sorted_elements(t, org_output): 
    t = ''.join(t)
    add_heading_asterisk(t, org_output)

def add_heading_asterisk(t, org_output): 
    t = t.replace('\n=', '\n* ')
    split_sorted_elements_by_line_break(t, org_output)

def split_sorted_elements_by_line_break(t, org_output):
    t = re.split('(\n)', t)
    unique_headings(t, org_output)

def unique_headings(t, org_output): 
    u = []
    [u.append(x) for x in t if x not in u]
    t = u
    clean_file_from_remainings(t, org_output)

def clean_file_from_remainings(t, org_output): 
    t = [i for i in t if i not in {'', '\n', '* '}]
    add_line_breaks(t, org_output)

def add_line_breaks(t, org_output): 
    t = [i + '\n' for i in t]
    to_org(t, org_output)

def to_org(txt_input, org_output):
    org = []
    for i in txt_input: 
        if i.startswith('*'):
            org.append(i)
        else:
            org.append('- ' + i)
    org = ''.join(org)        
    final_message(org, org_output)   

def final_message(text, org_output):
    print(len(text), 'lines successfully converted into {}!'.format(org_output))
    write(org_output, text)

def write(org_output, arq):
    with open(org_output, 'w') as f:
        f.write(arq)

def list_books(org_input):
    l = open(org_input, "r").read() 
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
