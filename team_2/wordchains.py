from collections import defaultdict, deque
import sys
import string

def make_graph(n):
    with open('/usr/share/dict/words') as f:
        words = set(word.lower() for word in f.read().splitlines() if len(word) == n)
    graph = defaultdict(list)
    for word in words:
        graph[word] = similar_words(word, words)
    return graph

def similar_words(word, words):
    sim_words = set()
    for i in range(len(word)):
        for c in string.ascii_lowercase:
            new_word = word[:i]+c+word[i+1:]
            if new_word in words and new_word != word:
                sim_words.add(new_word)
    return sim_words

#def walk(start_node, end_node, graph, visited=set(), chain=[]):
#    graph_words = graph[start_node]
#    if end_node in graph_words:
#        print "win"
#        return
#    for word in graph_words:
#        visited.add(word)

def walk(graph, start, end):
    paths = deque([[start]])
    while True:
        path = paths.popleft()
        current_node = path[-1]
        next_nodes = graph[current_node]
        if end in next_nodes:
            return path + [end]
        paths.extend([path + [node] for node in next_nodes])

def solve(start_word, end_word):
    assert len(start_word) == len(end_word)
    graph = make_graph(len(start_word))
    return walk(graph, start_word, end_word)

if __name__ == "__main__":
    start_word, end_word = sys.argv[1:]
    print " -> ".join(solve(start_word, end_word))
