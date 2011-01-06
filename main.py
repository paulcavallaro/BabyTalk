#!/usr/bin/python
from optparse import OptionParser
import sys
import MySQLdb

global_dict = dict()

def shift_listl(lst) :
    for i in range(len(lst)-1) :
        lst[i] = lst[i+1]

def shift_wordsl(lst, word) :
    shift_listl(lst)
    lst[len(lst)] = word
    

def parse_file(fname, db=None, table=None, user=None, pword=None) :
    fd = open(fname, 'r')
    order = 2;
    last_words = [None] * order
    for line in fd :
        words = line.split(" ")
        for word in words :
            if !last_words.count(None) :
                shift_wordsl(last_words, word)
                


def main() :
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", type="string",
                      help="Specify a text file to learn from.", default=None)
    parser.add_option("-s", "--seed", dest="seed_phrase", type="string",
                      help="Specify a word or phrase to seed the generated sentence.", default=None)
    parser.add_option("-db", "--database", dest="database", type="string",
                      help="Specify a MySQL DB to use", default=None)
    parser.add_option("-t", "--table", dest="table", type="string",
                      help="Specify a MySQL table to use", default="babyTalk")
    parser.add_option("-u", "--user", dest="user", type="string",
                      help="Specify the MySQL user name. Required if using -db option.", default=None)
    parser.add_option("-p", "--password", dest="pword", type="string",
                      help="Specify the MySQL password. Require if using -db option.", default=None)
    parser.add_option("-od", "--order", dest="order", type="int",
                      help="Specify the order of the Markov Chain.", default=2)
    
    (options, args) = parser.parse_args()
    
    if filename :
        parse_file(options.filename, options.database, options.table, options.user, options.pword)
        
    
    
    


if __name__ == '__main__' :
    main()
