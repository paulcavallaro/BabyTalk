
class WordMap :
    """
    Will hold a mapping from phrases to frequency
    """
    def __init__(self, order) :
        self.order = order
        self.count = 0
        self.table = dict()
 

    def put(self, word_list) :
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
