"""
Docstring
"""

import random

class WordMap :
    """
    Will hold a mapping from phrases to frequency
    """
    def __init__(self, order) :
        """
        Constructor which takes the order of 
        the markov chain
        """
        self.order = order
        self.count = 0
        self.table = dict()
 

    def put(self, word_list) :
        """
        Puts a phrase into the word list, incrementing
        the count of appropriate lower order WordMaps
        and creating lower order WordMaps as needed
        """
        self.count += 1
        word = word_list[0]
        if self.table.get(word, None) != None :
            if self.order > 0 :
                self.table[word].put(word_list[1:])
            else :
                self.table[word] += 1
        elif self.order > 0 :
            self.table[word] = WordMap(self.order-1)
            self.table[word].put(word_list[1:])
        else :
            self.table[word] = 1

    def get_word(self, index) :
        """
        Get the next word based on the previous words
        weighting the probability by the count of seen
        examples using just the index.

        Returns a tuple of the word and the corresponding
        WordMap
        """
        if index >= self.count :
            raise Exception("Index is %d, but count is only %d" 
                            % (index, self.count))

        for key in self.table.keys() :
            if self.order > 0 :
                index -= self.table[key].count
            else :
                index -= self.table[key]
            if index < 0 :
                return key


    def get_next_word(self, word_list) :
        """
        Get the next word based on the previous words
        weighting the probability by the count of seen
        examples

        Returns a tuple of the word and the corresponding
        WordMap
        """
        if len(word_list) > self.order :
            raise Exception("Looking up into a WordMap of order %d with a word_list of length %d"
                            % (self.order, len(word_list)))
        
        if None in word_list :
            index = word_list.index(None) + 1
        else :
            index = 0
            
        wmap = self
        while wmap.order > 0 and index < len(word_list) :
            wmap = wmap.table[word_list[index]]
            index += 1

        return wmap.get_word(random.randint(0, wmap.count-1))
        

        
            

        


