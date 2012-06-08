import nltk
import networkx
import itertools
import sys

def getWordsLength(file,l):
    f = open(file,'r')
    words = []
    for line in f.readlines():
        line = line.rstrip()
        if len(line) == l:
           words.append(line)

    return words

def getWordPairs(words):
    return itertools.ifilter(lambda x: nltk.metrics.distance.edit_distance(x[0], x[1]) == 1, itertools.product(words, words))

def main():
    query = raw_input('Enter two words. seperted by a space. make sure they are the same length: ')
    w1, w2 = query.split(' ')
    words = getWordsLength('/usr/share/dict/words',len(w1))
    words = getWordPairs(words)

    #words = [('cat','bat'),('bog','dog')]
    G = networkx.Graph()
    G.add_edges_from(words)
    print networkx.shortest_path(G, w1, w2)

if __name__ == '__main__':
    main()	

