#!/usr/bin/python
from optparse import OptionParser
import MySQLdb
import random
from WordMap import WordMap

conclusions = ['.', '?', '!']

def shift_listl(lst) :
    for i in range(len(lst)-1) :
        lst[i] = lst[i+1]

def shift_wordsl(lst, word) :
    shift_listl(lst)
    lst[-1] = word
    
def parse_file(fname, order) :
    fd = open(fname, 'r')
    prev_words = [None] * (order + 1)
    wmap = WordMap(order)
    for line in fd :
        if not line.strip() :
            continue
        words = line.strip().split(" ")
        for word in words :
            shift_wordsl(prev_words, word)
            if None not in prev_words :
                wmap.put(prev_words)
    return wmap

def init_words(words, wmap) :
    if words[-1] == None :
        word = wmap.get_word(random.randint(0, wmap.count-1))
        words[-1] = word

def gen_sentence(seed, wmap, order) :
    #sentence = seed
    words = [None] * order
    #words[-len(seed):] = seed
    init_words(words, wmap)
    sentence = []
    word = words[-1]
    sentence.append(word)
    while not word[-1:] in conclusions :
        word = wmap.get_next_word(words)
        sentence.append(word)
        shift_wordsl(words, word)
        
    return ' '.join(sentence)
        


def main() :
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", type="string",
                      help="Specify a text file to learn from.", default=None)
    parser.add_option("-s", "--seed", dest="seed", type="string",
                      help="Specify a word or phrase to seed the generated sentence.", default='')
    parser.add_option("-d", "--database", dest="database", type="string",
                      help="Specify a MySQL DB to use", default=None)
    parser.add_option("-t", "--table", dest="table", type="string",
                      help="Specify a MySQL table to use", default="babyTalk")
    parser.add_option("-u", "--user", dest="user", type="string",
                      help="Specify the MySQL user name. Required if using -db option.", default=None)
    parser.add_option("-p", "--password", dest="pword", type="string",
                      help="Specify the MySQL password. Require if using -db option.", default=None)
    parser.add_option("-O", "--order", dest="order", type="int",
                      help="Specify the order of the Markov Chain.", default=2)
    
    (opts, args) = parser.parse_args()
    
    if opts.filename :
        wmap = parse_file(opts.filename, opts.order)
        print gen_sentence(opts.seed, wmap, opts.order)
    
    
    


if __name__ == '__main__' :
    main()
