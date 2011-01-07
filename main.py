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
    lst[len(lst)-1] = word
    
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
            wmap.put(prev_words)
    return wmap

def init_words(words, wmap) :
    for 

def gen_sentence(seed, wmap) :
    sentence = seed
    word = seed
    prev_words = [None] * order
    init_words(prev_words, wmap)
    while not word[-1:] in conclusions :
        val = random.randint(0, wmap.count-1)
        for key in wmap.table.keys() :
            if wmap.order > 0 :
                count += wmap.table[key].count
            else :
                count += wmap.table[key]
            if count >= val :
                word = key
                break
        sentence += " " + word
        shiftl_words(prev_words, word)
        

    wmap = wmap.table.get(word, None)



    while not word[-1:] in conclusions :
        while not word[-1:] in conclusions and wmap.order > 0 :
            val = random.randint(0, wmap.count-1)
            count = 0
            for key in wmap.table.keys() :
                if wmap.order > 0 :
                    count += wmap.table[key].count
                else :
                    count += wmap.table[key]
                if count >= val :
                    word = key
                    break
            sentence += " " + word
        if wmap.order
        wmap = wmap.table[key]
        wmap = wmap.table.get(key, None)
    return sentence
        


def main() :
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", type="string",
                      help="Specify a text file to learn from.", default=None)
    parser.add_option("-s", "--seed", dest="seed", type="string",
                      help="Specify a word or phrase to seed the generated sentence.", default="the")
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
    
    (ops, args) = parser.parse_args()
    
    if ops.filename :
        wmap = parse_file(ops.filename, ops.order)
        print gen_sentence(ops.seed, wmap)
    
    
    


if __name__ == '__main__' :
    main()
